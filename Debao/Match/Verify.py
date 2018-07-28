#coding=gbk
import Db.Mysql
import traceback
import zlog as logging

def get_table_config_id(table_id):
    '''
        ��ȡĳһ��������ID,���ڲ�t_cash_table_config��
        ��Σ�table_id
        ���Σ�config_id    ����id [{'config_id':34}]
        ��д��liulk
        ���ڣ�2012-06-19 14:20:44
    '''
    sql = '''SELECT  f_config_id config_id
                FROM t_cash_table_list
               WHERE f_id = %s'''
    args = ( table_id, )
    config_id = Db.Mysql.connect('esun_texas').query(sql, args)
    return config_id

    
    
    
def get_permission_index(config_id):
    '''
        #��t_cash_table_config��
        #��ȡȨ����������λ��t_cash_table_conf������һ���ֶ�
            name   :    f_permission_idx
            type   :    int
            example:    1
        ��Σ�config_id ����id
        ���Σ�index
        ��д��liulk
        ���ڣ�2012-06-19 12:30:04
        �޸ģ���
    '''
    sql = '''SELECT f_permission_idx p_index 
                FROM t_cash_table_config
               WHERE f_id = %s'''
    args = ( config_id, )
    index = Db.Mysql.connect('esun_texas').query(sql, args)
    
    #[{'p_index':1}]
    return index

    
    
def get_permission_rules( index ):
    '''
            �����ֶ����б�˳��ȡ��Ӧ�ֶ�ֵ
            ע�⣺��ǰֻ����ע��������ע��ʱ�䣬û�м���VIP�ȼ���IP������
        ��Σ�field_name_list
                field_name_list = ['f_channel_rules', 'f_time_rules']
        ���Σ�rules_dic �磬{ 'f_time_rules:'1,2,3', 'f_channel_rules':'1,3,5' }
        ��д��liulk
        ʱ�䣺2012-06-19 15:27:34
        �޸ģ���
    '''    
    rules_dic = {}
    
    #������Ϊ0����ʾ������Ȩ������
    if index == 0:
        return rules_dic

    sql = '''SELECT  f_channel_rules,
                     f_time_rules,
                     f_white_list,
                     f_charge,
                     f_ladder_point,
                     f_vip_level
                FROM t_permission_rule
               WHERE f_permission_idx = %s'''
    args = ( index )
        
    rules_dic = Db.Mysql.connect('esun_texas').query(sql, args)
    if len( rules_dic ) == 0:
        return None
    else:
        return rules_dic[0]


    
def db_get_regchannel(index):
    '''
        ��index��ȡ���������
    ��Σ�index���� 3
    ���Σ�result �� [{'channel':'500pai'}]
    ��д��liulk
    ʱ�䣺2012-06-20 10:58:21
    �޸ģ���
    '''
    sql = '''SELECT  f_register_channel channel
                FROM t_channel_rule
               WHERE f_permission_idx = %s'''
    args = (index, )
    result = Db.Mysql.connect('esun_texas').query(sql, args)
    
    if len( result ) == 0:
        return None
    else:
        return result[0]

    
            
def get_specific_channel(index):
    '''
        ��index��ȡ���������
    ��Σ�index���� 3
    ���Σ�channel �� '500pai'
    ��д��liulk
    ʱ�䣺2012-06-20 10:58:21
    �޸ģ�2012-07-16 11:00:43
    '''    
    #channel = db_get_regchannel(index).get('channel')
    channel = db_get_regchannel(index)
    if channel == None:
        return channel
    else:
        return channel.get('channel')
        
        
def get_limited_channel_list(code_list):
    '''
        ��ȡ��������ľ���ע������
    ��Σ��������Ʊ�ţ���'1,3,4'
          ע�⣺','ǰ�����пո񣡣���
          
    ���Σ������б���["500wan", "500pai", "1000wan"]
    ��д��liulk
    ʱ�䣺2012-06-20 10:18:43
    �޸ģ���
    '''
    #�ö��ŷָ��ַ���
    #���Ч����channel_list = ['1', '3', '4']
    code_list = code_list.split( ',' )

    channel_list = []
    
    for value in code_list:
        arg = int(value)
        ret = get_specific_channel( arg )
        if ret == None:
            continue
        #����ѯ����������Ϣ���������б�
        channel_list.append(ret)
    
    return channel_list



def db_get_time_section(index):
    '''
        ��ȡһ��ʱ���
    ��Σ�index
    ���Σ�result ��{'lower':0, 'upper':30}
    ��д��liulk
    ʱ�䣺2012-06-21 12:11:43
    '''
    sql = '''SELECT  f_lower_limit lower,
                     f_upper_limit upper
                FROM t_time_rule
               WHERE f_permission_idx = %s'''
    args = (index, )
    result = Db.Mysql.connect('esun_texas').query(sql, args)
    if len( result ) == 0:
        return None
    else:
        return result[0]
    
    
    
    
