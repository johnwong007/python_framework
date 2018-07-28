#coding=utf-8
import XmlConfig
def get_int_value( prefix, key, default ):
    value = get_xml_value( prefix, key, default )
    return int( value )

def get_str_value( prefix, key, default ):
    value = get_xml_value( prefix, key, default )
    return value

def get_xml_value( prefix, key, default ):
    _map_ = XmlConfig.get( prefix )
    if not _map_ or             \
       type(_map_) != dict or   \
       not _map_.has_key( key ):
        value = default
    else :
        value = _map_[ key ]

    return value

def get_limit_service_names():
    result = []
    str_service_names = get_str_value( '/match/other/limit_service_names', 'value', '' )
    tmp_service_names = str_service_names.split(',')
    for service_name in tmp_service_names:
        service_name = service_name.strip()
        if service_name != '':
            result.append( service_name )

    return result


CODE_EXIST_TABLE                = -11001    # �����룺�Ѿ����ڵ�����
OK_ERROR                        =  10000
REGISTER_CHANNEL_ERROR          = -11033	#ע��������֤ʧ�ܴ���
REGISTER_TIME_ERROR             = -11034	#ע��ʱ����֤ʧ�ܴ���
WHITE_LIST_ERROR                = -11036    #����������
LADDER_POINT_ERROR              = -11037    #���ݻ�������
CHARGING_ERROR                  = -11038    #��ֵ����
CASH_TABLE_RULE_TYPE_ERROR      = -11045    #�ֽ����������ʹ���
NOTEXIST_PAY_TYPE_ERROR         = -11046    #�����ڵ�֧�����ͣ�silver, gold)
NOT_IN_MATCH_ERROR              = -11050    #��Ҳ��ڱ�����
MAX_REBUY_TIMES_ERROR           = -11051    #�ﵽ���rebuy����
FREQUENTLY_REQUEST_REBUY_ERROR  = -11052    #Ƶ������rebuy����
ADDON_OVER_TIME_ERROR           = -13011    #addon��ʱ
IN_QIANQUAN_ERROR               = -13016    #����ǮȦ������rebuy
FREQUENTLY_AUTO_REBUY_ERROR     = -13017    #����Զ�rebuyƵ��������bug
NOT_EXIST_SIT                   = -11011    #�����ڵ���λ �������ֻ��ɰ���ʾ ͬʱҲ��ʾvip�ȼ���������������


REBUY_MODE_AUTO             =   0              # rebuy��ʽ���Զ�
REBUY_MOdE_NOT_AUTO         =   1              # ����


STATUS_MATCH_ANNOUNCED      = 'ANNOUNCED'       # ����״̬������
STATUS_MATCH_REGISTERING    = 'REGISTERING'     # ����״̬: δ����
STATUS_MATCH_READY          = 'PREPARING'       # ����״̬: ׼������
STATUS_MATCH_CREATE_TABLE   = 'PREP_TABLE'      # ����״̬: ��������
STATUS_MATCH_JOIN_PLAYER    = 'PREP_PLAYER'     # ����״̬: �������
STATUS_MATCH_START          = 'STARTING'        # ����״̬: ����
STATUS_MATCH_RUNNING        = 'RUNNING'         # ����״̬: ������
STATUS_MATCH_SYNC           = 'SYNCING'         # ����״̬��ͬ�������飩����
STATUS_MATCH_PRIZE          = 'PRIZE'           # ����״̬���ɽ�
STATUS_MATCH_END            = 'COMPLETED'       # ����״̬������
STATUS_MATCH_CANCEL         = 'CANCELED'        # ����״̬: ����ȡ��


STATUS_CASH_PREPARE         = 'PREPARING'       # �ֽ�����״̬: ׼��
STATUS_CASH_CREATE_TABLE    = 'PREP_TABLE'      # �ֽ�����״̬: ��������
STATUS_CASH_START           = 'STARTING'
STATUS_CASH_RUNNING         = 'RUNNING'

STATUS_TABLE_OPENED         = 'OPENED'          # ����״̬: ����
STATUS_TABLE_CLOSED         = 'CLOSED'          # ����״̬: �ر�
STATUS_TABLE_PAUSE          = 'PAUSE'           # ����״̬����ͣ
STATUS_TABLE_ADDON          = 'ADDON'           # ����״̬��ADDON,���ռ���

