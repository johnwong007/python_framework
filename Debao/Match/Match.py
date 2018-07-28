#coding=gbk

import traceback
import math
import zlog as logging
import JsonUtil
import Db.Mysql
import Object.Match as omatch
from . import Config
import Protocol as P


def add_reduce_chips_detail ( tableid, uid, oper_type, save_chips, service_fee, oper_time, box_total ):
    '''
    添加一条卸码的详细记录到表 t_reduce_chips_info
    '''
    sql = '''
            insert into t_reduce_chips_info( f_tableid, f_userid, f_oper, 
                    f_chips, f_service_fee, f_oper_time, f_instime, f_total )
                    values ( %s, %s, %s, %s, %s, %s, now(), %s )
          '''
    args = ( tableid, uid, oper_type, save_chips, service_fee, oper_time, box_total )
    db = Db.Mysql.connect('esun_texas')
    ret = db.execute(sql, args)
    db.commit()

    return ret


def add_ins_detail ( tableid, hand_id, ownerid, ptObj):
    '''
    添加一局保险详细信息(用于oracle后台统计数据)
    '''
    tableName = ptObj[ P.PT_TABLE_NAME ]
    payType = ptObj[ P.PT_PAY_TYPE ]
    for ptUnit in ptObj[ P.PT_USER_ALL_UNIT ]:
        if float(ptUnit[P.USER_PT_OPER_WIN_OR_LOST]) == 0:
            continue

        sql = ''' insert into t_paipu_order( 
                    f_userid, f_ownerid, f_username, f_tableid, 
                    f_handid, f_service, f_currency_type, f_win_amt, 
                    f_order_safe_amt, f_pay_safe_amt, f_tablename, f_addtime ) 
                    values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now() )'''
        args = ( int(ptUnit[P.USER_ID]), str(ownerid), str(ptUnit[P.USER_NAME]), str(tableid), 
                str(hand_id), 'SAFE', str(payType), float(ptUnit[P.PT_USER_CHIPS]), 
                float(ptUnit[P.PT_USER_MONEY]), float(ptUnit[P.USER_PT_OPER_WIN_OR_LOST]), 
                str(tableName) )
        #logging.info('***jason add_ins_detail, args:%s', str(args))
        ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return 0  


def add_ins_history ( tableid, hand_id, ownerid, pots_money, ptObj):
    '''
    添加一局保险回顾信息
    '''
    # 先从表中将用户头像url获取出来
    for ptUnit in ptObj[ P.PT_USER_ALL_UNIT ]:
        sql = ''' select f_user_portrait from t_user_show where f_id = %s '''
        args = ( ptUnit[P.USER_ID] )
        sqlRet = Db.Mysql.connect('esun_texas').query(sql, args)
        if (len(sqlRet) > 0):
            tp = sqlRet[0]
            ptUnit[ P.PT_USER_HEAD_IMG ] = tp['f_user_portrait']

        

    jasonCommCard = JsonUtil.write( ptObj[ P.COMMUNITY_CARDS ] )
    jasonUserList = JsonUtil.write( ptObj[ P.PT_USER_ALL_UNIT ] )
    
    sql = ''' insert into t_product_detail (
                    tableid,
                    handid,
                    ownerid,
                    comm_cards,
                    total_pots,
                    usersinfo, sysIncome) values ( %s, %s, %s, %s, %s, %s, %s )'''
    args = ( tableid, hand_id, ownerid, jasonCommCard, pots_money, jasonUserList, 
        str(ptObj[ P.PT_SYS_PT_INFO ]) )
    #logging.info('***jason add_ins_history, args:%s, sql:%s', str(args), str(sql))
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret 

