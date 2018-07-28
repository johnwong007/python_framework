#coding=gbk
'''
cx_Oracle的二次封装。
*）依赖于XmlConfig读取xml格式的配置，配置例子：
    <db>
        <oracle>
            <esun dsn='BOSSNEW' user='great' password='500wanboss' />
            <esun02 dsn='BOSSNEW' user='great' password='500wanboss' threaded='True' pooling="pool_size=4;timeout=16;use_threadlocal=True" />
        </oracle>
    </db>
*）在callfunc和callproc中，可以用'$CURSOR'等来指定变量输出类型，具体支持类型请看_VAR_TYPE_。
*）参考文档：
    DBAPI-2.0说明：
        http://www.python.org/topics/database/DatabaseAPI-2.0.html
    SQLAlchemy连接池的参数和用法：
        http://www.sqlalchemy.org/docs/core/pooling.html
    cx_Oracle的参数和用法：
        http://cx-oracle.sourceforge.net/html/index.html
*）运行例子：
    dbo = Oracle.connect('esun')
    rows = dbo.query("select 'a' from dual")
    rows = dbo.query("select :1 from dual", ['b'])
    rows = dbo.query("select :myvar as id from dual", {'myvar': 'c'})
    print rows, rows[0], rows[0][0], rows[0]['id'], rows[0]['ID']
'''
import os
import cx_Oracle

# 初始化Oracle的环境变量
if not (os.environ.has_key("TNS_ADMIN") or os.environ.has_key("ORACLE_HOME")):
    os.environ["TNS_ADMIN"] = "/opt/oracle/instantclient/admin"
if not os.environ.has_key("NLS_DATE_FORMAT"):
    os.environ["NLS_DATE_FORMAT"] = "YYYY-MM-DD HH24:MI:SS"
if not os.environ.has_key("NLS_LANG"):
    os.environ["NLS_LANG"] = ".ZHS16GBK"


_VAR_TYPE_ = {
    '$STRING': cx_Oracle.STRING,
    '$NUMBER': cx_Oracle.NUMBER,
    '$CURSOR': cx_Oracle.CURSOR,
}


class Conn:

    def __init__(self, conn):
        self.conn = conn
        self.setRowFactory('default')

    def isAlive(self):
        '''检查是否存活'''
        try:
            self.conn.ping()
        except cx_Oracle.Error:
            return 0
        return 1

    def close(self):
        try:
            self.conn.close()
        except:
            pass

    def __del__(self):
        self.close()

    def setRowFactory(self, type):
        if type == 'upper':
            self._rowFactory = rowUpper
        elif type == 'lower':
            self._rowFactory = rowLower
        elif type == 'tuple':
            self._rowFactory = rowTuple
        else:
            self._rowFactory = ResultRow

    def query(self, *args, **kwargs):
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return self.fetchAll_(cur)
        finally:
            cur.close()

    def execute(self, *args, **kwargs):
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.rowcount
        finally:
            cur.close()

    def executemany(self, *args):
        cur = self.conn.cursor()
        try:
            return cur.executemany(*args)
        finally:
            cur.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def callproc(self, name, args=[]):
        cur = self.conn.cursor()
        argtypes = {}
        for i in range(len(args)):
            if args[i] in _VAR_TYPE_:
                argtypes[i] = args[i]
                args[i] = cur.var(_VAR_TYPE_[args[i]])
        try:
            ret = cur.callproc(name, args)
            for i in argtypes:
                args[i] = self.getVarValue_(args[i], argtypes[i])
            return ret
        finally:
            cur.close()

    def callfunc(self, name, retype, args=[]):
        cur = self.conn.cursor()
        argtypes = {}
        for i in range(len(args)):
            if args[i] in _VAR_TYPE_:
                argtypes[i] = args[i]
                args[i] = cur.var(_VAR_TYPE_[args[i]])
        try:
            ret = cur.callfunc(name, _VAR_TYPE_[retype], args)
            for i in argtypes:
                args[i] = self.getVarValue_(args[i], argtypes[i])
            return ret
        finally:
            cur.close()

    def getVarValue_(self, v, t):
        if t == '$STRING':
            return v.getvalue()
        elif t == '$CURSOR':
            cur = v.getvalue()
            rows = self.fetchAll_(cur)
            cur.close()
            return rows
        else:
            return v

    def fetchAll_(self, cur):
        return ResultSet(cur.description, cur.fetchall(), self._rowFactory)


class ResultSet:
    ''' 结果集。可以当tuple用，每个记录到了调用的时候才根据factory转化。
    '''

    def __init__(self, description, datas, factory):
        self.description = description
        self.datas = datas
        self.factory = factory
        self.index = 0
        self.length = len(datas)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        return self.factory(self.description, self.datas[key])

    def __iter__(self):
        return self

    def next(self):
        if self.index >= self.length:
            self.index = 0
            raise StopIteration
        self.index += 1
        return self.factory(self.description, self.datas[self.index - 1])


class ResultRow:
    ''' 记录行。可以当tuple或者dict使用，不区分大小写。
    '''

    def __init__(self, description, data):
        self.description = dict([(description[i[0]][0], i[0]) for i in enumerate(description)])
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data[key]
        else:
            return self.data[self.description[key.upper()]]

    def __iter__(self):
        return iter(self.data)

    def keys(self):
        return self.description.keys()


def rowUpper(description, data):
    # row factory: dict with upper key
    return dict([(i[1][0].upper(), data[i[0]]) for i in enumerate(description)])

def rowLower(description, data):
    # row factory: dict with lower key
    return dict([(i[1][0].lower(), data[i[0]]) for i in enumerate(description)])

def rowTuple(description, data):
    # row factory: tuple
    return data


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
            conf = XmlConfig.get('/db/oracle/' + id)
            for i in ['threaded', 'twophase', 'events']:
                if conf.has_key(i):
                    conf[i] = eval(str(conf[i]))
            poolConf = conf.pop('pooling', 'pool_size=4').split(';')
            poolConf = [i.split('=') for i in poolConf]
            poolConf = dict([(i[0], eval(i[1])) for i in poolConf])
        _DB_POOL_[id] = QueuePool(lambda: cx_Oracle.connect(**conf), **poolConf)
    for i in range(_DB_POOL_[id].size() + 1):
        conn = _DB_POOL_[id].connect()
        try:
            conn.ping()
            break
        except cx_Oracle.Error:
            conn.invalidate()
    return Conn(conn)

@ThreadUtil.lockingCall(_DB_LOCK_)
def get(id, conf=None):
    '''使用连接实例连接数据库（多线程共用一个连接，线程锁保护）'''
    if not _DB_INST_.has_key(id):
        _DB_INST_[id] = ThreadUtil.LockingObjectCall(connect(id, conf))
    if not _DB_INST_[id].isAlive():
        # get不是每次从pool取得新连接，没有自动重连，这里自己实现
        import os, logging
        logging.error('oracle connection lost [%s] [%s]', os.getpid(), id)
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

