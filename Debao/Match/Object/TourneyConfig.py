#coding=gbk
import Db.Mysql
from .. import Match as MM

_CONFIG_ = {}
_INSTANCE_ = None

class Rule:
    '''�������������ݽṹģ��'''
    play_type           = ''
    seat_num            = ''    #ÿһ��������
    start_dtime         = ''    #����ʱ��
    min_usernum         = ''    #������������
    blind_type          = ''    #��ä��������
    init_chips          = ''    #��ʼ�û�������
    wait_time           = 0     #ÿ���û�˵��ʱ��
    pay_type            = ''    #��������
    apply_time          = ''    #����ʱ��
    apply_delay_time    = 0     #�ӳٱ���ʱ�� ��λs
    bonus_ratio         = 0     #���ر��ʣ����������ڽ��صı���
    inthemoney_ratio    = 0     #ǮȦ �ܹ��õ����������η�Χ ǰ%����
    hand_fee            = 0     #������
    pause               = 'NO'  #������ͣ��
    rebuy               = 'NO'  #�Ƿ���rebuy��
    rebuy_times         = 0     #����rebuy����
    rebuy_blindlevel    = 0     #����rebuy�����äע�ȼ������ڴ˵ȼ�����rebuy
    rebuy_value         = 0     #һ��rebuy������,Ĭ��Ϊ��ʼ����
    rebuy_paytype       = ''    #rebuy���֣�Ĭ�Ϻ����µ�pay_type��ͬ
    rebuy_paymoney      = 0     #rebuy��Ҫ����Ǯ
    addon               = 'NO'  #�Ƿ��ǿ���addon
    addon_value         = 0     #���ռ��������
    addon_paymoney      = 0     #addon��֧����Ǯ
    addon_wait_time     = 0     #addon�ȴ�ʱ��
    valid_rebuy_time    = 0     #������Ϸ���rebuyʱ��
    is_allin            = 'NO'  #�Ƿ���ALL_IN��
    target_gameaddr     = None  #������ʱָ����Game����
    hunting_reward      = None  #����������
    match_addr          = []    #���·����ַ

    @staticmethod
    def getInstance():
        global _INSTANCE_
        
        if not _INSTANCE_:
            _INSTANCE_ = Rule()
        return _INSTANCE_
    
    def __init__(self):
        self.blind_conf = {}

    
def load_rule(match_ids):
    '''�������¹���'''
    sql = '''
        select f_id id,
               f_play_type play_type,
               f_blind_type blind_type,
               f_seat_num seat_num,
               f_init_chips init_chips,
               f_waittime waittime,
               f_plan_starttime plan_starttime,
               f_min_player min_player,
               f_max_player max_player,
               f_match_addr match_addr,
               f_game_addr game_addr,
               f_isback isback,
               f_pay_type pay_type,
               f_apply_time apply_time,
               f_apply_delay_time apply_delay_time,
               f_bonus_ratio bonus_ratio,
               f_inthemoney_ratio inthemoney_ratio,
               f_hand_fee hand_fee,
               f_pause pause,
               f_rebuy rebuy,
               f_rebuy_times rebuy_times, 
               f_legal_rebuy_level rebuy_blindlevel,
               f_rebuy_value rebuy_value,
               f_rebuy_paytype rebuy_paytype,
               f_rebuy_paymoney rebuy_paymoney,
               f_addon addon,
               f_addon_value addon_value,
               f_addon_paymoney addon_paymoney,
               f_addon_wait_time addon_wait_time,
               f_all_in is_allin,
               f_target_gameaddr target_gameaddr,
               f_hunting_reward hunting_reward
          from t_match where f_id in (%s)
    '''
    sql = sql % ', '.join(['%s']*len(match_ids))
    
    ret = Db.Mysql.connect('esun_texas').query(sql, match_ids)
    
    for i in ret:
        r = Rule()
        r.play_type         = i['play_type']
        r.seat_num          = i['seat_num']
        r.start_dtime       = i['plan_starttime']
        r.min_usernum       = i['min_player']
        r.blind_type        = i['blind_type']
        r.init_chips        = i['init_chips']
        r.wait_time         = i['waittime']
        r.pay_type          = i['pay_type']
        r.apply_time        = str(i['apply_time'])
        r.apply_delay_time  = int(i['apply_delay_time'])
        r.bonus_ratio       = i['bonus_ratio']
        r.inthemoney_ratio  = i['inthemoney_ratio']
        r.hand_fee          = i['hand_fee']         #������
        r.pause             = i['pause']            #������ͣ��Ϣ��
        r.rebuy             = i['rebuy']            #�Ƿ���rebuy��
        r.rebuy_times       = i['rebuy_times']      #���rebuy����
        r.rebuy_blindlevel  = i['rebuy_blindlevel'] #����rebuy�����äע�ȼ�
        r.rebuy_value       = i['rebuy_value']      #һ��rebuy���ĳ��룬Ĭ��Ϊ��ʼ����
        r.rebuy_paytype     = i['rebuy_paytype']
        r.rebuy_paymoney    = i['rebuy_paymoney']
        r.addon             = i['addon']
        r.addon_value       = i['addon_value']
        r.addon_paymoney    = i['addon_paymoney']
        r.addon_wait_time   = i['addon_wait_time']
        r.is_allin          = i['is_allin']
        r.target_gameaddr   = i['target_gameaddr']  
        r.hunting_reward    = i['hunting_reward']
        r.match_addr        = eval(i['match_addr'])      
        
        #�������äע�ṹ��ͬʱ���㿪��������rebuyʱ��
        MM.load_bind_type(r)
        if r.rebuy == 'YES':
            MM.update_valid_rebuy_time(r.valid_rebuy_time, i['id'])

        _CONFIG_[i['id']] = r
    
def get(match_id):
    '''��ȡ���¹���'''
    ret = None
    id = int(match_id)
    if _CONFIG_.has_key(id):
        ret = _CONFIG_[id]
    
    return ret

def remove(match_id):
    id = int(match_id)
    if _CONFIG_.has_key(id):
        del _CONFIG_[id]