def add_sys_cash_ins_history ( tableid, hand_id, ownerid, pots_money, ptObj):
    '''
    save the common cash table info in order to reviewing game
    '''
    # logging.info('=====================>add_sys_cash_ins_history')
    # logging.info(str(ptObj))
    db = Db.Mysql.connect('esun_texas')
    # get user url
    for ptUnit in ptObj[ P.PT_USER_ALL_UNIT ]:
        sql = ''' select f_user_portrait from t_user_show where f_id = %s '''
        args = ( ptUnit[P.USER_ID] )
        sqlRet = db.query(sql, args)
        if (len(sqlRet) > 0):
            tp = sqlRet[0]
            ptUnit[ P.PT_USER_HEAD_IMG ] = tp['f_user_portrait']

    

    public_cards = ptObj[ P.COMMUNITY_CARDS ]
    left_public_cards = ptObj[ P.LEFT_COMMUNITY_CARDS ]
    public_cards_num = len(public_cards)
    prefix = [str(public_cards_num)]
    public_cards = list(prefix)+list(public_cards)+list(left_public_cards)    

    # jasonCommCard = JsonUtil.write( ptObj[ P.COMMUNITY_CARDS ] )
    jasonCommCard = JsonUtil.write( public_cards )
    jasonUserList = JsonUtil.write( ptObj[ P.PT_USER_ALL_UNIT ] )
    
    sql = '''
            select *
            from 
            t_product_sys_cash_detail
            where
            tableid = %s
        '''
    args = (tableid)
    ret = db.query(sql, args)
    ret = []
    if ret and len(ret)>0:

        sql = ''' update t_product_sys_cash_detail set
                         tableid = %s,
                         handid = %s,
                         ownerid = %s,
                         comm_cards = %s,
                         total_pots = %s,
                         usersinfo = %s,
                         sysIncome = %s
                   where tableid = %s '''
        args = ( tableid, hand_id, ownerid, jasonCommCard, pots_money, jasonUserList, 
            str(ptObj[ P.PT_SYS_PT_INFO ]), tableid)
    else:
        sql = ''' insert into t_product_sys_cash_detail (
                        tableid,
                        handid,
                        ownerid,
                        comm_cards,
                        total_pots,
                        usersinfo, sysIncome) values ( %s, %s, %s, %s, %s, %s, %s )
            '''
        args = ( tableid, hand_id, ownerid, jasonCommCard, pots_money, jasonUserList, 
            str(ptObj[ P.PT_SYS_PT_INFO ]))
    # logging.info('=====================>'+str(args))
    #logging.info('***jason add_ins_history, args:%s, sql:%s', str(args), str(sql))
    ret = db.execute(sql, args)
    return ret     

def get_create_table_comsump_info(user_id, config_id):
    sql = ''' select sub_type SUB_TYPE, pay_type PAY_TYPE,  pay_number PAY_NUMBER, card_id CARD_ID 
                from t_create_room_log where owner_id = %s and config_id = %s'''
    args = ( user_id, config_id)
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret

def add_pt_adjust_info(table_id, adjust_list):
    db = Db.Mysql.connect('esun_texas')

    # 先删除
    sql = '''
        delete from t_pt_adjust where f_tableid = %s
          '''
    args = (table_id)
    db.execute(sql, args)
    db.commit()

    # 再写入
    for p in adjust_list:
        sql = '''
                insert into t_pt_adjust(f_tableid, f_uid, f_username, f_percent) 
                values (%s, %s, %s, %s)
              '''
        args = ( table_id, p[ P.USER_ID ], p[ P.USER_NAME ], p[ P.PT_POT_PERCENT ] )
        ret = db.execute(sql, args)
        db.commit()

    return []


def get_live_match( match_addr,
                    nolive_status_list = [ Config.STATUS_MATCH_END,
                                           Config.STATUS_MATCH_CANCEL ] ):
    '''获取未结束赛事列表'''
    sql = '''SELECT f_id id,
                    f_name name,
                    f_type type,
                    f_status status,
                    f_real_starttime starttime, 
                    f_level level
               FROM t_match
              where f_show = 'YES'
                and f_examine = 'YES'
                and f_match_addr = %s '''

    args = [match_addr]

    if len( nolive_status_list ) > 0 :
        sql = sql + ' and f_status not in ('
        
        tmp = ''
        for status in nolive_status_list :
            tmp = tmp + '\'' + status + '\','

        sql = sql + tmp[:-1] + ')'
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret

def get_new_match( match_addr, new_status, second_before ):
    '''获取新建赛事列表'''
    sql = '''SELECT f_id id,
                    f_name name,
                    f_type type,
                    f_status status,
                    f_real_starttime starttime,
                    f_level level                       
               FROM t_match
              where f_show = 'YES'
                and f_examine = 'YES'
                and f_match_addr = %s
                and f_uptime < date_sub(now(), interval %s second) '''
    if len( new_status ) > 0 :
        sql = sql + ' and f_status in ('
        
        tmp = ''
        for status in new_status :
            tmp = tmp + '\'' + status + '\','

        sql = sql + tmp[:-1] + ')'

    args = [match_addr, second_before]

    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret


def get_match_without_owner( nolive_status_list = [ Config.STATUS_MATCH_END,
                                           Config.STATUS_MATCH_CANCEL ] ):
    '''获取未被认领的赛事列表'''
    sql = '''SELECT f_id id,
                    f_name name
               FROM t_match
              where f_show = 'YES'
                and f_examine = 'YES'
                and f_match_addr = %s '''

    args = [Config.NO_NAME_OF_MATCH_ADDR]

    if len( nolive_status_list ) > 0 :
        sql = sql + ' and f_status not in ('
        
        tmp = ''
        for status in nolive_status_list :
            tmp = tmp + '\'' + status + '\','

        sql = sql + tmp[:-1] + ')'
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret


def get_e_sport_extral_matchs(match_id):
    ''' 获取电竞比赛对应的其它比赛'''
    sql = '''select f_sub_id as sub_id from t_e_sport_match where f_math_id = %s'''
    args = [match_id]
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret    


def update_match_addr(match_id, addr):
    '''更新赛事地址'''
    sql = '''UPDATE `t_match` SET `f_match_addr` = %s, `f_uptime` = now() WHERE `f_id` = %s '''
    args = [addr, match_id]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_status(match_id, status):
    '''更新赛事状态'''
    sql = '''UPDATE `t_match` SET `f_status` = %s, `f_uptime` = now() WHERE `f_id` = %s '''
    args = [status, match_id]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret
    
def check_add_blind(match_id, match_doing_time):
    '''检查是否要增加盲注，如果真，返回 : [大盲, 小盲, 底注]'''
    
    match = omatch.get(match_id)
    if not match:
        logging.error('model Match.Match.check_add_blind can"t found match:%s', match_id)
        return None
    mc = match.conf
    
    if not mc.blind_conf.has_key(mc.latest_blind_time):
        return None
    
    conf = mc.blind_conf[mc.latest_blind_time]
    
    if match_doing_time > conf[3]: #该升盲了
        mc.latest_blind_time = conf[3]
        return mc.blind_conf[conf[3]][0:3] #大盲, 小盲, 底注
    return None
    
def get_gain_conf(match_id, user_rank):
    '''检查用户是否有获取奖励'''
    match = omatch.get(match_id)
    if not match:
        logging.error('model Match.Match.check_add_blind can"t found match:%s', match_id)
        return None
    mc = match.conf
    
    if user_rank > mc.gain_conf[-1][0][1]: #比最大的钱圈名次还大
        return None
    
    for i in mc.gain_conf:
        if user_rank >= i[0][0] and user_rank <= i[0][1] :
            return i[1]
    
    return None

def load_pay_type(r):
    '''加载参赛条件'''
    sql = '''SELECT f_name name, f_desc idesc, f_result result 
                FROM `t_resources_type` 
             WHERE f_id= %s'''
    ret = Db.Mysql.connect('esun_texas').query(sql, [r.pay_type])
    
    if ret:
        r.pay_desc = ret[0]['idesc']
        r.pay_conf = JsonUtil.read(ret[0]['result'])
    