STATUS_PLAYER_PLAYING       = 'PLAYING'         # ���״̬���ڴ���
STATUS_PLAYER_ELIMINATED    = 'ELIMINATED'      # ���״̬���˳������£�
STATUS_PLAYER_WIN_TABLE     = 'WINNER'          # ���״̬���������л�ʤ


STATUS_ORDER_INIT           = 'INIT'            # ����״̬����ʼ̬
STATUS_ORDER_RETURNING      = 'RETURNING'       # ����״̬��������
STATUS_ORDER_GAMEFAIL       = 'GAMEFAIL'        # ����״̬����Ϸ��ӳ���ʧ��
STATUS_ORDER_DONE           = 'DONE'            # ����״̬����Ϸ��ӳ������
STATUS_ORDER_ACCTOP         = 'ACCTOP'          # ����״̬���˻�������


TABLE_TYPE_SIT              = 'SITANDGO'        # �������ͣ���������
TABLE_TYPE_TIME             = 'TOURNEY'         # �������ͣ���ʱ���򾺱���
TABLE_TYPE_CASH             = 'CASH'            # �������ͣ��ֽ���

MATCH_TYPE_SIT              = 'SITANDGO'        # �������ͣ���������
MATCH_TYPE_TIME             = 'TOURNEY'         # �������ͣ���ʱ��

APPLY_PAY_STATUS            = 'PAYED'           # ��������״̬���Ѹ���
APPLY_STATUS                = 'VALID'           # ����״̬���ѱ���

BUSISORT_MATCH_GAME         = 'MATCH_GAME'      # ���״��࣬�����ж���
BUSINO_REBUY                = 'REBUY'           # �������࣬rebuy
BUSINO_ADDON                = 'ADDON'           # �������࣬addon
BUSISORT_CASH_GAME          = 'CASH_GAME'       # ���״��࣬�ֽ�������
BUSINO_CASH_OUT             = 'CASH_OUT'        # �������࣬����һ����ֽ�
BUSINO_BUY_IN               = 'BUYIN'           # �������࣬����һ����ֽ�


#
# ����������Ǽ���XML����ͳһ�����
#


## MD��� ##
LOCAL_GROUP_NAME    = get_str_value( '/match/MD/local', 'group_name', 'MATCH' )
LOCAL_IP            = get_str_value( '/match/MD/local', 'ip', "" )  							# �������Ӵ�
MD_ADDRESS          = get_str_value( '/match/MD/address', 'ip', '' ) 							#��Ϣ�ַ����������Ӵ�
GAME_GROUP_NAME     = get_str_value( '/match/MD/game', 'group_name', 'GAME' )           		# ��Ϸ��������
AGENT_GROUP_NAME    = get_str_value( '/match/MD/agent', 'group_name', 'lobby' )
AGENT_SERVICE_NAME  = get_str_value( '/match/MD/agent', 'service_name', 'lobbym' )
AGENT_ADDRESS       = (AGENT_GROUP_NAME, AGENT_SERVICE_NAME)                            		# ��������ַ
TIMEOUT_LISTEN      = get_int_value( '/match/MD/timeout', 'listen', 1 )


