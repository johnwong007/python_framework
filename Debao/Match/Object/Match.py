#coding=gbk
import time
import Db.Mysql
import zlog as logging
from . import Table as TableObject
from .. import Config

_CONFIG_ = {}

class Match:
    '''�������������ݽṹģ��'''
    def __init__(self):
        self.match_id  = 0              #����ID
        self.name      = ''             #������
        self.desc      = ''             #��������
        self.type      = ''             #��������
        self.conf      = None           #���¹�������
        self.match_status    = 0        #����Ŀǰ��״̬  
        self.apply_is_end    = False    #�Ƿ�ɱ��� True False
        self.table_list      = []       #���¹������ [tableid, tableid, ...]
        self.user_list       = []       #�����û��б�
        self.user_conf       = {}       #���µ��û���Ϊӳ��   userid :  { 'username' : xxx, 'playerid' : xxx }
        self.last_blind_level= None     #���µ���һ��äע�ȼ�
        self.blind_level     = None     #���µ�äע�ȼ�
        self.player_ids      = {}       #���ID�ֵ� { userid : playerid }
        self.player_hands    = {}       #��������� { userid : hands_num }
        self.uid_tableid     = {}       #���ID��table_id�ֵ�  {uid ��table_id}

        self.sq_create_table = 0        #�������������кţ����ں���Ϸ����У��
        self.sq_join_table   = 0        #�������������кţ����ں���Ϸ����У��
        self.sq_start_table  = 0        #������ʼ�����кţ����ں���Ϸ����У��
        self.sq_regroup_table = 0       #������������кţ����ں���Ϸ����У��

        self.table_wait_for_sync = []   #�ȴ�ͬ���������������

        self.start_time = 0             #����ʱ��
        self.player_lose_list       = {}    #����б� uid => rank
        self.status_uptime          = time.time()      #����״̬����ʱ��
        self.to_check_apply         = True   # �Ƿ��鱨������ true �� false ��
        self.has_addon              = False  #�Ƿ��Ѿ�addon
        self.destroying_table_num   = 0      #�������ٹ����е�����

        self.delay_apply_user       = {}     #�ӳٵǼǽ�������� uid:userinfo
        self.no_sync_table_list     = []     #�ӳٵǼǴ�����������û��ͬ������ table_id

        self.level                  = ''     # �羺�õ�   added by WangJian

        

    def register_table( self, table_id ):
        if self.table_list.count( table_id ) <= 0:
            self.table_list.append( table_id )
        return self

    def unregister_table( self, table_id ):
        if self.table_list.count( table_id ) > 0:
            self.table_list.remove( table_id )
        return self

    def get_status(self):
        return self.match_status

    def set_status(self, status):
        '''
            ��������״̬
        '''
        self.status_uptime = time.time()
        self.match_status = status

    def get_blind_conf(self):
        '''
            ȡ��ǰäע��Ϣ
        '''
        ret = None
        t_now = time.time()
        
        # ͬһ����������������Ӧ��ͳһ��ä
        t_pass = t_now - self.start_time
        blind_conf = self.conf.blind_conf
        time_list = blind_conf.keys()
        time_list.sort()
        for t in time_list:
            if t_pass > t :
                blind_info = blind_conf[t]
                self.last_blind_level = self.blind_level
                self.blind_level = blind_info[3]
                ret = blind_info
        return ret
    

    def get_usable_seat_num( self, ignore_table_id='' ):
        '''
            ȡ���õ���λ��
        '''
        usable_seat_num = 0
        for table_id in self.table_list:
            if ignore_table_id == table_id:
                continue
            table = TableObject.get( table_id )
            if not table:
                continue
            seat_num     = table.seat_num
            player_count = len( table.player_list )
            usable_seat_num += seat_num - player_count

        return usable_seat_num

    def get_min_player_table( self ):
        '''
            ȡ�����������棬�������ٵ�����ID��������
            ���أ�{'table_id' : table_id , 'player_count' : player_count}
        '''
        ret = None
        
        for table_id in self.table_list:
            table = TableObject.get( table_id )
            playercnt = len( table.player_list )
            
            if not ret or playercnt < ret['player_count']:
                ret = {
                'player_count' : playercnt,
                'table_id'     : table_id,
                }

        return ret
    
    def rank_player(self):
        '''
            ���ܣ���������
            ��д��chend
            ������2012-1-11 11:33:04
            �޸ģ�
        '''
        # �����㷨������������ - ���������
        rank = len(self.user_list) - len(self.player_lose_list)

        return rank

    def get_alive_player( self ):
        '''
            ���ܣ�������Ч��Ҹ���
            ��д��chend
            ������2012-1-11 11:55:31
            �޸ģ�
        '''
        
        return len(self.user_list) - len(self.player_lose_list)

    def get_status_pass_time( self ):
        return time.time() - self.status_uptime

    def add_player_info( self, user_id, player_id, hand_num=0 ):
        self.player_ids[ user_id ] = player_id
        self.player_hands[ user_id ] = hand_num

    def save_player_status( self, user_id, hand_num ):
        self.player_hands[ user_id ] += hand_num

    def record_delay_apply(self, user_id, username):
        if self.delay_apply_user.has_key(str(user_id)):
            return False
        else:
            self.delay_apply_user[str(user_id)] = username
            return True
            
    def remove_delay_apply(self, user_id):
        if self.delay_apply_user.has_key(str(user_id)):
            self.delay_apply_user.pop(str(user_id))

    def add_no_sync_table(self, table_id):
        if not table_id in self.no_sync_table_list:
            self.no_sync_table_list.append(table_id)

    def remove_no_sync_table(self, table_id):
        if table_id in self.no_sync_table_list:
            self.no_sync_table_list.remove(table_id)

    def delay_table_can_sync_rule(self, user_num):
        '''
            �ӳٱ����´��������Ƿ���Է���ͬ������
            user_num : ��ǰ��������
        '''
        # ԭ������������㷨�����������Ƶ�ʱ��
        # ���������п�ס��bug���龰����������ģ�
        # A�������ӳٵǼǴ����ģ���������������������ʼ�մﲻ�����Ƶ�����
        # ����������B��������һ����ҳ����˵�����Ҳû���������A����
        # ��ʱA������Զ���ᱻ����������addonʱ���ⳡ������Զ��ȴ�A�����Ľ���
        # ʵ����A����û�п�ʼ������γ���һ������
        return True

        # ԭ�����㷨
        current_num = self.get_alive_player()
        logging.debug('delay_table_can_sync_rule: user_num=%s, current_num=%s, table_num=%s'
            %(user_num, current_num, len(self.table_list)))

        if user_num >= current_num / len(self.table_list):
            return True
        else:
            return False



def add_match(match_id, match_name, match_status, match_type, start_time, level = ''):
    '''���һ���������ݽṹ'''
    m = Match()
    m.match_id = str(match_id)
    m.name = match_name
    m.type = match_type
    m.match_status = match_status
    m.start_time = start_time
    m.level = level

    _CONFIG_[str(match_id)] = m
    

def get(match_id):
    '''��ȡ���¹���'''
    ret = None
    id = str(match_id)
    if _CONFIG_.has_key(id):
        ret = _CONFIG_[id]
    
    return ret

def get_all_match():
    '''��������������'''
    return _CONFIG_

def get_all_match_id():
    '''��ȡ���е�����ID�б�'''
    return _CONFIG_.keys()

def has_key(match_id):
    id = str(match_id)
    return _CONFIG_.has_key(id)

def remove(match_id):
    id = str(match_id)
    if _CONFIG_.has_key(id):
        del _CONFIG_[id]

def size():
    return len( _CONFIG_ )