def load_gain_type(r):
    '''加载获奖物品排名详情'''
    sql = '''SELECT a.f_desc idesc, a.f_prize_start_rank start_rank, a.f_prize_end_rank end_rank, 
                    a.f_resources_type res_type, b.f_name name, b.f_desc res_desc, 
                    b.f_result result FROM `t_gain_type` a 
                LEFT JOIN `t_resources_type` b ON a.f_resources_type = b.f_id 
             WHERE a.f_name = %s ORDER BY a.f_prize_start_rank'''
    ret = Db.Mysql.connect('esun_texas').query(sql, [r.gain_type])
    
    r.gain_desc = ret[0]['idesc']
    
    for i in ret:
        r.gain_res_desc.append(i['res_desc'])
        r.gain_conf.append([[i['start_rank'], i['end_rank']], JsonUtil.read(i['result'])])
    
def load_bind_type(r):
    sql = '''SELECT f_name name, f_desc idesc, f_time time, f_bblind bblind, 
                    f_sblind sblind, f_ante ante, f_level level FROM `t_blind_type` 
             WHERE f_name = %s ORDER BY f_level'''
    ret = Db.Mysql.connect('esun_texas').query(sql, [r.blind_type])

    num = len(ret)
    tLast = 0
    for i in range(num):
        o = ret[i]
        next_time = i < num-1 and ret[i+1]['time'] or 0
        r.blind_conf[tLast] = [o['bblind'], o['sblind'], o['ante'], o['level'], next_time]
        tLast += o['time']
        
        #rebuy赛计算开赛后合法的rebuy时间
        if (r.rebuy == 'YES'):
            if (ret[i]['level'] <= r.rebuy_blindlevel):
                r.valid_rebuy_time += ret[i]['time']
        
def get_match_apply( match_id, pay_status=Config.APPLY_PAY_STATUS, status=Config.APPLY_STATUS ):
    '''
        功能：获取赛事参赛名单(默认是已付款的)
        编写：chend
        创建：2012-1-9 12:14:15
        修改：
                2015-01-16 reEnter 存在多条报名记录，只取一条
    '''
    sql = ''' select DISTINCT(f_uid) user_id,
                     f_username user_name,
                     f_match_id match_id
                from t_apply_match
               where f_match_id = %s
                 and f_pay_status = %s
                 and f_status = %s'''
    ret = Db.Mysql.connect('esun_texas').query(sql, [match_id, pay_status, status])
    return ret

def update_match_starttime( match_id, starttime ):
    '''
        功能：更新赛事的开始时间
        编写：chend
        创建：2012-1-12 17:03:46
        修改：2012-2-6 20:17:20 f_starttime ==> 
    '''
    sql = '''UPDATE `t_match` SET `f_real_starttime` = %s WHERE `f_id` = %s '''
    args = [starttime, match_id]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret
    
def update_match_endtime( match_id ):
    '''记录比赛结束时间'''
    sql = '''UPDATE t_match SET f_endtime = now() 
              WHERE f_id = %s'''
    args = ( match_id, )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_blind_level( match_id, blind_level ):
    '''
        功能：更新赛事的盲注等级
        编写：chend
        创建：2012-1-19 14:20:38
        修改：
    '''
    sql = '''UPDATE `t_match` SET `f_blind_level` = %s, `f_uptime` = now() WHERE `f_id` = %s '''
    args = [blind_level, match_id]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_apply_user_number( match_id, apply_num ):
    '''
        功能：更新赛事的报名人数
        编写：chend
        创建：2012-2-16 14:31:16
        修改：
    '''
    sql = '''UPDATE `t_match` SET `f_apply_users` = %s, `f_uptime` = now() WHERE `f_id` = %s '''
    args = [apply_num, match_id]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def get_match_prize_info( match_id ):
    '''获取赛事奖池'''
    sql = '''SELECT f_id id,
                    f_bonus_pool bonus_pool,
                    f_bonus_caution_money bonus_caution_money
               FROM t_match
              WHERE f_id = %s '''

    args = [ match_id ]
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret

def ensure_prize_pool( match_id ):
    '''
        功能：更新赛事的奖池
        编写：chend
        创建：2012-1-19 14:20:38
        修改：
    '''
    sql = '''UPDATE t_match
                SET f_bonus_caution_money_used = f_bonus_caution_money - f_bonus_pool,
                    f_bonus_pool = f_bonus_caution_money,
                    f_uptime = now()
              WHERE f_id = %s '''
    args = [match_id]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def get_match_addr_config_count( addr ):
    '''
        功能：取赛事地址在配置表中的条数
        编写：chend
        创建：2012-2-16 14:27:26
        修改：
    '''
    sql = '''SELECT count(*) cnt
               FROM t_config_match_addr
              WHERE f_match_addr = %s '''

    args = [ addr ]
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret[0]['cnt']


def get_all_match_addr(job, order='TABLE', status = 'RUNNING'):
    '''
        功能：取所有赛事地址
        编写：chend
        创建：2012-2-29 18:16:15
        修改：添加job参数，指定是承载现金桌还是比赛
              CASH  现金桌
              MATCH 比赛
    '''
    if job not in ('CASH', 'MATCH'):
        logging.error('get_all_match_addr job type error! %s'%job)
        return []
        
    sql = '''SELECT f_match_addr match_addr,
                    f_table_num table_num,
                    f_match_num match_num,
                    f_cash_num cash_num
               FROM t_config_match_addr
              WHERE f_status = %s 
          '''
    args = [status]
    
    if None != job:
        sql += ' and f_adminnote = %s'
        args.append(job)
        
    sql += " ORDER BY "
    if 'MATCH' == order:
        sql = sql + 'f_match_num'
    elif 'CASH' == order:
        sql = sql + 'f_cash_num'
    else:
        sql = sql + 'f_table_num'
    
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    #logging.debug('get_all_match_addr ret = %s'%str(ret))
    return ret

    

