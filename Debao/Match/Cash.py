#coding=gbk
import zlog as logging
import JsonUtil
import Db.Mysql
from . import Config

def get_cash_config( match_addr ):
    '''
        功能：获取现金赛配置
        编写：chend
        创建：2012-2-7 19:34:35
        修改：2013-05-14 添加f_in_use字段
    '''
    sql = '''
        select  f_id                    cash_id,
                f_name                  config_name,
                f_seat_num              seat_num,
                f_level                 level,
                f_pay_type              pay_type,
                f_rate                  rate,
                f_min_coins             min_buyin,
                f_max_coins             max_buyin,
                f_ante                  ante,
                f_big_blind             big_blind,
                f_small_blind           small_blind,
                f_new_blind             new_blind,
                f_rake_before_flop      rake_before_flop,
                f_rake_ratio_after_flop rake_ratio_after_flop,
                f_max_rake_after_flop   max_rake_after_flop,
                f_waittime              waittime,
                f_is_rebuy              is_rebuy,
                f_turn_bigblind         turn_bigblind,
                f_holdtime              holdtime,
                f_reentertime           reentertime,
                f_entrusttimes          entrusttimes,
                f_min_tables            min_tables,
                f_max_tables            max_tables,
                f_match_addr            match_addr,
                f_serv_addr             serv_addr,
                f_rule_type             rule_type,
                f_target_gameaddr       target_gameaddr,
                SUBSTRING(f_card_endtime, 1) card_endtime,
                f_passwd                passwd,
                f_owner                 owner,
                f_play_type             play_type
           from t_cash_table_config
          where f_match_addr = %s and f_examine = 'YES'
            and f_in_use = 'YES'
    '''
    args = [match_addr]
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    
    return ret


def get_new_cash_config( match_addr, second_before ):
    '''
        功能：获取现金赛配置
        编写：chend
        创建：2012-2-7 19:34:35
        修改：
    '''
    sql = '''
        select  f_id                    cash_id,
                f_name                  config_name,
                f_seat_num              seat_num,
                f_level                 level,
                f_pay_type              pay_type,
                f_rate                  rate,
                f_min_coins             min_buyin,
                f_max_coins             max_buyin,
                f_ante                  ante,
                f_big_blind             big_blind,
                f_small_blind           small_blind,
                f_new_blind             new_blind,
                f_rake_before_flop      rake_before_flop,
                f_rake_ratio_after_flop rake_ratio_after_flop,
                f_max_rake_after_flop   max_rake_after_flop,
                f_waittime              waittime,
                f_is_rebuy              is_rebuy,
                f_turn_bigblind         turn_bigblind,
                f_holdtime              holdtime,
                f_reentertime           reentertime,
                f_entrusttimes          entrusttimes,
                f_min_tables            min_tables,
                f_max_tables            max_tables,
                f_match_addr            match_addr,
                f_serv_addr             serv_addr,
                f_rule_type             rule_type,
                f_target_gameaddr       target_gameaddr,
                SUBSTRING(f_card_endtime, 1) card_endtime,
                f_passwd                passwd,
                f_owner                 owner,
                f_play_type             play_type
           from t_cash_table_config
          where f_match_addr = %s
            and f_examine = 'YES'
            and f_uptime < date_sub(now(), interval %s second)
            and f_in_use = 'YES'
    '''
    args = [match_addr, second_before]
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret


def get_cash_without_owner():
    '''
        功能：获取现金赛配置
        编写：chend
        创建：2012-2-7 19:34:35
        修改：
    '''
    sql = '''
        select  f_id                    cash_id,
                f_name                  config_name
           from t_cash_table_config
          where f_examine = 'YES'
            and f_match_addr = %s
    '''
    args = [Config.NO_NAME_OF_MATCH_ADDR]
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret

def update_match_addr(cash_id, addr):
    '''更新赛事地址'''
    sql = '''UPDATE `t_cash_table_config` SET `f_match_addr` = %s, `f_uptime` = now() WHERE `f_id` = %s '''
    args = [addr, cash_id]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_cash_chips_order_status( order_id, status, remark ):
    '''
        功能：更新玩家筹码订单表的状态
        编写：chend
        创建：2012-2-9 15:25:21
        修改：
    '''
    
    sql = '''update t_cash_chips_order
                set f_status = %s,
                    f_remark = %s,
                    f_uptime = now()
              where f_id = %s
    '''
    args = ( status, remark, order_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)

    return ret

    
