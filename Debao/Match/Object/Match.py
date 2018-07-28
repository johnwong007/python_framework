#coding=gbk
import time
import Db.Mysql
import zlog as logging
from . import Table as TableObject
from .. import Config

_CONFIG_ = {}

class Match:
    '''锦标赛规则数据结构模块'''
    def __init__(self):
        self.match_id  = 0              #赛事ID
        self.name      = ''             #赛事名
        self.desc      = ''             #赛事描述
        self.type      = ''             #赛事类型
        self.conf      = None           #赛事规则配置
        self.match_status    = 0        #赛事目前的状态  
        self.apply_is_end    = False    #是否可报名 True False
        self.table_list      = []       #赛事管理的桌 [tableid, tableid, ...]
        self.user_list       = []       #参赛用户列表
        self.user_conf       = {}       #赛事的用户作为映射   userid :  { 'username' : xxx, 'playerid' : xxx }
        self.last_blind_level= None     #赛事的上一次盲注等级
        self.blind_level     = None     #赛事的盲注等级
        self.player_ids      = {}       #玩家ID字典 { userid : playerid }
        self.player_hands    = {}       #玩家总手数 { userid : hands_num }
        self.uid_tableid     = {}       #玩家ID、table_id字典  {uid ：table_id}

        self.sq_create_table = 0        #创建赛桌的序列号，用于和游戏服务校对
        self.sq_join_table   = 0        #加入赛桌的序列号，用于和游戏服务校对
        self.sq_start_table  = 0        #赛桌开始的序列号，用于和游戏服务校对
        self.sq_regroup_table = 0       #赛桌重组的序列号，用于和游戏服务校对

        self.table_wait_for_sync = []   #等待同步规则、重组的牌桌

        self.start_time = 0             #开赛时间
        self.player_lose_list       = {}    #输家列表 uid => rank
        self.status_uptime          = time.time()      #赛事状态更新时间
        self.to_check_apply         = True   # 是否检查报名人数 true 是 false 否
        self.has_addon              = False  #是否已经addon
        self.destroying_table_num   = 0      #正在销毁过程中的牌桌

        self.delay_apply_user       = {}     #延迟登记进来的玩家 uid:userinfo
        self.no_sync_table_list     = []     #延迟登记创建的牌桌还没有同步规则 table_id

        self.level                  = ''     # 电竞用到   added by WangJian

        

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
            更新赛事状态
        '''
        self.status_uptime = time.time()
        self.match_status = status

    def get_blind_conf(self):
        '''
            取当前盲注信息
        '''
        ret = None
        t_now = time.time()
        
        # 同一场比赛中所有牌桌应该统一升盲
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
            取可用的座位数
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
            取现有牌桌里面，人数最少的牌桌ID及其人数
            返回：{'table_id' : table_id , 'player_count' : player_count}
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
            功能：返回排名
            编写：chend
            创建：2012-1-11 11:33:04
            修改：
        '''
        # 排名算法：赛事总人数 - 输家总人数
        rank = len(self.user_list) - len(self.player_lose_list)

        return rank

    def get_alive_player( self ):
        '''
            功能：返回有效玩家个数
            编写：chend
            创建：2012-1-11 11:55:31
            修改：
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
            延迟报名新创的牌桌是否可以发送同步规则
            user_num : 当前牌桌人数
        '''
        # 原来采用下面的算法控制牌桌发牌的时机
        # 后来发现有卡住的bug，情景大概是这样的：
        # A牌桌是延迟登记创建的，逐个安排玩家坐进来，但始终达不到发牌的条件
        # 可能是由于B牌桌内有一个玩家出局了导致再也没有玩家坐进A牌桌
        # 此时A牌桌永远不会被驱动，到了addon时间这场比赛永远会等待A牌桌的结束
        # 实际上A从来没有开始，这就形成了一个死锁
        return True

        # 原来的算法
        current_num = self.get_alive_player()
        logging.debug('delay_table_can_sync_rule: user_num=%s, current_num=%s, table_num=%s'
            %(user_num, current_num, len(self.table_list)))

        if user_num >= current_num / len(self.table_list):
            return True
        else:
            return False



def add_match(match_id, match_name, match_status, match_type, start_time, level = ''):
    '''添加一个赛事数据结构'''
    m = Match()
    m.match_id = str(match_id)
    m.name = match_name
    m.type = match_type
    m.match_status = match_status
    m.start_time = start_time
    m.level = level

    _CONFIG_[str(match_id)] = m
    

def get(match_id):
    '''获取赛事规则'''
    ret = None
    id = str(match_id)
    if _CONFIG_.has_key(id):
        ret = _CONFIG_[id]
    
    return ret

def get_all_match():
    '''返回现所有赛事'''
    return _CONFIG_

def get_all_match_id():
    '''获取现有的赛事ID列表'''
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