def add_match_addr_config( addr, desc, status, admin, adminnote ):
    '''
        功能：插入赛事服务地址配置表
        编写：chend
        创建：2012-2-16 12:29:19
        修改：
    '''

    sql = ''' insert into t_config_match_addr (
                    f_match_addr,
                    f_desc,
                    f_status,
                    f_adminname,
                    f_adminnote,
                    f_table_num,
                    f_match_num,
                    f_cash_num,
                    f_uptime,
                    f_instime) values ( %s, %s, %s, %s, %s, 0, 0, 0, now(), now() )'''
    args = ( addr, desc, status, admin, adminnote )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_addr_config( table_num, match_num, cash_num, addr ):
    '''
        功能：更新赛事服务地址配置表的赛桌个数
        编写：chend
        创建：2012-2-16 12:29:19
        修改：
    '''

    sql = ''' update t_config_match_addr set
                     f_table_num = %s,
                     f_match_num = %s,
                     f_cash_num = %s,
                     f_uptime = now()
               where f_match_addr = %s '''
    args = ( table_num, match_num, cash_num , addr )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_addr_config_mnum( match_num, addr ):
    '''
        功能：更新赛事服务地址配置表的赛事个数
        编写：chend
        创建：2012-3-1 15:56:46
        修改：
    '''

    sql = ''' update t_config_match_addr set
                     f_match_num = %s,
                     f_uptime = now()
               where f_match_addr = %s '''
    args = ( match_num, addr )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_addr_config_cnum( cash_num, addr ):
    '''
        功能：更新赛事服务地址配置表的赛桌个数
        编写：chend
        创建：2012-3-1 15:56:51
        修改：
    '''

    sql = ''' update t_config_match_addr set
                     f_cash_num = %s,
                     f_uptime = now()
               where f_match_addr = %s '''
    args = ( cash_num , addr )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_addr_config_tnum( table_num, addr ):
    '''
        功能：更新赛事服务地址配置表的赛桌个数
        编写：chend
        创建：2012-3-1 15:56:51
        修改：
    '''

    sql = ''' update t_config_match_addr set
                     f_table_num = %s,
                     f_uptime = now()
               where f_match_addr = %s '''
    args = ( table_num , addr )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def update_match_addr_config_status( status, addr, adminnote = None ):
    '''
        功能：更新赛事服务地址配置表的状态
        编写：chend
        创建：2012-2-23 11:09:36
        修改：
    '''

    sql = ''' update t_config_match_addr set
                     f_status = %s,
                     f_adminnote = %s,
                     f_uptime = now()
               where f_match_addr = %s '''
    args = ( status, adminnote, addr )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def register_match_addr( ser_addr ):
    '''
        功能：到数据库中登记赛事服务地址
        描述：注意这里没有对重复的数据进行异常处理；组名固定。。。
        编写：chend
        创建：2012-2-16 16:45:48
        修改：
    '''
    addr = ( Config.LOCAL_GROUP_NAME, ser_addr )
    addr = str(addr)
    cnt = get_match_addr_config_count( addr )
    
    if ser_addr in Config.CASH_MATCH.split(','):
        adminnote = 'CASH'
    else:
        adminnote = 'MATCH'

    if cnt <= 0:
        desc = '赛事服务' + ser_addr
        desc = desc.decode("gbk").encode("utf-8")
        status = 'RUNNING'
        admin = 'match'            
        add_match_addr_config( addr, desc, status, admin, adminnote )
    else:
        status = 'RUNNING'
        update_match_addr_config_status( status, addr, adminnote )


def unregister_match_addr( ser_addr ):
    '''
        功能：到数据库中注销赛事服务地址
        编写：chend
        创建：2012-2-23 11:11:14
        修改：
    '''
    addr = ( Config.LOCAL_GROUP_NAME, ser_addr )
    addr = str(addr)

    status = 'STOP'
    update_match_addr_config_status( status, addr )


