#coding=gbk
import Db.Mysql
from .. import Match as MM

_CONFIG_ = {}
_INSTANCE_ = None

class Rule:
    '''锦标赛规则数据结构模块'''
    play_type           = ''
    seat_num            = ''    #每一桌多少人
    start_dtime         = ''    #开赛时间
    min_usernum         = ''    #开赛最少人数
    blind_type          = ''    #升盲规则种类
    init_chips          = ''    #初始用户筹码数
    wait_time           = 0     #每个用户说话时间
    pay_type            = ''    #货币类型
    apply_time          = ''    #报名时间
    apply_delay_time    = 0     #延迟报名时间 单位s
    bonus_ratio         = 0     #奖池比率，报名费用于奖池的比率
    inthemoney_ratio    = 0     #钱圈 能够拿到奖励的名次范围 前%多少
    hand_fee            = 0     #手续费
    pause               = 'NO'  #整点暂停？
    rebuy               = 'NO'  #是否是rebuy赛
    rebuy_times         = 0     #允许rebuy次数
    rebuy_blindlevel    = 0     #允许rebuy的最大盲注等级，高于此等级不能rebuy
    rebuy_value         = 0     #一次rebuy筹码量,默认为初始筹码
    rebuy_paytype       = ''    #rebuy币种，默认和赛事的pay_type相同
    rebuy_paymoney      = 0     #rebuy需要花的钱
    addon               = 'NO'  #是否是可以addon
    addon_value         = 0     #最终加码的数量
    addon_paymoney      = 0     #addon需支付的钱
    addon_wait_time     = 0     #addon等待时间
    valid_rebuy_time    = 0     #开赛后合法的rebuy时间
    is_allin            = 'NO'  #是否是ALL_IN赛
    target_gameaddr     = None  #创牌桌时指定的Game服务
    hunting_reward      = None  #猎人赛奖励
    match_addr          = []    #赛事服务地址

    @staticmethod
    def getInstance():
        global _INSTANCE_
        
        if not _INSTANCE_:
            _INSTANCE_ = Rule()
        return _INSTANCE_
    
    def __init__(self):
        self.blind_conf = {}

    
def load_rule(match_ids):
    '''加载赛事规则'''
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
        r.hand_fee          = i['hand_fee']         #手续费
        r.pause             = i['pause']            #整点暂停休息否
        r.rebuy             = i['rebuy']            #是否是rebuy赛
        r.rebuy_times       = i['rebuy_times']      #最大rebuy次数
        r.rebuy_blindlevel  = i['rebuy_blindlevel'] #允许rebuy的最大盲注等级
        r.rebuy_value       = i['rebuy_value']      #一次rebuy到的筹码，默认为初始筹码
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
        
        #这里加载盲注结构，同时计算开赛后合理的rebuy时间
        MM.load_bind_type(r)
        if r.rebuy == 'YES':
            MM.update_valid_rebuy_time(r.valid_rebuy_time, i['id'])

        _CONFIG_[i['id']] = r
    
def get(match_id):
    '''获取赛事规则'''
    ret = None
    id = int(match_id)
    if _CONFIG_.has_key(id):
        ret = _CONFIG_[id]
    
    return ret

def remove(match_id):
    id = int(match_id)
    if _CONFIG_.has_key(id):
        del _CONFIG_[id]

