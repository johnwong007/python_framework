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
    '''�ֽ����������ݽṹģ��'''
    def __init__(self):
        self.cash_status    = Config.STATUS_CASH_PREPARE     #����Ŀǰ��״̬����Ĭ��ֵ
        
        self.cash_id            = 0     #����ID
        self.config_name        = ''    #������
        self.seat_num           = 0     #��λ��
        self.min_buyin          = 0     #��С����
        self.max_buyin          = 0     #�������
        self.ante               = 0     #ǰע
        self.big_blind          = 0     #��äע
        self.small_blind        = 0     #Сäע
        self.new_blind          = 0     #����äע
        self.wait_time          = 0     #˼��ʱ��
        self.is_rebuy           = 0     #�Ƿ�����rebuy
        self.turn_bigblind      = 0     #�Ƿ��ѡ���ä����
        self.holdtime           = 0     #����ʱ��
        self.reentertime        = 0     #���½���ʱ�� �ڸ�ʱ�䷶Χ�����½�����Ҫ�����ϴδ���ĳ���
        self.min_tables         = 0     #��С��������
        self.max_tables         = 0     #�����������
        self.pay_type           = ''    #�������
        self.rule_type          = 0     #�ֽ���ʹ�õĹ������ͣ����ڼ����¹���
        self.target_gameaddr    = ''    #������ʱָ����Game����
        self.card_endtime       = ''    #���ſ�����ʱ��
        self.passwd             = ''    #��������
        self.owner              = ''    #�������� sys/user_id
        self.play_type          = "COMMON"  #Ĭ��Ϊ��ͨ BIDA�ش���
        self.level              = ''    #����PRIMARY/MIDDLE/HIGH
        self.service_fee_rate   = 0     #����ѱ���������������
        self.insstate           = '0'   #�Ƿ��б��չ���
        self.sub_table_type     = '0'
        self.card_compare_type     = '0'
        self.auto_blind         = '1'
        self.bott_pre_bbtimes   = '0'
        self.pk_first_bet       = '0'
        self.comsump_type       = 0     # ��������ʱ��������   0:  Ĭ��ֵ   1: ����   2: ����

        self.redu_chip_flag       = 0
        self.redu_chip_limit       = 0
        self.redu_chip_service_rate       = 0
        self.apply_buyin_open   = 0
        self.pt_pot_open        = 0
        
        self.rake_before_flop       = 0 #����ǰ��ˮ
        self.rake_ratio_after_flop  = 0 #���ƺ��ˮ����
        self.max_rake_after_flop    = 0 #���ƺ�����ˮ��

        self.table_list      = []     #���¹������ [tableid, tableid, ...]
        self.sq_create_table = 0      #�������������кţ����ں���Ϸ����У��
        self.sq_start_table  = 0      #������ʼ�����кţ����ں���Ϸ����У��


        # ����Ĳ����������δ֪
        self.user_list       = []     #�����û��б�
        
        self.sq_join_table   = 0      #�������������кţ����ں���Ϸ����У��
        
        self.sq_regroup_table = 0     #������������кţ����ں���Ϸ����У��

        self.table_wait_for_sync = [] #�ȴ�ͬ���������������


    def register_table( self, table_id ):
        if self.table_list.count( table_id ) <= 0:
            self.table_list.append( table_id )
        return self

        
@lockingCall(lock)
def add_cash(cash_id, config_name, cash_obj = None):
    '''���һ���ֽ������ݽṹ'''
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
    '''��ȡ�ֽ�������'''
    ret = None
    id = str(cash_id)
    if _CONFIG_.has_key(id):
        ret = _CONFIG_[id]
    
    return ret

def get_all_cash():
    '''�����������ֽ�������'''
    return _CONFIG_

def get_all_cash_id():
    '''��ȡ���е��ֽ�������ID�б�'''
    return _CONFIG_.keys()

def has_key(cash_id):
    id = str(cash_id)
    return _CONFIG_.has_key(id)

def size():
    return len( _CONFIG_ )
