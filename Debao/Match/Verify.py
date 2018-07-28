#coding=gbk
import Db.Mysql
import traceback
import zlog as logging

def get_table_config_id(table_id):
    '''
        获取某一桌的配置ID,用于查t_cash_table_config表
        入参：table_id
        出参：config_id    配置id [{'config_id':34}]
        编写：liulk
        日期：2012-06-19 14:20:44
    '''
    sql = '''SELECT  f_config_id config_id
                FROM t_cash_table_list
               WHERE f_id = %s'''
    args = ( table_id, )
    config_id = Db.Mysql.connect('esun_texas').query(sql, args)
    return config_id

    
    
    
def get_permission_index(config_id):
    '''
        #查t_cash_table_config表
        #获取权限限制索引位，t_cash_table_conf表的最后一个字段
            name   :    f_permission_idx
            type   :    int
            example:    1
        入参：config_id 配置id
        出参：index
        编写：liulk
        日期：2012-06-19 12:30:04
        修改：无
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
            根据字段名列表按顺序取相应字段值
            注意：当前只限制注册渠道和注册时间，没有加入VIP等级和IP的限制
        入参：field_name_list
                field_name_list = ['f_channel_rules', 'f_time_rules']
        出参：rules_dic 如，{ 'f_time_rules:'1,2,3', 'f_channel_rules':'1,3,5' }
        编写：liulk
        时间：2012-06-19 15:27:34
        修改：无
    '''    
    rules_dic = {}
    
    #索引号为0，表示无入座权限限制
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
        由index获取具体的渠道
    入参：index，如 3
    出参：result 如 [{'channel':'500pai'}]
    编写：liulk
    时间：2012-06-20 10:58:21
    修改：无
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
        由index获取具体的渠道
    入参：index，如 3
    出参：channel 如 '500pai'
    编写：liulk
    时间：2012-06-20 10:58:21
    修改：2012-07-16 11:00:43
    '''    
    #channel = db_get_regchannel(index).get('channel')
    channel = db_get_regchannel(index)
    if channel == None:
        return channel
    else:
        return channel.get('channel')
        
        
def get_limited_channel_list(code_list):
    '''
        获取牌桌允许的具体注册渠道
    入参：渠道限制编号，如'1,3,4'
          注意：','前后不能有空格！！！
          
    出参：渠道列表，如["500wan", "500pai", "1000wan"]
    编写：liulk
    时间：2012-06-20 10:18:43
    修改：无
    '''
    #用逗号分隔字符串
    #割后效果：channel_list = ['1', '3', '4']
    code_list = code_list.split( ',' )

    channel_list = []
    
    for value in code_list:
        arg = int(value)
        ret = get_specific_channel( arg )
        if ret == None:
            continue
        #将查询到的渠道信息加入渠道列表
        channel_list.append(ret)
    
    return channel_list



def db_get_time_section(index):
    '''
        获取一个时间段
    入参：index
    出参：result 如{'lower':0, 'upper':30}
    编写：liulk
    时间：2012-06-21 12:11:43
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
        获取一条时间段限制，如(0,30)
    入参：索引号
    出参：result 
    编写：llk
    时间：2012-06-21 12:07:23
    '''
    time_section = []
    #ret = {'lower':0, 'upper':30}
    ret = db_get_time_section(index)
    if ret == None:
        return time_section
    
    time_section.append(ret.get('lower'))
    time_section.append(ret.get('upper'))
    
    #返回格式[0,30]
    return time_section    
                
                
                
def get_limited_time_list(code_list):
    '''
        获取牌桌允许的具体注册时间
        如(30,90)表示注册时间在30--90天之间的玩家
    入参：时间限制编号，如‘2,3’
    出参：time_list 如[[30,90], [90, 120]]
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
        获取用户注册渠道
    入参：user_id
    出参：user_regchannel 用户注册渠道
    编写：liulk
    时间：2012-06-20 11:56:34
    '''
    sql = '''SELECT  f_regchannel channel
                FROM t_user_info
               WHERE f_id = %s'''
    args = (user_id, )
    user_regchannel = Db.Mysql.connect('esun_texas').query(sql, args)
    #只有1条记录，从列表中取出该字典
    return user_regchannel[0]
        
        
def get_user_regtime(user_id):        
    '''
        获取用户注册时间
    入参：user_id
    出参：user_regtime 用户注册时间 {'time':'2012-02-06 16:10:16'}
    编写：liulk
    时间：2012-06-20 11:56:34
    '''
    sql = '''SELECT  f_regtime time
                FROM t_user_info
               WHERE f_id = %s'''
    args = (user_id, )
    user_regtime = Db.Mysql.connect('esun_texas').query(sql, args)    
    #只有1条记录，从列表中取出该字典
    return user_regtime[0]
        
        
def get_white_list(list_name):
    '''
        获取赛事白名单
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
        获取用户充值记录
        目前只查询用户是否充过值
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
    #没有查到，再查询  
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
        获取玩家天梯积分
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
        获取玩家vip等级
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
    
