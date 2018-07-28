#coding=utf-8

_CONFIG_ = {}

class UserInfo:
    ''' '''
    def __init__(self):
        self.userid = ''
        self.username = ''
        #记录用户连接
        #连接ID，呃，实际上它等于user_id
        self.conn_id = None
        #conn_info = ('groupname','name')
        self.conn_group = None
        self.conn_ser   = None
        #table_list ={'tableid':1}
        self.table_list = []

def add_user(userid, username):

    id = str(userid)
    # 如果已经有该用户，则只更新他的用户名
    if _CONFIG_.has_key(id):
        _CONFIG_[id].username = username

    u = UserInfo()
    u.userid = id
    u.username = username
    _CONFIG_[ id ] = u

def renew_conn(userid, conn_group, conn_ser, conn_id):

    id = str(userid)
    if not _CONFIG_.has_key(id):
        add_user(id, '')
    _CONFIG_[id].conn_group = conn_group
    _CONFIG_[id].conn_ser   = conn_ser
    _CONFIG_[id].conn_id    = conn_id

def get(userid):
    ''' 用户Userinfo类的实例 '''
    ret = None
    id = str(userid)
    if _CONFIG_.has_key(id):
        ret = _CONFIG_[id]
    return ret

def set(userid, class_ins):
    ''' '''
    _CONFIG_[userid] = class_ins
