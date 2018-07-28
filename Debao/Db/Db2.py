#coding=gbk
'''
ibm_db的二次封装，并使用了sqlalchemy.pool.QueuePool连接池。
*）依赖于XmlConfig读取xml格式的配置，配置例子：
    <db>
        <db2>
            <test01 dsn="HOSTNAME=192.168.0.230;PORT=3700;PROTOCOL=TCPIP;" database="SAMPLE" user="db2inst1" password="123456" />
            <test02 dsn="HOSTNAME=192.168.0.230;PORT=3700;PROTOCOL=TCPIP;" database="SAMPLE" user="db2inst1" password="123456" pooling="pool_size=4;timeout=16;use_threadlocal=True" />
        </db2>
    </db>
*）参考文档：
    DBAPI-2.0说明：
        http://www.python.org/topics/database/DatabaseAPI-2.0.html
    ibm_db的参数和用法：
        http://code.google.com/p/ibm-db/wiki/APIs
    SQLAlchemy连接池的参数和用法：
        http://www.sqlalchemy.org/docs/core/pooling.html
*）运行例子：
        db = Db.Mysql.connect('test01')
        rows = db.query("SELECT ? FROM SYSIBM.SYSDUMMY1", [time.time()])
        print rows[0][0]
        row = db.queryOne("SELECT ? FROM SYSIBM.SYSDUMMY1", [time.time()])
        print row[0]
'''
import ibm_db
import ibm_db_dbi


############################################################


class Conn:

    def __init__(self, conn):
        self.conn = conn

    def query(self, *args, **kwargs):
        '''查询，返回所有行记录'''
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.fetchall()
        finally:
            cur.close()

    def queryOne(self, *args, **kwargs):
        '''查询，返回单行记录'''
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.fetchone()
        finally:
            cur.close()

    def execute(self, *args, **kwargs):
        '''执行，返回被影响的行数'''
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.rowcount
        finally:
            cur.close()

    def executeMany(self, *args, **kwargs):
        '''执行，many'''
        cur = self.conn.cursor()
        try:
            return cur.executemany(*args, **kwargs)
        finally:
            cur.close()

    def insert(self, *args, **kwargs):
        '''插入，返回自增长字段的值，没有的话返回0或者None'''
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.last_identity_val
        finally:
            cur.close()

    def commit(self):
        '''提交'''
        return self.conn.commit()

    def rollback(self):
        '''回滚'''
        return self.conn.rollback()

    def isAlive(self):
        '''检查是否存活'''
        try:
            return ibm_db.active(self.conn.conn_handler)
        except AttributeError:
            return 0

    def close(self):
        try:
            self.conn.close()
        except:
            pass

    def __del__(self):
        self.close()


############################################################


import threading
from sqlalchemy.pool import QueuePool

import XmlConfig
import ThreadUtil

_DB_LOCK_ = threading.RLock() # 保护锁
_DB_POOL_ = {} # 连接池
_DB_INST_ = {} # 连接实例

@ThreadUtil.lockingCall(_DB_LOCK_)
def connect(id, conf=None):
    '''使用连接池连接数据库'''
    if not _DB_POOL_.has_key(id):
        if not conf:
            conf = XmlConfig.get('/db/db2/' + id)
            conf.setdefault('conn_options', {})
            poolConf = conf.pop('pooling', 'pool_size=4').split(';')
            poolConf = [i.split('=') for i in poolConf]
            poolConf = dict([(i[0], eval(i[1])) for i in poolConf])
        _DB_POOL_[id] = QueuePool(lambda: ibm_db_dbi.connect(**conf), **poolConf)
    return Conn(_DB_POOL_[id].connect())

@ThreadUtil.lockingCall(_DB_LOCK_)
def get(id, conf=None):
    '''使用连接实例连接数据库（多线程共用一个连接，线程锁保护）'''
    if not _DB_INST_.has_key(id):
        _DB_INST_[id] = ThreadUtil.LockingObjectCall(connect(id, conf))
    if not _DB_INST_[id].isAlive():
        # get不是每次从pool取得新连接，没有自动重连，这里自己实现
        import os, logging
        logging.error('db2 connection lost [%s] [%s]', os.getpid(), id)
        _DB_INST_[id].close()
        del(_DB_INST_[id])
        _DB_INST_[id] = ThreadUtil.LockingObjectCall(connect(id, conf))
    return _DB_INST_[id]

@ThreadUtil.lockingCall(_DB_LOCK_)
def dispose():
    '''释放连接池'''
    _DB_INST_.clear()
    for id in _DB_POOL_:
        _DB_POOL_[id].dispose()
import atexit
atexit.register(dispose)

