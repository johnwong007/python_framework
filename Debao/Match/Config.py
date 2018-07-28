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


CODE_EXIST_TABLE                = -11001    # 错误码：已经存在的牌桌
OK_ERROR                        =  10000
REGISTER_CHANNEL_ERROR          = -11033	#注册渠道验证失败错误
REGISTER_TIME_ERROR             = -11034	#注册时间验证失败错误
WHITE_LIST_ERROR                = -11036    #白名单限制
LADDER_POINT_ERROR              = -11037    #天梯积分限制
CHARGING_ERROR                  = -11038    #充值限制
CASH_TABLE_RULE_TYPE_ERROR      = -11045    #现金桌规则类型错误
NOTEXIST_PAY_TYPE_ERROR         = -11046    #不存在的支付类型（silver, gold)
NOT_IN_MATCH_ERROR              = -11050    #玩家不在比赛中
MAX_REBUY_TIMES_ERROR           = -11051    #达到最大rebuy次数
FREQUENTLY_REQUEST_REBUY_ERROR  = -11052    #频繁请求rebuy错误
ADDON_OVER_TIME_ERROR           = -13011    #addon超时
IN_QIANQUAN_ERROR               = -13016    #进入钱圈，不能rebuy
FREQUENTLY_AUTO_REBUY_ERROR     = -13017    #解决自动rebuy频繁弹窗的bug
NOT_EXIST_SIT                   = -11011    #不存在的座位 （兼容手机旧版提示 同时也表示vip等级不够不能入桌）


REBUY_MODE_AUTO             =   0              # rebuy方式，自动
REBUY_MOdE_NOT_AUTO         =   1              # 主动


STATUS_MATCH_ANNOUNCED      = 'ANNOUNCED'       # 赛事状态：公告
STATUS_MATCH_REGISTERING    = 'REGISTERING'     # 赛事状态: 未开赛
STATUS_MATCH_READY          = 'PREPARING'       # 赛事状态: 准备开赛
STATUS_MATCH_CREATE_TABLE   = 'PREP_TABLE'      # 赛事状态: 创建赛桌
STATUS_MATCH_JOIN_PLAYER    = 'PREP_PLAYER'     # 赛事状态: 加入玩家
STATUS_MATCH_START          = 'STARTING'        # 赛事状态: 开赛
STATUS_MATCH_RUNNING        = 'RUNNING'         # 赛事状态: 开打中
STATUS_MATCH_SYNC           = 'SYNCING'         # 赛事状态：同步（重组）赛桌
STATUS_MATCH_PRIZE          = 'PRIZE'           # 赛事状态：派奖
STATUS_MATCH_END            = 'COMPLETED'       # 赛事状态：结束
STATUS_MATCH_CANCEL         = 'CANCELED'        # 赛事状态: 赛事取消


STATUS_CASH_PREPARE         = 'PREPARING'       # 现金赛事状态: 准备
STATUS_CASH_CREATE_TABLE    = 'PREP_TABLE'      # 现金赛事状态: 创建赛桌
STATUS_CASH_START           = 'STARTING'
STATUS_CASH_RUNNING         = 'RUNNING'

STATUS_TABLE_OPENED         = 'OPENED'          # 牌桌状态: 开放
STATUS_TABLE_CLOSED         = 'CLOSED'          # 牌桌状态: 关闭
STATUS_TABLE_PAUSE          = 'PAUSE'           # 牌桌状态：暂停
STATUS_TABLE_ADDON          = 'ADDON'           # 牌桌状态：ADDON,最终加码

STATUS_PLAYER_PLAYING       = 'PLAYING'         # 玩家状态：在打牌
STATUS_PLAYER_ELIMINATED    = 'ELIMINATED'      # 玩家状态：退出（赛事）
STATUS_PLAYER_WIN_TABLE     = 'WINNER'          # 玩家状态：在牌桌中获胜


STATUS_ORDER_INIT           = 'INIT'            # 订单状态：初始态
STATUS_ORDER_RETURNING      = 'RETURNING'       # 订单状态：冲正中
STATUS_ORDER_GAMEFAIL       = 'GAMEFAIL'        # 订单状态：游戏添加筹码失败
STATUS_ORDER_DONE           = 'DONE'            # 订单状态：游戏添加筹码完成
STATUS_ORDER_ACCTOP         = 'ACCTOP'          # 订单状态：账户服务处理


TABLE_TYPE_SIT              = 'SITANDGO'        # 牌桌类型：坐满即玩
TABLE_TYPE_TIME             = 'TOURNEY'         # 牌桌类型：定时开打竞标赛
TABLE_TYPE_CASH             = 'CASH'            # 牌桌类型：现金赛

MATCH_TYPE_SIT              = 'SITANDGO'        # 赛事类型：坐满即开
MATCH_TYPE_TIME             = 'TOURNEY'         # 赛事类型：定时赛

APPLY_PAY_STATUS            = 'PAYED'           # 报名付费状态，已付费
APPLY_STATUS                = 'VALID'           # 报名状态，已报名

BUSISORT_MATCH_GAME         = 'MATCH_GAME'      # 交易大类，赛事中订单
BUSINO_REBUY                = 'REBUY'           # 交易子类，rebuy
BUSINO_ADDON                = 'ADDON'           # 交易子类，addon
BUSISORT_CASH_GAME          = 'CASH_GAME'       # 交易大类，现金桌订单
BUSINO_CASH_OUT             = 'CASH_OUT'        # 交易子类，筹码兑换成现金
BUSINO_BUY_IN               = 'BUYIN'           # 交易子类，筹码兑换成现金


#
# 下面的配置是记入XML里面统一管理的
#


