#coding=utf-8
import zlog as logging
import Db.Mysql
from . import Config
import Memory



def add_succ_enter_player ( table_id, user_id):
    '''
        ���ܣ��� t_table_succ_user_enter ����ɹ����������
    '''
    sql = '''insert into t_table_succ_user_enter (table_id, user_id)
                values (%s, %s)'''
    args = (table_id, user_id)
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    
    return ret


def add_match_player( user_id, user_name, match_type, match_id, table_id,
                seat_pos, chips, status, match_rank, remark='' ):
    '''
        ���ܣ�����t_match_player��, ����f_id
        ��д��chend
        ������2012-2-6 19:56:34
        �޸ģ�
    '''
    sql = ''' insert into t_match_player (
                    f_uid,
                    f_username,
                    f_match_type,
                    f_match_id,
                    f_table_id,
                    f_seat_pos,
                    f_chips,
                    f_status,
                    f_match_rank,
                    f_instime,
                    f_uptime,
                    f_remark) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, now(), now(), %s )'''
    args = ( user_id, user_name, match_type, match_id, table_id, seat_pos, chips,
                status, match_rank, remark )
    playerid = Db.Mysql.connect('esun_texas').insert(sql, args)
    
    # sql = '''
        # select f_id playerid from t_match_player where f_table_id = %s and f_seat_pos = %s
    # '''
    # args = ( table_id, seat_pos )
    # cur = Db.Mysql.connect('esun_texas').query(sql, args)
    # playerid = cur[0]['playerid']

    return playerid

