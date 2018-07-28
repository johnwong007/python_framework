#coding=utf-8

import time
import math
import zlog as logging

from . import Table as TableObject
from . import Match as MatchObject

from .. import Protocol as P
from .. import Message as Message


'''
    进入暂停状态的赛事对象字典
    {match_id : match_obj, ...}
'''
_PAUSE_MATCH_DICT_ = {}

'''
    table_dict 结构：
    
    {
        table_id : {
                        ADDON_FLAG : FALSE,
                        PAUSE_FLAG : FALSE,     #当两个标志位都为False的时候，可以继续比赛
                    },
        ...
    }
'''




class PauseMatch:
    '''
        所有处于暂停状态的比赛：
            PAUSE: 到达整点前5分钟的暂停休息
            ADDON：最终加码时段的暂停
    '''
    def __init__(self, match_id):
        self.match_id           = match_id
        self.pause_table_num    = 0             #处于暂停状态的牌桌数
        self.table_dict         = {}            #
        self.can_run            = False         #能否开赛标志位
        
        self.real_start_addon   = False         #是否触发了addon
        self.addon_table_num    = 0             #处于addon状态的牌桌数
        self.addon_start_time   = 0             #本场比赛addon开始时间戳
        self.addon_wait_time    = 0             #addon等待时间

        self.hbh_flag           = False         #hands-by-hands标志
        self.hbh_table_num      = 0             #处于hbh状态的牌桌数
            
    def add_pause_table(self, table_id, reason):
        '''
            增加一个暂停的牌桌
            reason: 触发的原因： PAUSE_FLAG/ADDON_FLAG
            
        '''
        table = TableObject.get( table_id )
        if not table:
            logging.error('from add_pause_table: not exist table[%s]'%table_id)
            return 
        
        #给先进来的牌桌补签标志位
        self.supply_table_flag(reason)
            
        logging.info('before add_table : %s, reason[%s]'%(self.table_dict, reason))    
        if self.table_dict.has_key(table_id):
            self.table_dict[table_id][reason] = True
        else:
            flag_info = {}
            #初始化数据结构
            flag_info['PAUSE_FLAG'] = False
            flag_info['ADDON_FLAG'] = False 
            flag_info['HBH_FLAG']   = False 

            self.table_dict[table_id] = flag_info
            table.pause_time = time.time()              #记录暂停开始时间
            
            #置标志位
            self.table_dict[table_id][reason] = True
            self.pause_table_count(reason)
            
        logging.info('after add_table : %s, reason[%s]'%(self.table_dict, reason))
        #更新总牌桌数量
        self.pause_table_num = len(self.table_dict)


    def pause_table_count(self, reason):
        ''''''
        if reason == 'ADDON_FLAG':
            self.addon_table_num += 1
        elif reason == 'HBH_FLAG':
            self.hbh_table_num += 1


    def clear_table_flag(self, table_id, reason):
        '''清标志位'''
        logging.info('---------------->IN clear_table_flag')
        if self.table_dict.has_key(table_id):
            self.table_dict[table_id][reason] = False
            return True
        else:
            return False
            
    def supply_table_flag(self, reason):
        '''补签标志位'''
        table_id_list = self.table_dict.keys()
        for i in table_id_list:
            if not self.table_dict[i][reason]: 
                self.table_dict[i][reason] = True
                self.pause_table_count(reason)

        logging.info('supply_table_flag for tables: %s'%table_id_list)
            
            
    def check_all_flag(self):
        ''''''
        # logging.debug('table_dict----->%s'%self.table_dict)
        table_id_list = self.table_dict.keys()
        for i in table_id_list:
            #有任何一个标志位为True，退出
            if self.table_dict[i]['PAUSE_FLAG'] or self.table_dict[i]['ADDON_FLAG'] \
                or self.table_dict[i]['HBH_FLAG']:
                return
        #所有牌桌的标志为都是False,可以继续打牌了
        self.can_run = True
    
      
    def check_real_addon(self):
        '''检查该场比赛是否可以正式addon了'''
        match = MatchObject.get(self.match_id)
        if match == None:
            logging.error('not existmatch_id[%s]'%(match_id))
            return 
        
        total_table_num = len(match.table_list) - match.destroying_table_num
        logging.info('check_real_addon match[%s] total_table_num = %s'
                                        %(self.match_id, total_table_num))
        if self.addon_table_num >= total_table_num:
            return True
        else:
            return False
            
    def update_pause_starttime(self):
        '''
            更新各牌桌的暂停起始时间，以便统一盲注
        '''
        tid_list = self.table_dict.keys()                           #取所有的牌桌id
        
        for id in tid_list:
            table = TableObject.get( id )
            if not table:
                logging.error('from update_pause_starttime: not exist table[%s]'%table_id)
                continue
            
            table.pause_time = self.addon_start_time                #统一暂停开始时间
            
        