def get_specific_time_section(index):
    '''
        ��ȡһ��ʱ������ƣ���(0,30)
    ��Σ�������
    ���Σ�result 
    ��д��llk
    ʱ�䣺2012-06-21 12:07:23
    '''
    time_section = []
    #ret = {'lower':0, 'upper':30}
    ret = db_get_time_section(index)
    if ret == None:
        return time_section
    
    time_section.append(ret.get('lower'))
    time_section.append(ret.get('upper'))
    
    #���ظ�ʽ[0,30]
    return time_section    
                
                
                
def get_limited_time_list(code_list):
    '''
        ��ȡ��������ľ���ע��ʱ��
        ��(30,90)��ʾע��ʱ����30--90��֮������
    ��Σ�ʱ�����Ʊ�ţ��确2,3��
    ���Σ�time_list ��[[30,90], [90, 120]]
    '''
    code_list = code_list.split(',')
    
    time_list = []
    for value in code_list:
        ret = get_specific_time_section( int(value) )
        if len( ret ) == 0:
            continue
        else:
            time_list.append(ret)
    
    return time_list
        
        
        
def get_user_regchannel(user_id):        
    '''
        ��ȡ�û�ע������
    ��Σ�user_id
    ���Σ�user_regchannel �û�ע������
    ��д��liulk
    ʱ�䣺2012-06-20 11:56:34
    '''
    sql = '''SELECT  f_regchannel channel
                FROM t_user_info
               WHERE f_id = %s'''
    args = (user_id, )
    user_regchannel = Db.Mysql.connect('esun_texas').query(sql, args)
    #ֻ��1����¼�����б���ȡ�����ֵ�
    return user_regchannel[0]
        
        
def get_user_regtime(user_id):        
    '''
        ��ȡ�û�ע��ʱ��
    ��Σ�user_id
    ���Σ�user_regtime �û�ע��ʱ�� {'time':'2012-02-06 16:10:16'}
    ��д��liulk
    ʱ�䣺2012-06-20 11:56:34
    '''
    sql = '''SELECT  f_regtime time
                FROM t_user_info
               WHERE f_id = %s'''
    args = (user_id, )
    user_regtime = Db.Mysql.connect('esun_texas').query(sql, args)    
    #ֻ��1����¼�����б���ȡ�����ֵ�
    return user_regtime[0]
        
        
def get_white_list(list_name):
    '''
        ��ȡ���°�����
    '''
    sql = '''select f_user_id user_id
              from t_match_white_list
              where f_name = %s'''
    args = (list_name, )
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    
    if not ret:
        logging.error('no white_list info %s'%list_name)
        return []
    uid_list = []
    try:
        for i in ret:
            uid_list.append( str(i['user_id']) )
        return uid_list
    except:
        logging.error('%s'%traceback.format_exc())
        return  []
        
def get_user_charg_info(user_id):
    '''
        ��ȡ�û���ֵ��¼
        Ŀǰֻ��ѯ�û��Ƿ���ֵ
    '''
    charge_num = 0
    db = Db.Mysql.connect('esun_texas')
    sql = '''select sum(f_charge_number) num
              from t_user_charging_order_bak 
              where f_uid = %s 
              and f_order_status = "SUC"
          '''
    args = (user_id, )
    ret = db.query(sql, args)
    try:
        if not ret[0]['num']:
            return 0
        if int(ret[0]['num']) > 0:
            charge_num += int(ret[0]['num'])
    except:
        logging.error('%s'%traceback.format_exc())
        return 0
    #û�в鵽���ٲ�ѯ  
    sql2 = '''select sum(f_charge_number) num
              from t_user_charging_order
              where f_uid = %s 
              and f_order_status = "SUC"
          '''
    ret2 = db.query(sql2, args)
    try:
        if int(ret2[0]['num']) > 0:
            charge_num += int(ret[0]['num'])        
    except:
        logging.error('%s'%traceback.format_exc())
        return 0
        
    return charge_num
        
def get_user_ladder_point(user_id):
    '''
        ��ȡ������ݻ���
    '''
    sql = '''select f_rank ladder_point
              from t_user_exp_rank
              where f_uid = %s'''
    args = (user_id, )
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    if not ret:
        return 0
    else:
        try:
            return int( ret[0]['ladder_point'] )
        except:
            logging.error('%s'%traceback.format_exc())
            return  0
        
def get_user_vip_level(user_id):
    '''
        ��ȡ���vip�ȼ�
    '''
    sql = '''select f_level vip_level
              from t_user_vip
              where f_uid = %s  '''
    args = (user_id, )
    ret = Db.Mysql.connect('esun_texas').query(sql, args)
    if not ret:
        return 0
    else:
        try:
            return int( ret[0]['vip_level'] )
        except:
            logging.error('%s'%traceback.format_exc())
            return  0
    
