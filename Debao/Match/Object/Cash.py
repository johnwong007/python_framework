#coding=gbk
import time
import Db.Mysql
import threading
from .. import Config

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

class Cash:
    '''现金赛规则数据结构模块'''
    def __init__(self):
        self.cash_status    = Config.STATUS_CASH_PREPARE     #赛事目前的状态，有默认值
        
        self.cash_id            = 0     #配置ID
        self.config_name        = ''    #配置名
        self.seat_num           = 0     #座位数
        self.min_buyin          = 0     #最小买入
        self.max_buyin          = 0     #最大买入
        self.ante               = 0     #前注
        self.big_blind          = 0     #大盲注
        self.small_blind        = 0     #小盲注
        self.new_blind          = 0     #新手盲注
        self.wait_time          = 0     #思考时间
        self.is_rebuy           = 0     #是否允许rebuy
        self.turn_bigblind      = 0     #是否可选择大盲参赛
        self.holdtime           = 0     #留坐时间
        self.reentertime        = 0     #重新进入时间 在该时间范围内重新进入需要带入上次带离的筹码
        self.min_tables         = 0     #最小桌子数量
        self.max_tables         = 0     #最大桌子数量
        self.pay_type           = ''    #金币类型
        self.rule_type          = 0     #现金桌使用的规则类型（现在加了新规则）
        self.target_gameaddr    = ''    #创牌桌时指定的Game服务
        self.card_endtime       = ''    #开放卡过期时间
        self.passwd             = ''    #房间密码
        self.owner              = ''    #房间属主 sys/user_id
        self.play_type          = "COMMON"  #默认为普通 BIDA必打桌
        self.level              = ''    #级别PRIMARY/MIDDLE/HIGH
        self.service_fee_rate   = 0     #服务费比例，按总买入算
        self.insstate           = '0'   #是否有保险功能
        self.sub_table_type     = '0'
        self.card_compare_type     = '0'
        self.auto_blind         = '1'
        self.bott_pre_bbtimes   = '0'
        self.pk_first_bet       = '0'
        self.comsump_type       = 0     # 创建牌桌时消耗类型   0:  默认值   1: 房卡   2: 货币

        self.redu_chip_flag       = 0
        self.redu_chip_limit       = 0
        self.redu_chip_service_rate       = 0
        self.apply_buyin_open   = 0
        self.pt_pot_open        = 0
        
        self.rake_before_flop       = 0 #翻牌前抽水
        self.rake_ratio_after_flop  = 0 #翻牌后抽水比例
        self.max_rake_after_flop    = 0 #翻牌后最大抽水数

        self.table_list      = []     #赛事管理的桌 [tableid, tableid, ...]
        self.sq_create_table = 0      #创建赛桌的序列号，用于和游戏服务校对
        self.sq_start_table  = 0      #赛桌开始的序列号，用于和游戏服务校对


        # 下面的参数可用与否，未知
        self.user_list       = []     #参赛用户列表
        
        self.sq_join_table   = 0      #加入赛桌的序列号，用于和游戏服务校对
        
        self.sq_regroup_table = 0     #赛桌重组的序列号，用于和游戏服务校对

        self.table_wait_for_sync = [] #等待同步规则、重组的牌桌


    def register_table( self, table_id ):
        if self.table_list.count( table_id ) <= 0:
            self.table_list.append( table_id )
        return self

        
@lockingCall(lock)
def add_cash(cash_id, config_name, cash_obj = None):
    '''添加一个现金赛数据结构'''
    if not cash_obj:
        C = Cash()
        C.cash_id      = cash_id
        C.config_name  = config_name
        _CONFIG_[str(cash_id)] = C
    else:
        _CONFIG_[str(cash_id)] = cash_obj

@lockingCall(lock)        
def del_cash(cash_id):
    ''''''
    try:
        if _CONFIG_.has_key(str(cash_id)):
            del _CONFIG_[str(cash_id)]
    except:
        return False
    return True
    

def get(cash_id):
    '''获取现金赛配置'''
    ret = None
    id = str(cash_id)
    if _CONFIG_.has_key(id):
        ret = _CONFIG_[id]
    
    return ret

def get_all_cash():
    '''返回现所有现金赛配置'''
    return _CONFIG_

def get_all_cash_id():
    '''获取现有的现金赛配置ID列表'''
    return _CONFIG_.keys()

def has_key(cash_id):
    id = str(cash_id)
    return _CONFIG_.has_key(id)

def size():
    return len( _CONFIG_ )