def insert_cash_chips_order( player_id, user_id, user_name, table_id,
    inout, busisort, pay_type, pay_id, chips, pay_money, pay_channel,
    status, remark='' ):
    '''
        功能：插入玩家筹码订单表
        编写：chend
        创建：2012-2-9 14:54:51
        修改：execute --> insert 
    '''
    
    sql = ''' insert into t_cash_chips_order (
                    f_player_id,
                    f_uid,
                    f_username,
                    f_table_id,
                    f_inout,
                    f_busisort,
                    f_pay_type,
                    f_pay_id,
                    f_chips,
                    f_pay_money,
                    f_pay_channel,
                    f_status,
                    f_remark,
                    f_instime,
                    f_uptime) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now(), now() )'''
    args = ( player_id, user_id, '', table_id,
    inout, busisort, pay_type, pay_id, chips, pay_money, pay_channel,
    status, remark )
    order_id = Db.Mysql.connect('esun_texas').insert(sql, args)
    return order_id


def insert_reduce_chips_service_fee( player_id, user_id, user_name, table_id, table_name, hand_id,  
    busisort, pay_type, pay_id, chips, pay_money, pay_channel, status, remark=''):
    '''
        写卸码相关的服务费
    '''
    #logging.info('*** insert_reduce_chips_service_fee, handid:%s', str(hand_id))
    orderid = insert_cash_chips_order(player_id, user_id, user_name, table_id,
                            'OUT', busisort, pay_type, pay_id, chips, pay_money, pay_channel,
                            status, remark)

    sql = ''' insert into t_user_acct_order( 
                    f_uid, f_username, f_status, f_inout, f_acct_type, 
                    f_busisort, f_busino, f_channel, f_transorder, f_transmoney, 
                    f_addtime, f_lastmodifytime, f_content) 
                    values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now(), now(), %s )
          '''
    args = ( user_id, user_name, 'SUC', 'OUT', pay_type, busisort, 'SYS_REDUCE_CHIP', 
                'LOBBY', orderid, chips, table_id)
    Db.Mysql.connect('esun_texas').insert(sql, args)

    # 继续写 t_paipu_order 表 (orcale后台需要)
    sql = '''
            insert into t_paipu_order( 
                f_userid, f_username, f_tableid, f_handid, f_service, 
                f_currency_type, f_win_amt, f_tablename, f_addtime)
                values ( %s, %s, %s, %s, %s, %s, %s, %s, now())
          '''
    args = ( user_id, user_name, str(table_id), str(hand_id), 'REDUCE_CHIP_FEE',
                'POINT',  pay_money, str(table_name))
    Db.Mysql.connect('esun_texas').insert(sql, args)
    return


def insert_system_pump_info( player_id, user_id, user_name, table_id,
    inout, busisort, pay_type, pay_id, chips, pay_money, pay_channel,
    status, remark='' ):
    '''
        写入系统抽水相关信息
    '''
    orderid = insert_cash_chips_order(player_id, user_id, user_name, table_id,
                            inout, busisort, pay_type, pay_id, chips, pay_money, pay_channel,
                            status, remark)

    sql = ''' insert into t_user_acct_order( 
                    f_uid, f_username, f_status, f_inout, f_acct_type, 
                    f_busisort, f_busino, f_channel, f_transorder, f_transmoney, 
                    f_addtime, f_lastmodifytime, f_content) 
                    values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now(), now(), %s )
          '''
    args = ( user_id, user_name, 'SUC', inout, pay_type, busisort, 'SYS_PUMP', 
                'LOBBY', orderid, chips, table_id)
    Db.Mysql.connect('esun_texas').insert(sql, args)
    return


    