def copy_sitandgo_match( match_id ):
    '''
        功能：拷贝生成一个坐满即开
        编写：chend
        创建：2012-2-27 15:32:21
        修改：
    '''
    sql = '''
        insert into t_match ( 
               f_name, f_type, f_play_type, f_level, f_status, f_desc, f_blind_type,
               f_blind_level, f_seat_num, f_init_chips, f_waittime, f_plan_starttime,
               f_real_starttime, f_endtime, f_show_time, f_apply_time, f_apply_delay_time,
               f_apply_quit_time, f_forcedend_time, f_pay_type, f_pay_money,  
               f_hand_fee, f_apply_users, f_bonus_pool, f_bonus_ratio, f_bonus_caution_money,  
               f_bonus_caution_money_used, f_min_player, f_max_player, f_gain_config,
               f_bonus_config, f_inthemoney_ratio, f_match_addr, f_game_addr,
               f_prize_status, f_prize_pool, f_show, f_examine, f_examine_admin,
               f_examine_time, f_instime, f_uptime, f_admin, f_adminnote, f_isback, f_copy_cnt,
               f_mobile_apply, f_permission_idx, f_kick_out_offline_user, f_disp_color,
               f_priority, f_pause, f_rebuy, f_rebuy_times,
               f_legal_rebuy_level, f_rebuy_value, f_rebuy_paytype, f_rebuy_paymoney,
               f_addon, f_addon_value, f_addon_paymoney, f_valid_rebuy_time,
               f_addon_wait_time, f_all_in, f_target_gameaddr, f_realtime_apply)
        select f_name, f_type, f_play_type, f_level, 'ANNOUNCED', f_desc, f_blind_type,
               1, f_seat_num, f_init_chips, f_waittime, f_plan_starttime,
               null, f_endtime, f_show_time, now(), f_apply_delay_time,
               f_apply_quit_time, f_forcedend_time, f_pay_type, f_pay_money,  
               f_hand_fee, 0, 0, f_bonus_ratio, f_bonus_caution_money,  
               0, f_min_player, f_max_player, f_gain_config,
               f_bonus_config, f_inthemoney_ratio, %s, f_game_addr,
               'NOPRIZE', 0, f_show, f_examine, 'match_server',
               now(), now(), now(), 'match_server', 'auto_genarate', f_isback, f_copy_cnt-1,
               f_mobile_apply, f_permission_idx, f_kick_out_offline_user, f_disp_color,
               f_priority, f_pause, f_rebuy, f_rebuy_times,
               f_legal_rebuy_level, f_rebuy_value, f_rebuy_paytype, f_rebuy_paymoney,
               f_addon, f_addon_value, f_addon_paymoney, f_valid_rebuy_time,
               f_addon_wait_time, f_all_in, f_target_gameaddr, 0 
          from t_match where f_id = %s and f_copy_cnt - 1 >= 0 '''
    args = ( Config.NO_NAME_OF_MATCH_ADDR, match_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret
    
    
def kickout_or_not(match_id):
    '''
        查询赛事配置，是否要踢出不在线用户
        入参：match_id
        出参：True
              False
        编写：liulk
        日期：2012.08.08  15:02
    '''
    sql = '''SELECT f_kick_out_offline_user kickout
                FROM t_match
             WHERE f_id = %s'''
    args = (match_id)
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    
    if len(ret) != 0:
        if ret[0]['kickout'] == 'YES':
            return True
    return False
    
def getPauseTable(match_id, status_1 = Config.STATUS_TABLE_PAUSE,
                    status_2 = Config.STATUS_TABLE_OPENED):
    '''
        1.取处于暂停状态的牌桌列表
        2.考虑到以前没处理OPENED状态的牌桌，现在试着处理下
    '''
    sql = '''SELECT f_id table_id, f_uptime uptime,
                    f_rest_time rest_time
             FROM t_match_table_list
             WHERE f_match_id = %s 
             AND f_status in (%s, %s)'''
    args = (match_id, status_1, status_2)
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    
    if len(ret) != 0:
        return ret
    else:
        return None
        
def updateTableRestTime(table_id, total_rest_time):
    '''记录牌桌总共休息了多长时间'''
    sql = '''UPDATE t_match_table_list
               SET f_rest_time = %s
               WHERE f_id = %s'''
    args = (total_rest_time, table_id)
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret
        
def update_rebuy_order_status(rebuy_orderid, status):
    '''更新rebuy订单状态'''
    sql = '''UPDATE t_rebuy_chips_order
              SET f_status = %s,
                  f_uptime = now()
             WHERE f_id = %s'''
    args = (status, rebuy_orderid)
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_bonus(match_id, bonus_inc):
    '''rebuy,addon赛事增加奖池'''
    sql = '''UPDATE t_match
                SET f_bonus_pool = f_bonus_pool + %s,
                    f_uptime = now()
              WHERE f_id = %s'''
    args = (bonus_inc, match_id)
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret
    
def update_match_bonus_new(match_id, bonus_inc):
    '''rebuy,addon赛事增加奖池'''
    db = Db.Mysql.connect('esun_texas')
    # 1. 已经被使用的保证金金额
    try:
        sql_1 = '''select f_bonus_caution_money_used bcm_used
                   from t_match 
                   where f_id = %s'''
        args_1 = ( match_id, )
        ret = db.query(sql_1, args_1)
    except:
        logging.error('%s'%traceback.format_exc())
        return False
    
    if not ret:
        return False
        
    try:
        bcm_used = int(ret[0]['bcm_used'])                               #被使用的保证金
        # 2. 优先填补被使用掉的保证金
        if bonus_inc <= bcm_used:
            sql_2 = '''update t_match 
                          set f_bonus_caution_money_used = f_bonus_caution_money_used - %s
                        where f_id = %s'''
            args_2 = (bonus_inc, match_id)
            ret = db.execute(sql_2, args_2)
            db.commit()
            return ret
        # 填补完用掉的保证金后将余额投到奖池中去
        else:
            sql_3 = '''update t_match
                          set f_bonus_pool = f_bonus_pool + %s - f_bonus_caution_money_used,
                              f_bonus_caution_money_used = 0
                        where f_id = %s'''
            args_3 = (bonus_inc, match_id)
            ret = db.execute(sql_3, args_3)
            db.commit()
            return ret            
    except:
        logging.error('%s'%traceback.format_exc())
        return False
    
    return ret
    
    
def update_valid_rebuy_time(valid_time, match_id):
    '''rebuy赛，开赛后合法的rebuy时间'''
    sql = '''UPDATE t_match
                SET f_valid_rebuy_time = %s,
                    f_uptime = now()
              WHERE f_id = %s'''
    args = (valid_time, match_id)
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret
    
def get_bonus_qianquan(match_id, user_num):
    '''获取bonous_config钱圈比例'''
    sql = '''SELECT
                    b.f_inthemoney_ratio inthemoney_ratio,
                    b.f_end_rank end_rank
             FROM t_match a
             INNER JOIN t_bonus_config b
                        ON
                    a.f_bonus_config = b.f_name 
             WHERE a.f_id = %s
             AND b.f_start_players <= %s
             AND b.f_end_players >= %s
             ORDER BY b.f_id DESC
            LIMIT 1'''
    args = (match_id, user_num, user_num)
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    if len(ret) == 0:
        return 0
    else:
        money_ratio = math.ceil(float(ret[0]['end_rank'])/user_num * 100)
        return int(money_ratio)
        # return int(ret[0]['inthemoney_ratio'])
        
def get_gain_qianquan(match_id, user_num):
    '''计算gain_config钱圈比例'''
    if user_num == 0:
        return 0
        
    sql = '''SELECT
                        b.f_end_rank max_end_rank
              FROM t_match a
              INNER JOIN t_gain_config b
                        ON
                        a.f_gain_config = b.f_name 
             WHERE a.f_id = %s
             ORDER BY max_end_rank DESC
             LIMIT 1'''
    args = (match_id)
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    if len(ret) == 0:
        return 0
    else:
        max_end_rank = int(ret[0]['max_end_rank'])
        if max_end_rank >= user_num:
            gain_ratio = 100
        else:
            gain_ratio = ret[0]['max_end_rank'] / float(user_num) * 100
        return int(gain_ratio)
    
def update_inthemoney_ratio(match_id, inthemoney_ratio):
    '''更新赛事钱圈比'''
    sql = '''UPDATE t_match
                SET f_inthemoney_ratio = %s,
                    f_uptime = now()
              WHERE f_id = %s'''
    args = (inthemoney_ratio, match_id)
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    logging.info('Update match[%s] inthemoney_ratio[%s]'%(match_id, inthemoney_ratio))
    
    
def update_config_use_status(cash_id, status):
    '''
        更改配置使用状态
    '''
    sql = '''update t_cash_table_config 
                set f_in_use = %s,
                    f_uptime = now()
              where f_id = %s'''
    args = (status, cash_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    logging.info('update cash_table_config in use NO, cash[%s]'%cash_id)     
    
def del_cash_table_list(table_id):
    '''
        从牌桌列表中清楚指定牌桌
    '''

    sql = '''delete from t_table_succ_user_enter where table_id =  %s'''
    args =  (table_id,)
    Db.Mysql.connect('esun_texas').execute(sql, args)

    sql = '''delete from t_cash_table_list
              where f_id = %s'''
    args = (table_id, )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    logging.info('delete cash table %s'%table_id) 


    
    