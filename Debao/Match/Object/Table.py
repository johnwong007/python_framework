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
    '''�����������ݽṹģ��'''
    def __init__(self):
        self.table_id        = ''     #����ID
        self.table_type      = ''     #��������
        self.name            = ''     #��������
        self.match_id        = 0      #����ID
        self.cash_id         = 0      #�ֽ�������ID
        self.desc            = ''     #��������    
        self.seat_num        = 0      #������λ��
        self.match_seat_num  = 0      #�����£�������λ��
        self.player_list     = {}     #�û��б� seat position => player object  
        self.game_addr       = ()     #�������ڵ���Ϸ����
        self.match_id        = 0      #��Ӧ������id

        self.bblind_pos      = None   # ��äλ��
        self.sblind_pos      = None   # Сäλ��
        self.button_pos      = None   # ׯ��λ��
        self.hands_cnt       = 0      # ���˼���
    
        self.player_ids      = {}     #���ID�ֵ� { userid : playerid }
        self.player_names    = {}     #���username�ֵ� { userid : username }
        self.player_seats    = {}     #���seat_pos�ֵ� { userid : seat_pos }
        self.player_hands    = {}     #��������� { userid : hand_num }
        self.player_rake     = {}     #��ұ���ˮ { userid : rake }
    
        self.player_out_list = {}     #����Ϊ0���û��б� seat position => player object
        self.player_alive_list = {}   #���벻Ϊ0���û��б� seat position => player object
        self.is_in_database = False   #�Ƿ����
        self.is_show        = 'YES'   #�Ƿ񹫿�
        self.pause_time     = None    #��ͣʱ�䣬ÿ����ͣ������£���¼���һ����ͣʱ��
        self.total_rest_time = 0  #�����ܹ���Ϣ�˶೤ʱ��

        self.zombie_players = {}      #��ʬ�û������ƾֽ���ǰ�뿪��

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
    '''���һ���������ݽṹ'''
    m = Table()
    m.table_id = str(table_id)
    m.name     = table_name
    m.seat_num = seat_num
    m.match_seat_num = match_seat_num
    _CONFIG_[str(table_id)] = m

    
def join_table(table_id, player):
    '''����û���table_id��ȥ'''
    pass


def choose_one_table(table_id, player):
    '''ѡ��һ�����ʵ�table����������û�'''
    pass


def choose_one_table(table_id, player):
    '''ѡ��һ�����ʵ�table����������û�'''
    pass


def get(table_id):
    '''��ȡ��������'''
    ret = None
    id = str(table_id)
    if _CONFIG_.has_key(id):
        ret = _CONFIG_[id]
    
    return ret

def get_all_table():
    '''��������������'''
    return _CONFIG_

@lockingCall(lock)
def remove(table_id):
    id = str(table_id)
    if _CONFIG_.has_key(id):
        del _CONFIG_[id]

def size():
    return len( _CONFIG_ )