def insert_cash_table_config(name, seat_num, level, pay_type, min_coins, max_coins, 
                      big_blind, small_blind, rake_before_flop, waittime, holdtime,
                      reentertime, entrusttimes, match_addr, target_gameaddr,
                      card_endtime, passwd, owner, service_fee_rate, antedefault, insstate, 
                      sub_table_type, auto_blind, bott_pre_bbtimes, pump_rate,
                      redu_chip_limit, redu_chip_service_rate, apply_buyin_open, pt_pot_open, 
                      card_compare_type, pk_first_bet, redu_chip_flag):
    '''
        记录玩家所创牌桌的配置信息
    '''
    sql = '''insert into t_cash_table_config(
                f_name, f_seat_num, f_level, f_pay_type,
                f_rate, f_min_coins, f_max_coins, f_ante,
                f_big_blind, f_small_blind, f_new_blind, f_rake_before_flop,
                f_rake_ratio_after_flop, f_max_rake_after_flop, f_waittime, f_is_rebuy,
                f_turn_bigblind, f_holdtime, f_reentertime, f_entrusttimes,
                f_min_tables, f_max_tables, f_examine, f_match_addr, 
                f_instime, f_uptime, f_admin, f_target_gameaddr,
                f_card_endtime, f_passwd, f_owner, f_service_fee_rate, f_insstate, 
                f_sub_table_type, f_auto_blind, f_bott_pre_bbtimes, f_pump_rate,
                f_box_limit_chips, f_box_service_rate, f_apply_buyin_open, f_pt_pot_open,
                f_card_compare_type, f_pk_first_bet, f_redu_chip_flag)
            values (%s, %s, %s, %s,
                   %s, %s, %s, %s,
                   %s, %s, %s, %s,
                   %s, %s, %s, %s,
                   %s, %s, %s, %s,
                   %s, %s, %s, %s,
                   now(), now(), %s, %s,
                   %s, %s, %s, %s, %s, %s, 
                   %s, %s, %s, %s, %s, %s, 
                   %s, %s, %s, %s)'''
    args = (name, seat_num, level, pay_type,
            1, min_coins, max_coins, antedefault,
            big_blind, small_blind, big_blind, rake_before_flop,
            0, 0, waittime, "YES",
            "YES", holdtime, reentertime, entrusttimes,
            1, 1, "YES", match_addr,
            "sys", target_gameaddr,
            card_endtime, passwd, owner, service_fee_rate, 
            insstate, sub_table_type, auto_blind, bott_pre_bbtimes, 
            pump_rate, redu_chip_limit, redu_chip_service_rate, 
            int(apply_buyin_open), int(pt_pot_open), 
            int(card_compare_type), int(pk_first_bet), int(redu_chip_flag))
    cash_id = Db.Mysql.connect('esun_texas').insert(sql, args)
    return cash_id


def get_auto_buy_info(subtype):
    sql = '''select buy_type BUY_TYPE, buy_money BUY_MONEY, card_id CARD_ID from t_auto_buy_card where sub_type = %s'''
    args = (subtype)
    res = Db.Mysql.connect('esun_texas').query(sql, args)
    return res

def insert_create_table_comsump(config_id, subtype, user_id, comsump_type):
    '''
    插入朋友局创建房间时实际的消耗
    '''
    logging.info('********** insert_create_table_comsump bg, subtype:%s, comsump_type:%s', 
        str(subtype), str(comsump_type))
    #if int(subtype) == 0:
    #    logging.info('********** insert_create_table_comsump , subtype = 0')
    #    return 0

    buy_type = comsump_type
    buy_money = 0
    card_id = 0
    logging.info('********** get_auto_buy_info bg')
    ret = get_auto_buy_info(subtype)
    logging.info('********** get_auto_buy_info ret:%s', str(ret))
    buy_type = ret[0]['BUY_TYPE']
    buy_money = ret[0]['BUY_MONEY']
    card_id = ret[0]['CARD_ID']
    if int(comsump_type) > 1:
        # 通过货币创建房间
        card_id = 0

    sql = '''insert into t_create_room_log(config_id, sub_type, owner_id, pay_type, pay_number, card_id)
                values(%s, %s, %s, %s, %s, %s)'''
    args = (config_id, int(subtype), user_id, int(comsump_type), buy_money, card_id)
    idx = Db.Mysql.connect('esun_texas').insert(sql, args)
    return idx

