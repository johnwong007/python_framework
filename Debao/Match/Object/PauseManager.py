#coding=utf-8

import time
import math
import zlog as logging

from . import Table as TableObject
from . import Match as MatchObject

from .. import Protocol as P
from .. import Message as Message


'''
    ������ͣ״̬�����¶����ֵ�
    {match_id : match_obj, ...}
'''
_PAUSE_MATCH_DICT_ = {}

'''
    table_dict �ṹ��
    
    {
        table_id : {
                        ADDON_FLAG : FALSE,
                        PAUSE_FLAG : FALSE,     #��������־λ��ΪFalse��ʱ�򣬿��Լ�������
                    },
        ...
    }
'''




class PauseMatch:
    '''
        ���д�����ͣ״̬�ı�����
            PAUSE: ��������ǰ5���ӵ���ͣ��Ϣ
            ADDON�����ռ���ʱ�ε���ͣ
    '''
    def __init__(self, match_id):
        self.match_id           = match_id
        self.pause_table_num    = 0             #������ͣ״̬��������
        self.table_dict         = {}            #
        self.can_run            = False         #�ܷ�����־λ
        
        self.real_start_addon   = False         #�Ƿ񴥷���addon
        self.addon_table_num    = 0             #����addon״̬��������
        self.addon_start_time   = 0             #��������addon��ʼʱ���
        self.addon_wait_time    = 0             #addon�ȴ�ʱ��

        self.hbh_flag           = False         #hands-by-hands��־
        self.hbh_table_num      = 0             #����hbh״̬��������
            
    def add_pause_table(self, table_id, reason):
        '''
            ����һ����ͣ������
            reason: ������ԭ�� PAUSE_FLAG/ADDON_FLAG
            
        '''
        table = TableObject.get( table_id )
        if not table:
            logging.error('from add_pause_table: not exist table[%s]'%table_id)
            return 
        
        #���Ƚ�����������ǩ��־λ
        self.supply_table_flag(reason)
            
        logging.info('before add_table : %s, reason[%s]'%(self.table_dict, reason))    
        if self.table_dict.has_key(table_id):
            self.table_dict[table_id][reason] = True
        else:
            flag_info = {}
            #��ʼ�����ݽṹ
            flag_info['PAUSE_FLAG'] = False
            flag_info['ADDON_FLAG'] = False 
            flag_info['HBH_FLAG']   = False 

            self.table_dict[table_id] = flag_info
            table.pause_time = time.time()              #��¼��ͣ��ʼʱ��
            
            #�ñ�־λ
            self.table_dict[table_id][reason] = True
            self.pause_table_count(reason)
            
        logging.info('after add_table : %s, reason[%s]'%(self.table_dict, reason))
        #��������������
        self.pause_table_num = len(self.table_dict)


    def pause_table_count(self, reason):
        ''''''
        if reason == 'ADDON_FLAG':
            self.addon_table_num += 1
        elif reason == 'HBH_FLAG':
            self.hbh_table_num += 1


    def clear_table_flag(self, table_id, reason):
        '''���־λ'''
        logging.info('---------------->IN clear_table_flag')
        if self.table_dict.has_key(table_id):
            self.table_dict[table_id][reason] = False
            return True
        else:
            return False
            
    def supply_table_flag(self, reason):
        '''��ǩ��־λ'''
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
            #���κ�һ����־λΪTrue���˳�
            if self.table_dict[i]['PAUSE_FLAG'] or self.table_dict[i]['ADDON_FLAG'] \
                or self.table_dict[i]['HBH_FLAG']:
                return
        #���������ı�־Ϊ����False,���Լ���������
        self.can_run = True
    
      
    def check_real_addon(self):
        '''���ó������Ƿ������ʽaddon��'''
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
            ���¸���������ͣ��ʼʱ�䣬�Ա�ͳһäע
        '''
        tid_list = self.table_dict.keys()                           #ȡ���е�����id
        
        for id in tid_list:
            table = TableObject.get( id )
            if not table:
                logging.error('from update_pause_starttime: not exist table[%s]'%table_id)
                continue
            
            table.pause_time = self.addon_start_time                #ͳһ��ͣ��ʼʱ��
            
        
################################################################################

def get_pause_match(match_id):
    '''ȡһ������'''
    global _PAUSE_MATCH_DICT_
    
    if _PAUSE_MATCH_DICT_.has_key(match_id):
        return _PAUSE_MATCH_DICT_[match_id]
    else:
        return None
        
def add_pause_match(match_id, pause_obj):
    '''����һ������'''
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
        �жϵ�ǰʱ���Ƿ�Ϊ��Ϣʱ���
        Ĭ����Ϣʱ��Σ�55��--00�����㣩
    '''
    try:
        current_minute = time.strftime("%M", time.localtime())
        #ȡ��ǰʱ��ķ����� ��15:30:42  ������Ϊ30
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
        �жϸ������Ƿ���Ҫ��ͣ��Ϣ
        ��Σ�match����
        ���Σ�True/False
        ��д��liulk
        ���ڣ�2012.09.06  14:21
    '''
    try:
        #�����ж���������
        if match.conf.pause == 'YES':
            logging.info('match [%s] is setted need pause!'%match.match_id)
            #���ж��Ƿ���Ϣʱ���
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
        �Ƚ�ǮȦ��������ǰ����
        ����ǮȦ����rebuy��addon
        ��Σ�
        ���Σ�True/False    True:����rebuy/addon  False:������
        ��д��liulk
        ���ڣ�2012.11.08  13:52
    '''
    if not match:
        logging.info('JUDGE: match----> %s'%match)
        return False
    #ȡǮȦ����,ǮȦ��Ϊ0����Ϊʵ�ｱ�������ر䶯��Ӱ��
    inthemoney_ratio = match.conf.inthemoney_ratio
    #logging.info('match[%s] inthemoney_ratio = %s'%(match.match_id, inthemoney_ratio))
    if inthemoney_ratio == 0:
        return True
        
    #������
    total_users = len(match.user_list)
    #ǮȦ����
    inthemoney_num = int(total_users * inthemoney_ratio / 100)
    #��ǰʣ�������Ŀ = ���� - �Ѿ���̭��
    alive_user_num = total_users - len(match.player_lose_list)
    #logging.info('total_users[%s], inthemoney_num[%s], alive_user_num[%s]'
                    #%(total_users, inthemoney_num, alive_user_num))
    
    if alive_user_num <= inthemoney_num:
        return False
    else:
        return True
        

