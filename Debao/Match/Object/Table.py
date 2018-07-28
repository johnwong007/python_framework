#coding=gbk

import Db.Mysql
import threading

def lockingCall(lock):
    def decoFunc(f):
        def callFunc(*args, **kwargs):
            lock.acquire()
            try:
                return f(*args, **kwargs)
            finally:
                lock.release()
        return callFunc
    return decoFunc

lock = None
if not lock:
    lock = threading.Lock()


_CONFIG_ = {}

class Table:
    '''赛桌详情数据结构模块'''
    def __init__(self):
        self.table_id        = ''     #牌桌ID
        self.table_type      = ''     #牌桌类型
        self.name            = ''     #牌桌名称
        self.match_id        = 0      #赛事ID
        self.cash_id         = 0      #现金赛配置ID
        self.desc            = ''     #牌桌描述    
        self.seat_num        = 0      #牌桌座位数
        self.match_seat_num  = 0      #（赛事）牌桌座位数
        self.player_list     = {}     #用户列表 seat position => player object  
        self.game_addr       = ()     #赛桌所在的游戏服务
        self.match_id        = 0      #对应的赛事id

        self.bblind_pos      = None   # 大盲位置
        self.sblind_pos      = None   # 小盲位置
        self.button_pos      = None   # 庄家位置
        self.hands_cnt       = 0      # 打了几手
    
        self.player_ids      = {}     #玩家ID字典 { userid : playerid }
        self.player_names    = {}     #玩家username字典 { userid : username }
        self.player_seats    = {}     #玩家seat_pos字典 { userid : seat_pos }
        self.player_hands    = {}     #玩家总手数 { userid : hand_num }
        self.player_rake     = {}     #玩家被抽水 { userid : rake }
    
        self.player_out_list = {}     #筹码为0的用户列表 seat position => player object
        self.player_alive_list = {}   #筹码不为0的用户列表 seat position => player object
        self.is_in_database = False   #是否入库
        self.is_show        = 'YES'   #是否公开
        self.pause_time     = None    #暂停时间，每次暂停都会更新，记录最近一次暂停时间
        self.total_rest_time = 0  #牌桌总共休息了多长时间

        self.zombie_players = {}      #僵尸用户（在牌局结束前离开）

    def add_player( self, player, seat_pos, player_id, user_id, user_name, hand_num=0, rake=0 ):

        self.player_list[ int(seat_pos) ]   = player
        self.player_ids[ user_id ]          = player_id
        self.player_names[ user_id ]        = user_name
        self.player_seats[ user_id ]        = int(seat_pos)
        self.player_hands[ user_id ]        = hand_num
        self.player_rake[ user_id ]         = rake

    def del_player( self, seat_pos, user_id ):
        
        del self.player_list[ int(seat_pos) ]
        del self.player_ids[ user_id ]
        del self.player_names[ user_id ]
        del self.player_seats[ user_id ]
        del self.player_hands[ user_id ]
        del self.player_rake[ user_id ]

    def save_player_status( self, user_id, hand_num, rake ):
        self.player_hands[ user_id ] += hand_num
        self.player_rake[ user_id ] += rake

    def add_zombie_player( self, player_id, user_id, user_name, chips, hand_num, rake ):
        
        self.zombie_players[ user_id ] = {}
        self.zombie_players[ user_id ][ 'player_id' ] = player_id
        self.zombie_players[ user_id ][ 'user_name' ] = user_name
        self.zombie_players[ user_id ][ 'chips' ]     = chips
        self.zombie_players[ user_id ][ 'hand_num' ]  = hand_num
        self.zombie_players[ user_id ][ 'rake' ]      = rake

    def del_zombie_player( self, user_id ):
        
        if self.zombie_players.has_key( user_id ):
            del self.zombie_players[ user_id ]

def add_table(table_id, table_name, seat_num, match_seat_num=0):
    '''添加一个牌桌数据结构'''
    m = Table()
    m.table_id = str(table_id)
    m.name     = table_name
    m.seat_num = seat_num
    m.match_seat_num = match_seat_num
    _CONFIG_[str(table_id)] = m

    
def join_table(table_id, player):
    '''添加用户到table_id中去'''
    pass


def choose_one_table(table_id, player):
    '''选择一个合适的table，用来添加用户'''
    pass


def choose_one_table(table_id, player):
    '''选择一个合适的table，用来添加用户'''
    pass


def get(table_id):
    '''获取牌桌详情'''
    ret = None
    id = str(table_id)
    if _CONFIG_.has_key(id):
        ret = _CONFIG_[id]
    
    return ret

def get_all_table():
    '''返回现所有赛桌'''
    return _CONFIG_

@lockingCall(lock)
def remove(table_id):
    id = str(table_id)
    if _CONFIG_.has_key(id):
        del _CONFIG_[id]

def size():
    return len( _CONFIG_ )