def back_user_createroom_card(user_id, card_id):
    '''
    返回用户开房卡
    '''
    db = Db.Mysql.connect('esun_texas')
    # 获取用户已获得的道具信息
    sql = '''select f_id USER_PROPS_ID from t_user_props where f_uid = %s and f_props_id = %s and f_status = 'INUSE' '''
    args = (int(user_id), int(card_id))
    logging.info('**** back_user_createroom_card, sql:%s, args:%s', str(sql), str(args))
    ret1 = db.query( sql, args )
    numb = 1

    if len(ret1) == 0:
        #插入
        sql = '''
                 select f_props_id              PROPS_ID,
                        f_props_name            PROPS_NAME,
                        f_desc                  PROPS_DESC,
                        f_group                 PROPS_GROUP,
                        f_img_url               IMG_URL,
                        f_is_instant_use        IS_INSTANT_USE,
                        f_func_args             FUNC_ARGS,
                        f_props_limit           PROPS_LIMIT,
                        f_allow_add             ALLOW_ADD,
                        f_examine               EXAMINE
                 from   t_props_config
                 where f_props_id = %s
              '''

        params = (card_id)
        ret2 = db.query( sql, params )
        if (len(ret2) > 0):
            prop_info = ret2[0]

        props_args = [user_id,  prop_info['PROPS_ID'],  prop_info['PROPS_NAME'],  prop_info['PROPS_GROUP'],
                prop_info['IMG_URL'],   '',   numb,        'INUSE',
                prop_info['FUNC_ARGS'], 'YES',       prop_info['PROPS_DESC'], '' ]  
        ''' 插入玩家道具表 '''
        sql = ''' 
                  insert into t_user_props
                  (f_uid, f_props_id, f_props_name, f_group, f_img_url, f_props_limit, f_props_nums, f_status, f_func_args, f_allow_add, f_desc, f_instime, f_uptime, f_remark)
                  values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now(), now(), %s)
              '''
        pOther = props_args
        db.insert(sql, pOther)
        db.commit()
        return 1
    else:
        sql = '''
                 update t_user_props
                    set f_props_nums = f_props_nums + %s,
                        f_uptime     = now(),
                        f_instime    = now()
                  where f_id = %s
              '''
        args = [numb, ret1[0]['USER_PROPS_ID']]
        db.execute(sql, args)
        db.commit()
        return 1


def is_unback_chip_cash_table(config_id):
    '''
    根据配置id，判断是否需要立即返筹码
    '''
    db = Db.Mysql.connect('esun_texas')
    sql = '''select f_owner TABLE_OWNER, 
                    f_sub_table_type TABLE_SUB_TYPE from t_cash_table_config where f_id = %s'''
    args = (int(config_id))
    ret = db.query( sql, args )

    if len(ret) > 0:
        if (ret[0]['TABLE_OWNER'] == None):
            return 0
        if (ret[0]['TABLE_SUB_TYPE'] == None):
            return 0
        if (len(ret[0]['TABLE_OWNER']) == 0):
            return 0
        if (ret[0]['TABLE_OWNER'] == 'sys'):
            return 0
        if (int(ret[0]['TABLE_SUB_TYPE']) == 3):
            # 自定义卡
            return 0

        return 1
    return 0

def get_cash_table_pump_rate(config_id):
    '''
        根据配置id，获取子类型与抽水比例
    '''
    db = Db.Mysql.connect('esun_texas')
    sql = '''select f_pump_rate PUMP_RATE from t_cash_table_config where f_id = %s'''
    args = (int(config_id))
    ret = db.query( sql, args )    

    if len(ret) > 0:
        if (ret[0]['PUMP_RATE'] == None):
            return 0

        return int(ret[0]['PUMP_RATE'])

    return 0


def get_buyin_info(userid, tableid, dbconn=None):
    '''  获取现金桌玩家信息 '''
    dbconn = Db.Mysql.connect('esun_texas')
    sql = '''
            SELECT  a.f_match_addr match_addr,
                    a.f_id player_id,
                    a.f_username username,
                    a.f_chips chips,
                    b.f_pay_type pay_type,
                    a.f_min_buyin act_min_chips,
                    a.f_max_buyin act_max_chips,
                    a.f_chips_sitout sitout_chips,
                    b.f_min_coins conf_min_chips,
                    b.f_max_coins conf_max_chips,
                    b.f_play_type play_type, 
                    b.f_owner owner,
                    b.f_service_fee_rate service_fee_rate,
                    b.f_apply_buyin_open apply_buyin_open,
                    b.f_pt_pot_open pt_pot_open  
            FROM    t_cash_player a,
                    t_cash_table_config b,
                    t_cash_table_list c
            WHERE   a.f_uid = %s 
                    AND a.f_table_id = %s 
                    AND a.f_table_id = c.f_id 
                    AND c.f_config_id = b.f_id
          '''
    params = [userid, tableid]
    if not dbconn:
        dbconn = Mysql.connect('esun_texas')
    res = dbconn.query(sql, params)
    return res and res[0] or None