def need_addon(match, player_count):
    '''
        �ж��Ƿ�addonʱ��
        ��Σ�match���� table����
        ���Σ�True/False
        ��д��liulk
        ���ڣ�2012.10.29  10:37
    '''
    try:
        #����Ϊ����addon�����£���û��addon���Ĳſ���addon,���һ���˵�ʱ�򲻴���addon
        if match.conf.addon == 'YES' and match.has_addon == False and player_count > 1:
            #�жϵ���ǮȦ����û�У��絽�ﲻ��addon
            ret = judge_qianquan_user(match)

            # ��ֹ�������Ѿ�����֮ǰ����Ⱥ�addon��״̬�����±�����ס��bug
            if not ret:
                if get_pause_match(match.match_id):
                    logging.info('need_addon: already in qianquan, but some tables are in _PAUSE_MATCH_DICT_')
                else:
                    logging.debug('from need_addon: IN qianquan no addon! match[%s]'%match.match_id)
                    return False
            
            #�ж��Ƿ񵽴���Ӧ��äע����
            blind_conf = match.get_blind_conf()
            next_blindlevel = int(blind_conf[3])
            #Ҫ��ä�ˣ���äǰ���ռ���Ļ��ᵽ�ˡ���
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
        1. ��ǰ���� == final-talbe���� + 1
        2. ǮȦ���� +1 == ��ǰ���� 
    '''
    try:
        # ������������Ѿ�������������hands-by-hands״̬����ô����������������
        # Ӧ�ý����״̬��Ȼ��ͳһ���״̬
        pause_match = get_pause_match(match.match_id)
        if pause_match and pause_match.hbh_flag:
            return True


        alive_num = match.get_alive_player()
        
        # ��һ�������final-table
        if alive_num == match.conf.seat_num + 1:
            logging.debug("match[%s] final-table hands-by-hands!"%match.match_id)
            return True

        # �ڶ��������ǮȦ����
        inthemoney_num = match.conf.inthemoney_ratio/100.0 * len(match.user_list)
        if inthemoney_num == 0 or inthemoney_num <= match.conf.seat_num:
            return False

        # total_table_num = len(match.table_list) - match.destroying_table_num
        
        # �ҵ�������ǮȦ��������С������
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
    '''�ж��Ƿ�����ͣʱ�����addonʱ��'''
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
        ������д�����ͣ״̬������
        �Ѿ��������㣬�ָ���־λ
    '''
    for match_id in match_list:
        pause_match = get_pause_match(match_id)
        if not pause_match:
            logging.error('from check_pause_flag: not exist match_id[%s]'%match_id)
            return
            
        #û�����Ӵ���������ͣ״̬������
        # if pause_match.time_pause == False:
            # continue
        
        for table_id in pause_match.table_dict.keys():
            pause_match.table_dict[table_id]['PAUSE_FLAG'] = False
        
        #��������ͣ��־λ����ʾ�Ѿ�����������ͣ��
        #pause_match.time_pause = False
        
        