################################################################################

def get_pause_match(match_id):
    '''取一个对象'''
    global _PAUSE_MATCH_DICT_
    
    if _PAUSE_MATCH_DICT_.has_key(match_id):
        return _PAUSE_MATCH_DICT_[match_id]
    else:
        return None
        
def add_pause_match(match_id, pause_obj):
    '''增加一个对象'''
    global _PAUSE_MATCH_DICT_
    if _PAUSE_MATCH_DICT_.has_key(match_id):
        return
    
    _PAUSE_MATCH_DICT_[match_id] = pause_obj
    return True
    
def del_pause_match(match_id):
    '''del'''
    global _PAUSE_MATCH_DICT_
    if _PAUSE_MATCH_DICT_.has_key(match_id):
        del _PAUSE_MATCH_DICT_[match_id]
        logging.info('del pause_match[%s] from _PAUSE_MATCH_DICT_'%match_id)
        return True
    else:
        logging.error('from del_pause_match: no pause_match[%s] in _PAUSE_MATCH_DICT_'%match_id)
        return False
        
def get_pause_list():
    ''''''
    global _PAUSE_MATCH_DICT_
    
    match_list = _PAUSE_MATCH_DICT_.keys()
    return match_list
    
    
def is_time_to_pause(): 
    '''
        判断当前时间是否为休息时间段
        默认休息时间段：55分--00（整点）
    '''
    try:
        current_minute = time.strftime("%M", time.localtime())
        #取当前时间的分钟数 如15:30:42  分钟数为30
        current_minute = int(current_minute)
        if current_minute >= 55:
        #if (current_minute % 10) >= 8:
            return True
        else:
            return False
    except:
        logging.error('Some error: is_time_to_pause------>%s'%(traceback.format_exc()))

    
    
def need_pause(match):
    '''
        判断该牌桌是否需要暂停休息
        入参：match对象
        出参：True/False
        编写：liulk
        日期：2012.09.06  14:21
    '''
    try:
        #首先判断牌桌配置
        if match.conf.pause == 'YES':
            logging.info('match [%s] is setted need pause!'%match.match_id)
            #再判断是否到休息时间段
            if is_time_to_pause():
                logging.info('It is time to rest 5 minutes!')
                return True
            else:
                return False
        logging.debug('match [%s] is setted no need to pause'%match.match_id)
        return False
    except:
        logging.error('Some error: need_pause------>%s'%(traceback.format_exc()))

def judge_qianquan_user(match):
    '''
        比较钱圈人数，当前人数
        进入钱圈后不能rebuy、addon
        入参：
        出参：True/False    True:可以rebuy/addon  False:不可以
        编写：liulk
        日期：2012.11.08  13:52
    '''
    if not match:
        logging.info('JUDGE: match----> %s'%match)
        return False
    #取钱圈比率,钱圈比为0比赛为实物奖励，奖池变动无影响
    inthemoney_ratio = match.conf.inthemoney_ratio
    #logging.info('match[%s] inthemoney_ratio = %s'%(match.match_id, inthemoney_ratio))
    if inthemoney_ratio == 0:
        return True
        
    #总人数
    total_users = len(match.user_list)
    #钱圈人数
    inthemoney_num = int(total_users * inthemoney_ratio / 100)
    #当前剩余玩家数目 = 总数 - 已经淘汰的
    alive_user_num = total_users - len(match.player_lose_list)
    #logging.info('total_users[%s], inthemoney_num[%s], alive_user_num[%s]'
                    #%(total_users, inthemoney_num, alive_user_num))
    
    if alive_user_num <= inthemoney_num:
        return False
    else:
        return True
        