## MD相关 ##
LOCAL_GROUP_NAME    = get_str_value( '/match/MD/local', 'group_name', 'MATCH' )
LOCAL_IP            = get_str_value( '/match/MD/local', 'ip', "" )  							# 本地连接串
MD_ADDRESS          = get_str_value( '/match/MD/address', 'ip', '' ) 							#消息分发服务器连接串
GAME_GROUP_NAME     = get_str_value( '/match/MD/game', 'group_name', 'GAME' )           		# 游戏服务组名
AGENT_GROUP_NAME    = get_str_value( '/match/MD/agent', 'group_name', 'lobby' )
AGENT_SERVICE_NAME  = get_str_value( '/match/MD/agent', 'service_name', 'lobbym' )
AGENT_ADDRESS       = (AGENT_GROUP_NAME, AGENT_SERVICE_NAME)                            		# 代理服务地址
TIMEOUT_LISTEN      = get_int_value( '/match/MD/timeout', 'listen', 1 )


## 时间相关 ## 
TIME_TABLE_MANAGE_SLEEP = get_int_value( '/match/time/time_table_manage_sleep', 'value', 1 )  	# 牌桌管理循环的循环间隔时间
CHECK_APPLY_LOOP        = get_int_value( '/match/time/check_apply_loop', 'value', 5 ) 			# 相隔一定时间检查报名人数
TOURNEY_GUIDE_WAIT_TIME = get_int_value( '/match/time/tourney_guide_wait_time', 'value', 5 )   # 引导玩家进入牌桌以后，10秒以后再通知赛桌开打
SITANDGO_GUIDE_WAIT_TIME= get_int_value( '/match/time/sitandgo_guide_wait_time', 'value', 15 )  # 引导玩家进入牌桌以后，10秒以后再通知赛桌开打
WATCH_GAME_LOOP         = get_int_value( '/match/time/watch_game_loop', 'value', 20 )    		# 相隔一定时间检查游戏服务的状况
CHECK_NEW_MATCH         = get_int_value( '/match/time/check_new_match', 'value', 30 )    		# 相隔一定时间检测是否有新的赛事或者现金赛
MAX_STATUS_PASS_TIME    = get_int_value( '/match/time/max_status_pass_time', 'value', 300 ) 	# 赛事状态的最大持续时间（超过则认为赛事异常）
CHECK_NEW_GAME          = get_int_value( '/match/time/check_new_game', 'value', 60 )    		# 相隔一定时间检测有无新启动（停止）的游戏服务
CHECK_LOOP_PERFORMANCE  = get_int_value( '/match/time/check_loop_performance', 'value', 60 )
HOW_OLD_OF_NEW_MATCH    = get_int_value( '/match/time/how_old_of_new_match', 'value', 15 ) 	 	# 取n秒之前更新的新赛事
CONTROL_NEW_MATCH       = get_int_value( '/match/time/control_new_match', 'value', 10 )  		# 相隔一定时间领取新赛事
CONTROL_NEW_CASH        = get_int_value( '/match/time/control_new_cash', 'value', 15 )  		# 相隔一定时间领取新现金赛
AUTO_SUPPLY_CASH_TABLE  = get_int_value( '/match/time/auto_supply_cash_table', 'value', 37 )  	# 动态增加现金桌的间隔时间


## redis相关 ##
USER_ADDR_MEM_IP        = get_str_value( '/match/memory/redis1', 'ip', '' )  					# 用户地址的存储器的IP（目前就是个Redis。。。）
USER_ADDR_MEM_PORT      = get_int_value( '/match/memory/redis1', 'port', 6379 )           		# 用户地址的存储器的端口
COMMON_REDIS_IP         = get_str_value( '/match/memory/redis0', 'ip', '' )
COMMON_REDIS_PORT       = get_int_value( '/match/memory/redis0', 'port', 6379 )
USER_ADDR_PREFIX        = get_str_value( '/match/memory/prefix', 'user_info', '/500/texas_holdem/cliaddr/' ) # 用户地址的前缀
GAME_ADDR_PREFIX        = get_str_value( '/match/memory/prefix', 'game_info', '/500/texas_holdem/gameaddr/' )
LEVEL_GADDR_PREFIX      = get_str_value( '/match/memory/prefix', 'level_gaddr', '/500/texas_holdem/level_gameaddr/' )

## 其他 ##
COPY_NEW_SITANDGO       = get_str_value( '/match/other/copy_new_sitandgo', 'value', 'YES' ) 	# 是否拷贝生成新的坐满即玩
NO_NAME_OF_MATCH_ADDR   = get_str_value( '/match/other/no_name_of_match_addr', 'value', 'NO' )
GAMEADDR_CASH           = get_str_value( '/match/other/gameaddr_cash', 'value', '' )    		#专门为现金桌服务的游戏服务
GAMEADDR_MATCH          = get_str_value( '/match/other/gameaddr_match', 'value', '' )   		#专门为赛事服务的游戏服务
GAMEADDR_RAKEPOINT      = get_str_value( '/match/other/gameaddr_rakepoint', 'value', '' )  		#银币场
GAMEADDR_GOLD           = get_str_value( '/match/other/gameaddr_gold', 'value', '' )    		#金币场
GAMEADDR_TOURNEY        = get_str_value( '/match/other/gameaddr_tourney', 'value', '' ) 
GAMEADDR_SITANDGO       = get_str_value( '/match/other/gameaddr_sitandgo', 'value', '' ) 
LIMIT_SERVICE_NAMES     = get_limit_service_names()
CASH_TABLE_WHITE_LIST   = get_str_value( '/match/white_list/cash_table', 'value', '' )

## 现金桌比赛分离  ##
CASH_MATCH              = get_str_value( '/match/job/cash', 'value', '' )
MATCH_MATCH              = get_str_value( '/match/job/match', 'value', '' )

