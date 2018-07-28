#coding=gbk
"""
sqlite3�Ķ��η�װ
*���ο��ĵ���
    DBAPI-2.0˵����
        http://www.python.org/topics/database/DatabaseAPI-2.0.html
    sqlite3�Ĳ������÷���
        http://docs.pysqlite.googlecode.com/hg/sqlite3.html
*���������ӣ�
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
        """��ѯ�����������м�¼"""
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.fetchall()
        finally:
            cur.close()

    def queryOne(self, *args, **kwargs):
        """��ѯ�����ص��м�¼"""
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.fetchone()
        finally:
            cur.close()

    def execute(self, *args, **kwargs):
        """ִ�У����ر�Ӱ�������"""
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.rowcount
        finally:
            cur.close()

    def executeMany(self, *args, **kwargs):
        """ִ�У�many"""
        cur = self.conn.cursor()
        try:
            cur.executemany(*args, **kwargs)
        finally:
            cur.close()

    def insert(self, *args, **kwargs):
        """���룬�����������ֶε�ֵ��û�еĻ�����None"""
        cur = self.conn.cursor()
        try:
            cur.execute(*args, **kwargs)
            return cur.lastrowid
        finally:
            cur.close()

    def commit(self):
        """�ύ"""
        return self.conn.commit()

    def rollback(self):
        """�ع�"""
        return self.conn.rollback()

    def isAlive(self):
        """����Ƿ���"""
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
    """ʹ�����ӳ��������ݿ�"""
    dname = os.path.dirname(database)
    if dname and not os.path.isdir(dname):
        os.makedirs(dname, 0755)
    thread_protect = conf.pop('thread_protect', True) # �Ƿ�ʹ���̱߳���ģʽ
    conf.setdefault('check_same_thread', False) # Ĭ�ϲ�����Ƿ�ͬ�߳�
    conf.setdefault('timeout', 60) # Ĭ�ϵȴ�����ʱ��Ϊ60��
    if conf.pop('auto_commit', 0):
        conf.setdefault('isolation_level', None) # ����autocommit
    if thread_protect:
        return ThreadUtil.LockingObjectCall(Conn(sqlite3.connect(database, **conf)))
    else:
        return Conn(sqlite3.connect(database, **conf))