def need_addon(match, player_count):
    '''
        判断是否到addon时间
        入参：match对象， table对象
        出参：True/False
        编写：liulk
        日期：2012.10.29  10:37
    '''
    try:
        #配置为可以addon的赛事，且没有addon过的才可以addon,最后一个人的时候不触发addon
        if match.conf.addon == 'YES' and match.has_addon == False and player_count > 1:
            #判断到达钱圈人数没有，如到达不能addon
            ret = judge_qianquan_user(match)

            # 防止有牌桌已经在这之前进入等候addon的状态，导致比赛卡住的bug
            if not ret:
                if get_pause_match(match.match_id):
                    logging.info('need_addon: already in qianquan, but some tables are in _PAUSE_MATCH_DICT_')
                else:
                    logging.debug('from need_addon: IN qianquan no addon! match[%s]'%match.match_id)
                    return False
            
            #判断是否到达相应的盲注级别
            blind_conf = match.get_blind_conf()
            next_blindlevel = int(blind_conf[3])
            #要升盲了，升盲前最终加码的机会到了。。
            if next_blindlevel > match.conf.rebuy_blindlevel:
                logging.info('match[%s] : time to addon!'%match.match_id)
                return True
            else:
                return False
        #logging.info('match[%s] : not setted addon!'%match.match_id)
        return False
    except:
        logging.error('Some error: need_addon---->%s'%(traceback.format_exc()))
        return False

def need_hbh(match):
    '''
        hands-by-hands
        1. 当前人数 == final-talbe人数 + 1
        2. 钱圈人数 +1 == 当前人数 
    '''
    try:
        # 如果本场比赛已经有牌桌进入了hands-by-hands状态，那么后续的所有牌桌都
        # 应该进入该状态，然后统一解除状态
        pause_match = get_pause_match(match.match_id)
        if pause_match and pause_match.hbh_flag:
            return True


        alive_num = match.get_alive_player()
        
        # 第一种情况：final-table
        if alive_num == match.conf.seat_num + 1:
            logging.debug("match[%s] final-table hands-by-hands!"%match.match_id)
            return True

        # 第二种情况：钱圈人数
        inthemoney_num = match.conf.inthemoney_ratio/100.0 * len(match.user_list)
        if inthemoney_num == 0 or inthemoney_num <= match.conf.seat_num:
            return False

        # total_table_num = len(match.table_list) - match.destroying_table_num
        
        # 找到能容纳钱圈人数的最小桌子数
        # for i in range(1, alive_num):
        #     if i*match.conf.seat_num >= inthemoney_num:
        #         break
        # usable_seat_num = i*match.conf.seat_num         


        # if inthemoney_num < alive_num and alive_num <= usable_seat_num and total_table_num > 1:
        #     logging.debug("match[%s] QianQuan hands-by-hands! inthemoney_num=%s, alive_num=%s, usable_seat_num=%s"
        #                 %( match.match_id, inthemoney_num, alive_num, usable_seat_num))
        #     return True

        if math.floor(inthemoney_num) + 1 == alive_num:
            logging.debug("match[%s] QianQuan hands-by-hands! inthemoney_num=%s, alive_num=%s, inthemoney_ratio=%s"
                        %( match.match_id, inthemoney_num, alive_num, match.conf.inthemoney_ratio))
            return True


        return False
    except:
        logging.error("some error in need_hbh: %s"%(traceback.format_exc()))
        return False

    
def time_to_pause(match, player_count):
    '''判断是否到了暂停时间或者addon时间'''
    result = []
    
    if need_pause(match):
        result.append('PAUSE')
        
    if need_addon(match, player_count):
        result.append('ADDON')
        
    if need_hbh(match):
        result.append('HBH')

    return result
    
    
def check_pause_flag(match_list):
    '''
        检查所有处于暂停状态的桌子
        已经到达整点，恢复标志位
    '''
    for match_id in match_list:
        pause_match = get_pause_match(match_id)
        if not pause_match:
            logging.error('from check_pause_flag: not exist match_id[%s]'%match_id)
            return
            
        #没有桌子处于整点暂停状态，忽略
        # if pause_match.time_pause == False:
            # continue
        
        for table_id in pause_match.table_dict.keys():
            pause_match.table_dict[table_id]['PAUSE_FLAG'] = False
        
        #清整点暂停标志位，表示已经过了整点暂停了
        #pause_match.time_pause = False
        
        
