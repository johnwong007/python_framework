import os
import time
import pymssql

import XmlConfig

def rowUpper(cur, row):
    # row factory: dict with upper key
    pos = range(len(cur.description))
    return dict([(cur.description[i][0].upper(), row[i]) for i in pos])

def rowLower(cur, row):
    # row factory: dict with lower key
    pos = range(len(cur.description))
    return dict([(cur.description[i][0].lower(), row[i]) for i in pos])

def rowTuple(cur, row):
    # row factory: tuple
    return row


class SqlServer:

    def __init__(self, conf):
        self.conf = conf
        self.setRowFactory('upper')
        self.conn = pymssql.connect(**self.conf)

    def setRowFactory(self, type):
        if type == 'upper':
            self._rowFactory = rowUpper
        elif type == 'lower':
            self._rowFactory = rowLower
        else:
            self._rowFactory = rowTuple

    def close(self):
        try:
            self.conn.close()
        except:
            pass
        self.conn = None

    def query(self, sql, args=()):
        cur = self.conn.cursor()
        try:
            cur.execute(sql, args)
            return self.fetchAll_(cur)
        finally:
            cur.close()

    def execute(self, sql, args=()):
        cur = self.conn.cursor()
        try:
            return cur.execute(sql, args)
        finally:
            cur.close()

    def executemany(self, sql, args):
        cur = self.conn.cursor()
        try:
            return cur.executemany(sql, args)
        finally:
            cur.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def fetchAll_(self, cur):
        ret = []
        for row in cur.fetchall():
            ret.append(self._rowFactory(cur, row))
        return ret


############################################################


_SQLSERVER_DBS_ = {}

def get(id, conf=None):
    if not _SQLSERVER_DBS_.has_key(id):
        if not conf:
            conf = XmlConfig.get('/db/sqlserver/' + id)
        _SQLSERVER_DBS_[id] = SqlServer(conf)
    return _SQLSERVER_DBS_[id]

def release():
    for id in _SQLSERVER_DBS_:
        _SQLSERVER_DBS_[id].close()

import atexit
atexit.register(release)

