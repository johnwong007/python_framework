#coding=gbk
'''
ibm_db�Ķ��η�װ����ʹ����sqlalchemy.pool.QueuePool���ӳء�
*��������XmlConfig��ȡxml��ʽ�����ã��������ӣ�
    <db>
        <db2>
            <test01 dsn="HOSTNAME=192.168.0.230;PORT=3700;PROTOCOL=TCPIP;" database="SAMPLE" user="db2inst1" password="123456" />
            <test02 dsn="HOSTNAME=192.168.0.230;PORT=3700;PROTOCOL=TCPIP;" database="SAMPLE" user="db2inst1" password="123456" pooling="pool_size=4;timeout=16;use_threadlocal=True" />
        </db2>
    </db>
*���ο��ĵ���
    DBAPI-2.0˵����
        http://www.python.org/topics/database/DatabaseAPI-2.0.html
    ibm_db�Ĳ������÷���
        http://code.google.com/p/ibm-db/wiki/APIs
    SQLAlchemy���ӳصĲ������÷���
        http://www.sqlalchemy.org/docs/core/pooling.html
*���������ӣ�
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
        '''��ѯ�����������м�¼'''
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.fetchall()
        finally:
            cur.close()

    def queryOne(self, *args, **kwargs):
        '''��ѯ�����ص��м�¼'''
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.fetchone()
        finally:
            cur.close()

    def execute(self, *args, **kwargs):
        '''ִ�У����ر�Ӱ�������'''
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.rowcount
        finally:
            cur.close()

    def executeMany(self, *args, **kwargs):
        '''ִ�У�many'''
        cur = self.conn.cursor()
        try:
            return cur.executemany(*args, **kwargs)
        finally:
            cur.close()

    def insert(self, *args, **kwargs):
        '''���룬�����������ֶε�ֵ��û�еĻ�����0����None'''
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.last_identity_val
        finally:
            cur.close()

    def commit(self):
        '''�ύ'''
        return self.conn.commit()

    def rollback(self):
        '''�ع�'''
        return self.conn.rollback()

    def isAlive(self):
        '''����Ƿ���'''
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

_DB_LOCK_ = threading.RLock() # ������
_DB_POOL_ = {} # ���ӳ�
_DB_INST_ = {} # ����ʵ��

@ThreadUtil.lockingCall(_DB_LOCK_)
def connect(id, conf=None):
    '''ʹ�����ӳ��������ݿ�'''
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
    '''ʹ������ʵ���������ݿ⣨���̹߳���һ�����ӣ��߳���������'''
    if not _DB_INST_.has_key(id):
        _DB_INST_[id] = ThreadUtil.LockingObjectCall(connect(id, conf))
    if not _DB_INST_[id].isAlive():
        # get����ÿ�δ�poolȡ�������ӣ�û���Զ������������Լ�ʵ��
        import os, logging
        logging.error('db2 connection lost [%s] [%s]', os.getpid(), id)
        _DB_INST_[id].close()
        del(_DB_INST_[id])
        _DB_INST_[id] = ThreadUtil.LockingObjectCall(connect(id, conf))
    return _DB_INST_[id]

@ThreadUtil.lockingCall(_DB_LOCK_)
def dispose():
    '''�ͷ����ӳ�'''
    _DB_INST_.clear()
    for id in _DB_POOL_:
        _DB_POOL_[id].dispose()
import atexit
atexit.register(dispose)