def check_addon_flag(match_list):
    '''
        检查处于addon状态的比赛
        addon时间结束就恢复标记位
    '''
    for match_id in match_list:
        pause_match = get_pause_match(match_id)
        if not pause_match:
            logging.error('from check_addon_flag: not exist match_id[%s]'%match_id)
            return

        #只有真正触发了addon才继续check
        if pause_match.real_start_addon:
            #addon等待时间是否到达
            pass_time = time.time() - pause_match.addon_start_time 
            #等待时间已到，所有牌桌恢复标志位
            if pass_time >= pause_match.addon_wait_time:
                for table_id in pause_match.table_dict.keys():
                    pause_match.table_dict[table_id]['ADDON_FLAG'] = False
                    logging.info('check_addon_flag set flag = False, table[%s]'%table_id)
                
            
def check_hbh_flag(match_list):
    '''
        检查处于hbh状态的比赛
    '''
    for match_id in match_list:
        pause_match = get_pause_match(match_id)
        if not pause_match:
            logging.error('from check_hbh_flag: not exist match_id[%s]'%match_id)
            continue
        if not pause_match.hbh_flag:
            continue

        match = MatchObject.get(match_id)
        total_table_num = len(match.table_list) - match.destroying_table_num

        #修复延迟登记导致的比赛卡死
        #计算牌桌数量时将新创建的还未发送同步规则的牌桌也算进去
        if pause_match.hbh_table_num + len(match.no_sync_table_list) >= total_table_num:
            for table_id in pause_match.table_dict.keys():
                pause_match.table_dict[table_id]['HBH_FLAG'] = False


def check_match_canrun(match_list):
    '''检查 can_run标志'''
    for match_id in match_list:
        pause_match = get_pause_match(match_id)
        if not pause_match:
            logging.error('from check_match_canrun: not exist match_id[%s]'%match_id)
            continue
            
        pause_match.check_all_flag()
        
        
def deal_pause_table():
    '''
        处理处于暂停状态的牌桌：PAUSE/ADDON/HBH
        编写：liulk
        日期：2012.11.16  13:40
        修改：2014-07-24  11:27 加入hands-by-hands机制
    '''
    match_list = get_pause_list()
    #logging.info('in deal_pause_table PAUSE_MATCH_LIST------->%s'%match_list)
    if len(match_list) == 0:
        return
    
    #1. 恢复整点暂停牌桌标志位
    if not is_time_to_pause():
        check_pause_flag(match_list)
        
    #2. 恢复addon暂停标志位
    check_addon_flag(match_list)

    #3. 结束hbh状态
    check_hbh_flag(match_list)
    
    #4. 恢复比赛（两个标志位都为False）
    for m in match_list:
        pause_match = get_pause_match(m)
        logging.debug("in deal_pause_table------>Pause match info: mid=%s, table_dict=%s"%(m, pause_match.table_dict))
    check_match_canrun(match_list)
    

def check_addon_pause(match, match_id, table_id):
    '''
        销毁一个牌桌时检查该场比赛是否符合addon/pause 状态
        日期: 2013-01-03 14:25
        作者：刘立坤
        目的：修复addon牌桌卡死的bug
    '''
    pause_match = get_pause_match(match_id)
    
    #该场比赛没有处于等待addon/pause 状态
    if pause_match == None:
        return False
    
    logging.info('check_addon_pause match[%s], table_id[%s]'%(match_id, table_id))
    #所有牌桌进入addon状态
    if pause_match.check_real_addon():
        pause_match.addon_start_time = time.time()
        pause_match.real_start_addon = True
        pause_match.update_pause_starttime()                #统一所有牌桌的暂停开始时间
        match.has_addon = True        
        
            
    #可以通知所有牌桌开始addon了吗 
    if pause_match.real_start_addon:
        for tableid in pause_match.table_dict.keys():
            table = TableObject.get( tableid )
            if table == None:
                continue
            msg = {
            P.TABLE_ID         : tableid,
            P.ADDON_START_TIME : pause_match.addon_start_time
            }
            
            c_sequence_id = ''    # 取子序列号
            event = P.TABLE_ADDON
            remotename = table.game_addr
            data = P.pack().event( event ).mid( c_sequence_id ).body( msg ).get()
            Message.send( remotename, data )
        logging.info('Notify Game match[%s] start addon!'%match_id)
    
    
    
    
    
    
    
