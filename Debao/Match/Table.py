#coding=utf-8
import zlog as logging
import Db.Mysql
from . import Config


def add_match_table( table_id, table_name, match_id,
                        game_addr, seat_num, status, admin='match', adminnote='match' ):
    '''
        ���ܣ��������������
        ��д��chend
        ������2012-2-6 19:37:24
        �޸ģ�
    '''
    sql = ''' insert into t_match_table_list (
                    f_id,
                    f_name,
                    f_match_id,
                    f_serv_addr,
                    f_seat_num,
                    f_status,
                    f_admin,
                    f_adminnote,
                    f_instime,
                    f_uptime
                    ) values ( %s, %s, %s, %s, %s, %s, %s, %s, now(), now() )'''
    args = ( table_id, table_name, match_id, game_addr,
                seat_num, status, admin, adminnote )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def update_match_table_status( status, table_id, match_id ):
    '''
        ���ܣ��������ݿ������¶�Ӧ������״̬
        ��д��chend
        ������2012-2-6 18:00:21
        �޸ģ�
    '''
    sql = ''' update t_match_table_list 
                 set f_status = %s,
                     f_uptime = now()
               where f_id = %s
                 and f_match_id = %s '''
    args = [ status, table_id, match_id ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_match_table_player_cnt( player_cnt, table_id, match_id ):
    '''
        ���ܣ��������ݿ��ж�Ӧ����������
        ��д��chend
        ������2012-2-7 15:09:08
        �޸ģ�
    '''
    sql = ''' update t_match_table_list 
                 set f_player_cnt = %s,
                     f_uptime = now()
               where f_id = %s
                 and f_match_id = %s '''
    args = [ player_cnt, table_id, match_id ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def desc_match_table_player_cnt( player_cnt, table_id, match_id ):
    '''
        ���ܣ��������ݿ��ж�Ӧ����������
        ��д��chend
        ������2012-2-6 20:53:43
        �޸ģ�
    '''
    sql = ''' update t_match_table_list 
                 set f_player_cnt = f_player_cnt - %s,
                     f_uptime = now()
               where f_id = %s
                 and f_match_id = %s
                 and f_player_cnt - %s >= 0 '''
    args = [ player_cnt, table_id, match_id, player_cnt ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def inc_match_table_player_cnt( player_cnt, table_id, match_id ):
    '''
        ���ܣ��������ݿ��ж�Ӧ����������
        ��д��chend
        ������2012-2-6 20:15:05
        �޸ģ�
    '''
    sql = ''' update t_match_table_list 
                 set f_player_cnt = f_player_cnt + %s,
                     f_uptime = now()
               where f_id = %s
                 and f_match_id = %s '''
    args = [ player_cnt, table_id, match_id ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def get_match_table( match_id, status_1 = Config.STATUS_TABLE_OPENED, 
                        status_2 = Config.STATUS_TABLE_PAUSE ):
    '''
        ���ܣ�ȡָ�����µ������б�
        ��д��chend
        ������2012-2-6 17:57:39
        �޸ģ�
    '''
    sql = '''
        select f_id table_id,
               f_name table_name,
               f_match_id match_id,
               f_serv_addr serv_addr,
               f_player_cnt player_cnt,
               f_seat_num seat_num,
               f_status status
          from t_match_table_list
         where f_match_id = %s
           and f_status in (%s, %s)
    '''
    args = [ match_id, status_1, status_2 ]
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret


def delete_match_table( match_id, table_id ):
    '''
        ���ܣ�ɾ��ָ�����µ�����
        ��д��chend
        ������2012-2-7 14:59:59
        �޸ģ�
    '''
    sql = ''' delete from t_match_table_list 
               where f_match_id = %s
                 and f_id = %s '''
    args = [ match_id, table_id ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret



















def inc_cash_table_player_cnt( player_cnt, table_id, cash_id ):
    '''
        ���ܣ��������ݿ��ж�Ӧ����������
        ��д��chend
        ������2012-2-8 17:51:27
        �޸ģ�
    '''
    sql = ''' update t_cash_table_list 
                 set f_player_cnt = f_player_cnt + %s,
                     f_uptime = now()
               where f_id = %s
                 and f_config_id = %s '''
    args = [ player_cnt, table_id, cash_id ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def desc_cash_table_player_cnt( player_cnt, table_id, cash_id ):
    '''
        ���ܣ��������ݿ��ж�Ӧ����������
        ��д��chend
        ������2012-2-13 16:24:18
        �޸ģ�
    '''
    sql = ''' update t_cash_table_list 
                 set f_player_cnt = f_player_cnt - %s,
                     f_uptime = now()
               where f_id = %s
                 and f_config_id = %s
                 and f_player_cnt - %s >= 0 '''
    args = [ player_cnt, table_id, cash_id, player_cnt ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def get_cash_table( cash_id, status=Config.STATUS_TABLE_OPENED ):
    '''
        ���ܣ�ȡָ�����µ������б�
        ��д��chend
        ������2012-2-6 17:57:39
        �޸ģ�
    '''
    sql = '''
        select f_id table_id,
               f_name table_name,
               f_config_id config_id,
               f_serv_addr serv_addr,
               f_player_cnt player_cnt,
               f_seat_num seat_num,
               f_hands_num hands_num,
               f_status status,
               f_show is_show
          from t_cash_table_list
         where f_config_id = %s
           and f_status = %s
    '''
    args = [ cash_id, status ]
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    return ret

def add_cash_table( table_id, table_name, cash_id, game_addr,
                    seat_num, status, admin='match', adminnote='match' ):
    '''
        ���ܣ��������������
        ��д��chend
        ������2012-2-6 19:37:24
        �޸ģ�
    '''
    sql = ''' insert into t_cash_table_list (
                    f_id,
                    f_name,
                    f_config_id,
                    f_serv_addr,
                    f_seat_num,
                    f_status,
                    f_admin,
                    f_adminnote,
                    f_instime,
                    f_uptime,
                    f_show,
                    f_examine
                    ) values ( %s, %s, %s, %s, %s, %s, %s, %s, now(), now(), 'YES', 'YES' )'''
    args = ( table_id, table_name, cash_id, game_addr,
                seat_num, status, admin, adminnote )
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def update_cash_table_player_cnt( player_cnt, table_id, cash_id ):
    '''
        ���ܣ��������ݿ��ж�Ӧ����������
        ��д��chend
        ������2012-2-8 18:21:03
        �޸ģ�
    '''
    sql = ''' update t_cash_table_list 
                 set f_player_cnt = %s,
                     f_uptime = now()
               where f_id = %s
                 and f_config_id = %s '''
    args = [ player_cnt, table_id, cash_id ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_cash_table_playercnt_and_handsnum( player_cnt, hands_num, table_id ):
    '''
        ���ܣ��������ݿ��ж�Ӧ����������
        ��д��chend
        ������2012-2-8 18:21:03
        �޸ģ�
    '''
    sql = ''' update t_cash_table_list 
                 set f_player_cnt = %s,
                     f_hands_num = %s,
                     f_uptime = now()
               where f_id = %s '''
    args = [ player_cnt, hands_num, table_id ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def update_cash_table_show( is_show, table_id ):
    '''
        ���ܣ��������ݿ��ж�Ӧ����������
        ��д��chend
        ������2012-2-8 18:21:03
        �޸ģ�
    '''
    sql = ''' update t_cash_table_list 
                 set f_show = %s,
                     f_uptime = now()
               where f_id = %s '''
    args = [ is_show, table_id ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


def inc_cash_table_wait_num(table_id, cnt=1):
    '''
        ���ܣ��������ݿ��ж�Ӧ�����ĵȴ�����
        ��д��chend
        ������2012-3-21 10:42:43
        �޸ģ�
    '''
    sql = ''' update t_cash_table_list 
                 set f_wait_num = f_wait_num + %s,
                     f_uptime = now()
               where f_id = %s '''
    args = [ cnt, table_id ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret

def desc_cash_table_wait_num(table_id, cnt=1):
    '''
        ���ܣ��������ݿ��ж�Ӧ�����ĵȴ�����
        ��д��chend
        ������2012-3-21 10:43:11
        �޸ģ�
    '''
    sql = ''' update t_cash_table_list 
                 set f_wait_num = f_wait_num - %s,
                     f_uptime = now()
               where f_id = %s
                 and f_wait_num - %s >= 0'''
    args = [ cnt, table_id, cnt ]
    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


#
# ���ܣ�����������Ŀ���Լ����ϵ�����
# ��Σ�
#       player_count    ����������
#       max_seat_num    ÿ������������
# ���Σ�
#       result = [
#           {
#               'table_count' : ����,
#               'people_per_table' : ��������������,
#           },
#           ...
#       }
# ��д��chend
# ���ڣ�2011-12-28 18:17:54
# �޸ģ���
#
def count_tables( player_count, max_seat_num=9 ):

    result = []

    quotient = player_count/max_seat_num
    rest     = player_count%max_seat_num

    if 0 == rest:
        tmp = {
            'table_count' : quotient,
            'people_per_table' : max_seat_num,
        }

        result.append( tmp )

    else :
        i = 1
        quotient = player_count/(max_seat_num-1)
        rest     = player_count%(max_seat_num-1)
        while quotient < rest :
            i += 1
            quotient = player_count/(max_seat_num-i)
            rest     = player_count%(max_seat_num-i)
            

        tmp = {
            'table_count' : rest,
            'people_per_table' : max_seat_num-(i-1),
        }
        result.append( tmp )
        tmp = {
            'table_count' : quotient - rest,
            'people_per_table' : max_seat_num-i,
        }
        result.append( tmp )



    #for tmp in result:
    #    print "[%s]��[%s]����"%( tmp['table_count'], tmp['people_per_table'] )

    return result



# ��ȡ��tableid
# ����x��yʱ�䴴���ĵ�a��b����
def get_new_tableid( match_id, x, y ):
    import time
    
    tableid = str(match_id) + str( int(time.time()) ) + str(x) + str(y)

    return tableid

# ����tableid
# ÿ������(2λ) + ����(4λ) + �������� + ����ID
def make_table_id( match_id, match_type, seat_num, cnt ):
    import time

    str_seat_num = str(seat_num).zfill(2)
    str_cnt      = str(cnt).zfill(4)
    
    tableid  = str( int(time.time()) ) + str_seat_num + str_cnt + match_type + str(match_id) 

    return tableid

def insert_table_chips_log(ins_player_group, remark=''):
    sql = '''
    INSERT INTO t_table_chips_log
   (`f_table_type`, `f_match_id`, `f_config_id`, `f_pay_type`, `f_table_id`,
    `f_player_id_0`, `f_uid_0`, `f_username_0`, `f_ante_0`, `f_user_rake_0`, `f_putin_chips_0`, `f_get_chips_0`, `f_chips_0`,
    `f_player_id_1`, `f_uid_1`, `f_username_1`, `f_ante_1`, `f_user_rake_1`, `f_putin_chips_1`, `f_get_chips_1`, `f_chips_1`,
    `f_player_id_2`, `f_uid_2`, `f_username_2`, `f_ante_2`, `f_user_rake_2`, `f_putin_chips_2`, `f_get_chips_2`, `f_chips_2`, 
    `f_player_id_3`, `f_uid_3`, `f_username_3`, `f_ante_3`, `f_user_rake_3`, `f_putin_chips_3`, `f_get_chips_3`, `f_chips_3`, 
    `f_player_id_4`, `f_uid_4`, `f_username_4`, `f_ante_4`, `f_user_rake_4`, `f_putin_chips_4`, `f_get_chips_4`, `f_chips_4`, 
    `f_player_id_5`, `f_uid_5`, `f_username_5`, `f_ante_5`, `f_user_rake_5`, `f_putin_chips_5`, `f_get_chips_5`, `f_chips_5`, 
    `f_player_id_6`, `f_uid_6`, `f_username_6`, `f_ante_6`, `f_user_rake_6`, `f_putin_chips_6`, `f_get_chips_6`, `f_chips_6`, 
    `f_player_id_7`, `f_uid_7`, `f_username_7`, `f_ante_7`, `f_user_rake_7`, `f_putin_chips_7`, `f_get_chips_7`, `f_chips_7`, 
    `f_player_id_8`, `f_uid_8`, `f_username_8`, `f_ante_8`, `f_user_rake_8`, `f_putin_chips_8`, `f_get_chips_8`, `f_chips_8`, 
    `f_pot`, `f_rake`, `f_hand_id`, `f_instime`, `f_remark`)
VALUES
   (%s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, now(), %s)
    '''
    args = list()
    args.append( ins_player_group.table_type )
    args.append( ins_player_group.match_id )
    args.append( ins_player_group.config_id )
    args.append( ins_player_group.pay_type )
    args.append( ins_player_group.table_id )
    for seat_pos in range(9):
        player = ins_player_group.player_list[seat_pos]
        args.append( player.player_id )
        args.append( player.user_id )
        args.append( player.user_name )
        args.append( player.ante )
        args.append( player.user_rake )
        args.append( player.putin_chips )
        args.append( player.get_chips )
        args.append( player.chips )
    
    args.append( ins_player_group.pot )
    args.append( ins_player_group.rake )
    args.append( ins_player_group.hand_id )
    args.append( remark )

    ret = Db.Mysql.connect('esun_texas').execute(sql, args)
    return ret


class player_info:
    def __init__(self):
        self.player_id      = None
        self.user_id        = None
        self.user_name      = None
        self.ante           = 0
        self.user_rake      = 0
        self.putin_chips    = 0
        self.get_chips      = 0
        self.chips          = 0

class player_group:
    def __init__(self, table_type, match_id, config_id, pay_type, table_id, pot, rake, hand_id):
        self.table_type     = table_type
        self.match_id       = match_id
        self.config_id      = config_id
        self.pay_type       = pay_type
        self.table_id       = table_id
        self.player_list    = {}
        for i in range(9):
            player = player_info()
            self.player_list[i] = player
        self.pot            = pot
        self.rake           = rake
        self.hand_id        = hand_id

    def add_player(self, seat_num, player_id, user_id, user_name,
        ante, user_rake, putin_chips, get_chips, chips):
        i = int(seat_num)
        if i < 0 or i > 8:
            logging.error( "add player_group error! wrong seat_num %s"%i )
            return False
        self.player_list[i].player_id   = player_id
        self.player_list[i].user_id     = user_id
        self.player_list[i].user_name   = user_name
        self.player_list[i].ante        = ante
        self.player_list[i].user_rake   = user_rake
        self.player_list[i].putin_chips = putin_chips
        self.player_list[i].get_chips   = get_chips
        self.player_list[i].chips       = chips

