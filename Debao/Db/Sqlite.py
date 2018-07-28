#coding=gbk
"""
sqlite3的二次封装
*）参考文档：
    DBAPI-2.0说明：
        http://www.python.org/topics/database/DatabaseAPI-2.0.html
    sqlite3的参数和用法：
        http://docs.pysqlite.googlecode.com/hg/sqlite3.html
*）运行例子：
    import Db.Sqlitex
    db = Db.Sqlitex.connect('asdf.db')
    print db.execute('create table if not exists t_test(f_a integer, f_b text, primary key (f_a))')
    print db.insert('insert into t_test values (null, 123)')
    print db.execute('insert into t_test values (null, 456)')
    print db.insert('insert into t_test values (null, ?)', [789])
    print db.executeMany('insert into t_test values (null, ?)', [[1],[2],[3]])
    print db.query('select * from t_test')
    print db.queryOne('select * from t_test limit 1')['f_b']
    db.commit()
    db.close()
"""
import os
try:
    import sqlite3
except:
    import pysqlite2.dbapi2 as sqlite3


############################################################


class Conn:

    def __init__(self, conn):
        self.conn = conn
        self.conn.row_factory = sqlite3.Row
        self.conn.text_factory = str

    def query(self, *args, **kwargs):
        """查询，返回所有行记录"""
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.fetchall()
        finally:
            cur.close()

    def queryOne(self, *args, **kwargs):
        """查询，返回单行记录"""
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.fetchone()
        finally:
            cur.close()

    def execute(self, *args, **kwargs):
        """执行，返回被影响的行数"""
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.rowcount
        finally:
            cur.close()

    def executeMany(self, *args, **kwargs):
        """执行，many"""
        cur = self.conn.cursor()
        try:
            cur.executemany(*args, **kwargs)
        finally:
            cur.close()

    def insert(self, *args, **kwargs):
        """插入，返回自增长字段的值，没有的话返回None"""
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.lastrowid
        finally:
            cur.close()

    def commit(self):
        """提交"""
        return self.conn.commit()

    def rollback(self):
        """回滚"""
        return self.conn.rollback()

    def isAlive(self):
        """检查是否存活"""
        return 1

    def close(self):
        try:
            self.conn.close()
        except:
            pass

    def __del__(self):
        self.close()


############################################################


import ThreadUtil


def connect(database, **conf):
    """使用连接池连接数据库"""
    dname = os.path.dirname(database)
    if dname and not os.path.isdir(dname):
        os.makedirs(dname, 0755)
    thread_protect = conf.pop('thread_protect', True) # 是否使用线程保护模式
    conf.setdefault('check_same_thread', False) # 默认不检查是否同线程
    conf.setdefault('timeout', 60) # 默认等待解锁时间为60秒
    if conf.pop('auto_commit', 0):
        conf.setdefault('isolation_level', None) # 设置autocommit
    if thread_protect:
        return ThreadUtil.LockingObjectCall(Conn(sqlite3.connect(database, **conf)))
    else:
        return Conn(sqlite3.connect(database, **conf))