## ʱ����� ## 
TIME_TABLE_MANAGE_SLEEP = get_int_value( '/match/time/time_table_manage_sleep', 'value', 1 )  	# ��������ѭ����ѭ�����ʱ��
CHECK_APPLY_LOOP        = get_int_value( '/match/time/check_apply_loop', 'value', 5 ) 			# ���һ��ʱ���鱨������
TOURNEY_GUIDE_WAIT_TIME = get_int_value( '/match/time/tourney_guide_wait_time', 'value', 5 )   # ������ҽ��������Ժ�10���Ժ���֪ͨ��������
SITANDGO_GUIDE_WAIT_TIME= get_int_value( '/match/time/sitandgo_guide_wait_time', 'value', 15 )  # ������ҽ��������Ժ�10���Ժ���֪ͨ��������
WATCH_GAME_LOOP         = get_int_value( '/match/time/watch_game_loop', 'value', 20 )    		# ���һ��ʱ������Ϸ�����״��
CHECK_NEW_MATCH         = get_int_value( '/match/time/check_new_match', 'value', 30 )    		# ���һ��ʱ�����Ƿ����µ����»����ֽ���
MAX_STATUS_PASS_TIME    = get_int_value( '/match/time/max_status_pass_time', 'value', 300 ) 	# ����״̬��������ʱ�䣨��������Ϊ�����쳣��
CHECK_NEW_GAME          = get_int_value( '/match/time/check_new_game', 'value', 60 )    		# ���һ��ʱ����������������ֹͣ������Ϸ����
CHECK_LOOP_PERFORMANCE  = get_int_value( '/match/time/check_loop_performance', 'value', 60 )
HOW_OLD_OF_NEW_MATCH    = get_int_value( '/match/time/how_old_of_new_match', 'value', 15 ) 	 	# ȡn��֮ǰ���µ�������
CONTROL_NEW_MATCH       = get_int_value( '/match/time/control_new_match', 'value', 10 )  		# ���һ��ʱ����ȡ������
CONTROL_NEW_CASH        = get_int_value( '/match/time/control_new_cash', 'value', 15 )  		# ���һ��ʱ����ȡ���ֽ���
AUTO_SUPPLY_CASH_TABLE  = get_int_value( '/match/time/auto_supply_cash_table', 'value', 37 )  	# ��̬�����ֽ����ļ��ʱ��


## redis��� ##
USER_ADDR_MEM_IP        = get_str_value( '/match/memory/redis1', 'ip', '' )  					# �û���ַ�Ĵ洢����IP��Ŀǰ���Ǹ�Redis��������
USER_ADDR_MEM_PORT      = get_int_value( '/match/memory/redis1', 'port', 6379 )           		# �û���ַ�Ĵ洢���Ķ˿�
COMMON_REDIS_IP         = get_str_value( '/match/memory/redis0', 'ip', '' )
COMMON_REDIS_PORT       = get_int_value( '/match/memory/redis0', 'port', 6379 )
USER_ADDR_PREFIX        = get_str_value( '/match/memory/prefix', 'user_info', '/500/texas_holdem/cliaddr/' ) # �û���ַ��ǰ׺
GAME_ADDR_PREFIX        = get_str_value( '/match/memory/prefix', 'game_info', '/500/texas_holdem/gameaddr/' )
LEVEL_GADDR_PREFIX      = get_str_value( '/match/memory/prefix', 'level_gaddr', '/500/texas_holdem/level_gameaddr/' )

## ���� ##
COPY_NEW_SITANDGO       = get_str_value( '/match/other/copy_new_sitandgo', 'value', 'YES' ) 	# �Ƿ񿽱������µ���������
NO_NAME_OF_MATCH_ADDR   = get_str_value( '/match/other/no_name_of_match_addr', 'value', 'NO' )
GAMEADDR_CASH           = get_str_value( '/match/other/gameaddr_cash', 'value', '' )    		#ר��Ϊ�ֽ����������Ϸ����
GAMEADDR_MATCH          = get_str_value( '/match/other/gameaddr_match', 'value', '' )   		#ר��Ϊ���·������Ϸ����
GAMEADDR_RAKEPOINT      = get_str_value( '/match/other/gameaddr_rakepoint', 'value', '' )  		#���ҳ�
GAMEADDR_GOLD           = get_str_value( '/match/other/gameaddr_gold', 'value', '' )    		#��ҳ�
GAMEADDR_TOURNEY        = get_str_value( '/match/other/gameaddr_tourney', 'value', '' ) 
GAMEADDR_SITANDGO       = get_str_value( '/match/other/gameaddr_sitandgo', 'value', '' ) 
LIMIT_SERVICE_NAMES     = get_limit_service_names()
CASH_TABLE_WHITE_LIST   = get_str_value( '/match/white_list/cash_table', 'value', '' )

## �ֽ�����������  ##
CASH_MATCH              = get_str_value( '/match/job/cash', 'value', '' )
MATCH_MATCH              = get_str_value( '/match/job/match', 'value', '' )