def check_addon_flag(match_list):
    '''
        ��鴦��addon״̬�ı���
        addonʱ������ͻָ����λ
    '''
    for match_id in match_list:
        pause_match = get_pause_match(match_id)
        if not pause_match:
            logging.error('from check_addon_flag: not exist match_id[%s]'%match_id)
            return

        #ֻ������������addon�ż���check
        if pause_match.real_start_addon:
            #addon�ȴ�ʱ���Ƿ񵽴�
            pass_time = time.time() - pause_match.addon_start_time 
            #�ȴ�ʱ���ѵ������������ָ���־λ
            if pass_time >= pause_match.addon_wait_time:
                for table_id in pause_match.table_dict.keys():
                    pause_match.table_dict[table_id]['ADDON_FLAG'] = False
                    logging.info('check_addon_flag set flag = False, table[%s]'%table_id)
                
            
def check_hbh_flag(match_list):
    '''
        ��鴦��hbh״̬�ı���
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

        #�޸��ӳٵǼǵ��µı�������
        #������������ʱ���´����Ļ�δ����ͬ�����������Ҳ���ȥ
        if pause_match.hbh_table_num + len(match.no_sync_table_list) >= total_table_num:
            for table_id in pause_match.table_dict.keys():
                pause_match.table_dict[table_id]['HBH_FLAG'] = False


def check_match_canrun(match_list):
    '''��� can_run��־'''
    for match_id in match_list:
        pause_match = get_pause_match(match_id)
        if not pause_match:
            logging.error('from check_match_canrun: not exist match_id[%s]'%match_id)
            continue
            
        pause_match.check_all_flag()
        
        
def deal_pause_table():
    '''
        ��������ͣ״̬��������PAUSE/ADDON/HBH
        ��д��liulk
        ���ڣ�2012.11.16  13:40
        �޸ģ�2014-07-24  11:27 ����hands-by-hands����
    '''
    match_list = get_pause_list()
    #logging.info('in deal_pause_table PAUSE_MATCH_LIST------->%s'%match_list)
    if len(match_list) == 0:
        return
    
    #1. �ָ�������ͣ������־λ
    if not is_time_to_pause():
        check_pause_flag(match_list)
        
    #2. �ָ�addon��ͣ��־λ
    check_addon_flag(match_list)

    #3. ����hbh״̬
    check_hbh_flag(match_list)
    
    #4. �ָ�������������־λ��ΪFalse��
    for m in match_list:
        pause_match = get_pause_match(m)
        logging.debug("in deal_pause_table------>Pause match info: mid=%s, table_dict=%s"%(m, pause_match.table_dict))
    check_match_canrun(match_list)
    

def check_addon_pause(match, match_id, table_id):
    '''
        ����һ������ʱ���ó������Ƿ����addon/pause ״̬
        ����: 2013-01-03 14:25
        ���ߣ�������
        Ŀ�ģ��޸�addon����������bug
    '''
    pause_match = get_pause_match(match_id)
    
    #�ó�����û�д��ڵȴ�addon/pause ״̬
    if pause_match == None:
        return False
    
    logging.info('check_addon_pause match[%s], table_id[%s]'%(match_id, table_id))
    #������������addon״̬
    if pause_match.check_real_addon():
        pause_match.addon_start_time = time.time()
        pause_match.real_start_addon = True
        pause_match.update_pause_starttime()                #ͳһ������������ͣ��ʼʱ��
        match.has_addon = True        
        
            
    #����֪ͨ����������ʼaddon���� 
    if pause_match.real_start_addon:
        for tableid in pause_match.table_dict.keys():
            table = TableObject.get( tableid )
            if table == None:
                continue
            msg = {
            P.TABLE_ID         : tableid,
            P.ADDON_START_TIME : pause_match.addon_start_time
            }
            
            c_sequence_id = ''    # ȡ�����к�
            event = P.TABLE_ADDON
            remotename = table.game_addr
            data = P.pack().event( event ).mid( c_sequence_id ).body( msg ).get()
            Message.send( remotename, data )
        logging.info('Notify Game match[%s] start addon!'%match_id)
    
    
    
    
    
    
    