def update_match_player_position( player_id, user_id, table_id, seat_pos, chips, status ):
    '''
        ���ܣ�������ҵ�λ��
        ��д��chend
        ������2012-2-6 20:10:40
        �޸ģ�
    '''
    sql = ''' update t_match_player
                 set f_table_id = %s,
                     f_seat_pos = %s,
                     f_chips = %s,
                     f_status = %s,
                     f_uptime = now()
               where f_id = %s
                 and f_uid = %s'''
    args = ( table_id, seat_pos, chips, status, player_id, user_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def delete_player( user_id, match_id, table_id, status ):
    '''
        ���ܣ���t_player����ɾ������status�����
        ��д��chend
        ������2012-1-11 11:04:28
        �޸ģ�
    '''
    sql = ''' delete from t_player
               where f_uid = %s
                 and f_match_id = %s
                 and f_table_id = %s
                 and f_status = %s '''
    args = ( user_id, match_id, table_id, status )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def update_player_status_rank( user_id, match_id, table_id, status, rank ):
    '''
        ���ܣ�������ҵ�״̬������
        ��д��chend
        ������2012-1-11 11:40:53
        �޸ģ�
    '''
    sql = ''' update t_match_player
                 set f_status = %s,
                     f_match_rank = %s,
                     f_uptime = now()
               where f_uid = %s
                 and f_match_id = %s
                 and f_table_id = %s'''
    args = ( status, rank, user_id, match_id, table_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_player_chips( user_id, match_id, table_id, chips ):
    '''
        ���ܣ�������ҵĳ���
        ��д��chend
        ������2012-1-11 11:40:53
        �޸ģ�
    '''
    sql = ''' update t_match_player
                 set f_chips = %s,
                     f_uptime = now()
               where f_uid = %s
                 and f_match_id = %s
                 and f_table_id = %s'''
    args = ( chips, user_id, match_id, table_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def update_match_player_status( user_id, match_id, table_id ):
    '''
        ���ܣ��������״̬
        ��д��chend
        ������2012-1-11 11:40:53
        �޸ģ�
    '''
    sql = ''' update t_match_player
                 set f_status = %s,
                     f_uptime = now()
               where f_uid = %s
                 and f_match_id = %s
                 and f_table_id = %s'''
    args = ( 'ELIMINATED', user_id, match_id, table_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args) 
    return ret
    
def delete_match_player( match_id ):
    '''
        ���ܣ���t_match_player����ɾ��ָ������id�����
        ��д��chend
        ������2012-2-6 18:06:15
        �޸ģ�
    '''
    sql = ''' delete from t_match_player
               where f_match_id = %s '''
    args = ( match_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def get_match_player_by_tableid( match_id, table_id ):
    '''
        ���ܣ�ȡ��ָ�����¡�����id�����
        ��д��chend
        ������2012-2-6 18:59:19
        �޸ģ�
    '''
    sql = '''SELECT f_id player_id,
                    f_uid user_id,
                    f_username user_name,
                    f_match_id match_id,
                    f_table_id table_id,
                    f_seat_pos seat_pos,
                    f_chips chips,
                    f_hand_num hand_num,
                    f_status status,
                    f_match_rank rank
               from t_match_player
              where f_match_id = %s
                and f_table_id = %s '''
    args = ( match_id, table_id )
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret

def get_match_out_players( match_id ):
    '''
        ���ܣ�ȡ��ָ�����µ���̭���
        ��д��chend
        ������2012-3-24 19:30:14
        �޸ģ�
    '''
    sql = '''SELECT f_uid user_id,
                    f_username user_name,
                    f_match_rank rank
               from t_match_player
              where f_match_id = %s
                and f_status = %s '''
    args = ( match_id, Config.STATUS_PLAYER_ELIMINATED )
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret

def record_match_player_status( player_id, hand_num ):
    '''
        ���ܣ��Ǽ���ҵ�������
        ��д��chend
        ������2012-2-21 14:48:08
        �޸ģ�
    '''
    sql = ''' update t_match_player
                 set f_hand_num = f_hand_num + %s,
                     f_uptime = now()
               where f_id = %s'''
    args = ( hand_num, player_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret
    
    









def add_cash_player( user_id, user_name, match_addr, table_id, pay_type,
                seat_pos, chips, min_buyin, max_buyin, status, chips_sitout, remark='' ):
    '''
        ���ܣ�����t_cash_player��, ����f_id
        ��д��chend
        ������2012-2-6 19:56:34
        �޸ģ�
    '''
    sql = ''' insert into t_cash_player (
                    f_uid,
                    f_username,
                    f_match_addr,
                    f_table_id,
                    f_pay_type,
                    f_seat_pos,
                    f_chips,
                    f_min_buyin,
                    f_max_buyin,
                    f_status,
                    f_remark,
                    f_instime,
                    f_uptime,
                    f_buyin,
                    f_cashout,
                    f_chips_sitout) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now(), now(), 0, 0, %s )'''
    args = ( user_id, user_name, match_addr, table_id, pay_type,
                seat_pos, chips, min_buyin, max_buyin, status, remark, chips_sitout )
    db = Db.Mysql.connect('esun_texas')
    ret = db.insert(sql, args)
    db.commit()
    
    # sql = '''
        # select f_id playerid from t_cash_player where f_table_id = %s and f_seat_pos = %s
    # '''
    # args = ( table_id, seat_pos )
    # cur = Db.Mysql.connect('esun_texas').query(sql, args)
    
    
    # playerid = cur[0]['playerid']

    return ret


def get_cash_player_by_tableid( table_id ):
    '''
        ���ܣ�ȡ��ָ���ֽ���������id�����
        ��д��chend
        ������2012-2-8 10:59:25
        �޸ģ�
    '''
    sql = '''SELECT f_id player_id,
                    f_uid user_id,
                    f_username user_name,
                    f_table_id table_id,
                    f_seat_pos seat_pos,
                    f_chips chips,
                    f_hand_num hand_num,
                    f_rake rake,
                    f_status status
               from t_cash_player
              where f_table_id = %s '''
    args = ( table_id )
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret

def update_cash_player_chips( player_id, user_id, table_id, chips,
                                status=Config.STATUS_PLAYER_PLAYING ):
    '''
        ���ܣ�������ҵĳ���
        ��д��chend
        ������2012-2-8 18:16:50
        �޸ģ�2012-2-9 15:12:02 �����ֶΣ�״̬
    '''
    sql = ''' update t_cash_player
                 set f_chips = %s,
                     f_status = %s,
                     f_uptime = now()
               where f_id = %s
                 and f_uid = %s
                 and f_table_id = %s'''
    args = ( chips, status, player_id, user_id, table_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def update_cash_player_fin_chips( player_id, user_id, table_id, chips,
                                status=Config.STATUS_PLAYER_PLAYING ):
    '''
        ���ܣ�������ҵĳ���
        ��д��chend
        ������2012-2-8 18:16:50
        �޸ģ�2012-2-9 15:12:02 �����ֶΣ�״̬
    '''
    sql = ''' update t_cash_player_finish
                 set f_chips = %s,
                     f_status = %s,
                     f_uptime = now()
               where f_id = %s
                 and f_uid = %s
                 and f_table_id = %s'''
    args = ( chips, status, player_id, user_id, table_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def add_cash_player_chips( player_id, user_id, table_id, chips ):
    '''
        ���ܣ������ҵĳ���
        ��д��chend
        ������2012-2-9 15:43:26
        �޸ģ�
    '''
    sql = ''' update t_cash_player
                 set f_chips = f_chips + %s,
                     f_uptime = now()
               where f_id = %s
                 and f_uid = %s
                 and f_table_id = %s'''
    args = ( chips, player_id, user_id, table_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def finish_cash_player( player_id ):
    '''
        ���ܣ��ƶ�ָ����ҵ���ɱ���
        ��д��chend
        ������2012-2-9 15:07:18
        �޸ģ�
    '''
    
    logging.info( 'move to t_cash_player_finish[%s]'%player_id )
    
    sql_insert = '''
        insert into t_cash_player_finish select * from t_cash_player where f_id =%s
    '''
    sql_delete = '''
        delete from t_cash_player where f_id = %s
    '''
    args = ( player_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql_insert, args)
    args = ( player_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql_delete, args)
    return ret





def insert_chips_log( player_id, user_id, user_name, table_type, match_id, table_id, pay_type,
    inout, busisort, chips, balance_chips, orderid, hand_id, remark='' ):
    '''
        ���ܣ�������ҳ�����ˮ��
        ��д��chend
        ������2012-2-4 14:39:27
        �޸ģ�2012-2-6 20:36:23 �±�
    '''
    #remark = remark.decode("gbk").encode("utf-8") 
    sql = ''' insert into t_player_chips_log (
                    f_player_id,
                    f_uid,
                    f_username,
                    f_table_type,
                    f_match_id,
                    f_table_id,
                    f_pay_type,
                    f_inout,
                    f_busisort,
                    f_chips,
                    f_balance_chips,
                    f_orderid,
                    f_hand_id,
                    f_remark,
                    f_instime) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now() )'''
    args = ( player_id, user_id, user_name, table_type, match_id, table_id,
    pay_type, inout, busisort, chips, balance_chips, orderid, hand_id, remark )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def batch_insert_chips_log( chips_log_list ):
    '''
        ���ܣ�����������ҳ�����ˮ��
        ��д��chend
        ������2012-2-7 18:02:21
        �޸ģ�
    '''
    sql = ''' insert into t_player_chips_log (
                    f_player_id,
                    f_uid,
                    f_username,
                    f_table_type,
                    f_match_id,
                    f_table_id,
                    f_pay_type,
                    f_inout,
                    f_busisort,
                    f_chips,
                    f_balance_chips,
                    f_orderid,
                    f_hand_id,
                    f_remark,
                    f_instime) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now() )'''

    ret = Db.Mysql.connect('esun_texas').executeMany(sql, chips_log_list)
    return ret


def insert_cash_wait_list( table_id, user_id, user_name ):
    '''
        ���ܣ�������ҵȴ����б�
        ��д��chend
        ������2012-2-14 14:00:09
        �޸ģ�
    '''
    
    sql = ''' insert into t_cash_table_waitlist (
                    f_table_id,
                    f_uid,
                    f_username,
                    f_instime) values ( %s, %s, %s, now() )'''
    args = ( table_id, user_id, user_name )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def remove_cash_wait_list( table_id, user_id, user_name ):
    '''
        ���ܣ��Ƴ���ҵȴ����б�
        ��д��chend
        ������2012-2-14 15:55:52
        �޸ģ�
    '''
    
    sql = ''' delete from t_cash_table_waitlist
               where f_table_id = %s
                 and f_uid = %s '''
    args = ( table_id, user_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def record_cash_player_buyin( player_id, buy_in ):
    '''
        ���ܣ��Ǽ���ҵ��������
        ��д��chend
        ������2012-2-16 10:34:40
        �޸ģ�
    '''
    sql = ''' update t_cash_player
                 set f_buyin = f_buyin + %s,
                     f_uptime = now()
               where f_id = %s'''
    args = ( buy_in, player_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def record_cash_player_cashout( player_id, cash_out ):
    '''
        ���ܣ��Ǽ���ҵĶ��ֳ���
        ��д��chend
        ������2012-2-16 10:37:30
        �޸ģ�
    '''
    sql = ''' update t_cash_player
                 set f_cashout = f_cashout + %s,
                     f_uptime = now()
               where f_id = %s'''
    args = ( cash_out, player_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def record_cash_player_finish_cashout( player_id, cash_out ):
    '''
        ���ܣ��Ǽ�������ҵĶ��ֳ���
        ��д��chend
        ������2012-2-16 10:44:43
        �޸ģ�
    '''
    sql = ''' update t_cash_player_finish
                 set f_cashout = f_cashout + %s,
                     f_uptime = now()
               where f_id = %s'''
    args = ( cash_out, player_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def record_cash_player_status( player_id, hand_num, rake ):
    '''
        ���ܣ��Ǽ���ҵ�����������ˮ
        ��д��chend
        ������2012-2-21 14:48:08
        �޸ģ�
    '''
    sql = ''' update t_cash_player
                 set f_hand_num = f_hand_num + %s,
                     f_rake = f_rake + %s,
                     f_uptime = now()
               where f_id = %s'''
    args = ( hand_num, rake, player_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def record_cash_player_finish_status( player_id, hand_num, rake ):
    '''
        ���ܣ��Ǽ���ҵ�����������ˮ
        ��д��chend
        ������2012-2-21 14:48:08
        �޸ģ�
    '''
    sql = ''' update t_cash_player_finish
                 set f_hand_num = f_hand_num + %s,
                     f_rake = f_rake + %s,
                     f_uptime = now()
               where f_id = %s'''
    args = ( hand_num, rake, player_id )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def check_user_online_status(userid):
    '''
        ��redis������û�������Ϣ�����û��Ƿ�����
        ��Σ�userid
        ���Σ�True, ����
              False, ������
        ��д��liulk
        ���ڣ�2012.08.13  11:33
    '''
    key = Config.USER_ADDR_PREFIX + str(userid)
    user_addr = Memory.getUserConnection( key )
    logging.info('userid: %s, user_addr: %s'%(userid, str(user_addr)))
    if not user_addr:
        return False
    else:
        return True

def get_cash_player_unrecharge_chips(table_id, user_id):
    '''
        ��������id��uid, ��ȡ����ں����ֽ�����û�д����ĳ���
    '''
    sql = ''' select f_pay_type PAY_TYPE, f_cashout CASH_OUT from t_cash_player_finish
            where f_uid = %s and f_table_id = %s order by f_id desc limit 1'''
    args = (int(user_id), table_id)
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret

def get_cash_player_unrecharge_infos(table_id):
    '''
        ��������id, ��ȡ�����ֽ�����û�д����ĳ�����Ϣ
    '''
    sql = ''' select f_id PLAYER_ID, f_uid USER_ID, f_username USER_NAME, 
                     f_pay_type PAY_TYPE, f_cashout CASH_OUT, 0 IS_CHARGED,
                     f_table_id TABLE_ID from t_cash_player_finish a where a.f_id in 
               ( select max(f_id) from t_cash_player_finish where f_table_id = %s and f_cashout > 0 group by f_uid)'''
    args = (table_id)
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret   

def get_player_chips_in_reduce_box(table_id, user_id):
    '''
        ��������id �� uid����ȡ����ڱ������еĳ���
    '''
    sql = '''
            select f_total TOTAL_CHIPS from t_reduce_chips_info 
            where f_tableid = %s and f_userid = %s order by f_id desc limit 1
          '''
    args = (table_id, int(user_id))
    ret = Db.Mysql.connect('esun_texas').query(sql, args)

    if len(ret) == 0:
        return 0

    return int(ret[0]['TOTAL_CHIPS'])     

def get_uncharge_chip_in_reduce_box(table_id):
    '''
        ������ɢʱ�����ػ��б��ܷ�û�н������Ϣ
    '''
    sql = '''
            select f_userid BOX_UID from t_reduce_chips_info where f_tableid = %s group by f_userid
          '''
    args = (table_id)
    ret1 = Db.Mysql.connect('esun_texas').query(sql, args)

    if len(ret1) == 0:
        return ret1

    ret = []

    logging.info('*** get_uncharge_chip_in_reduce_box 1 ret:%s', str(ret1))

    for i in ret1:
        chips = get_player_chips_in_reduce_box(table_id, i['BOX_UID'])
        logging.info('*** get_uncharge_chip_in_reduce_box 2 , tableid:%s, uid:%s, chips:%s', 
            str(table_id), str(i['BOX_UID']), str(chips))
        if (chips > 0):
            # ��������id��uid����ȡ�������player_id
            sql2 = '''
                    select f_id LAST_PLAYER_ID, f_username USER_NAME from t_cash_player_finish 
                    where f_uid = %s and f_table_id = %s order by f_id desc limit 1
                   '''
            args2 = (i['BOX_UID'], table_id)
            ret2 = Db.Mysql.connect('esun_texas').query(sql2, args2)
            logging.info('*** get_uncharge_chip_in_reduce_box 3 ret:%s', str(ret2))
            if len(ret2) == 1:
                logging.info('*** get_uncharge_chip_in_reduce_box 4')
                u_info = {}
                u_info['UID'] = i['BOX_UID']
                u_info['USERNAME'] = ret2[0]['USER_NAME']
                u_info['PLAYER_ID'] = ret2[0]['LAST_PLAYER_ID']
                u_info['BOX_CHIPS'] = chips
                ret.append(u_info)

    logging.info('*** get_uncharge_chip_in_reduce_box ret:%s', str(ret))
    return ret


