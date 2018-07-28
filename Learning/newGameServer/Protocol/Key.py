#coding=gbk       
                            
''' 参数key对应 '''
                            
CODE                        = '0001'             #操作（返回）码，对照表待定                                  
SESSION_ID                  = '0002'             #session id                                                        
HEADER                      = '0003'             #消息头                                                            
BODY                        = '0004'             #消息体                                                            
COMMAND_ID                  = '0005'             #指令id                                                            
CONNECT_ID                  = '0006'             #连接id                                                            
TIMESTAMP                   = '0007'             #unix时间戳                                                        
SEQUENCE_ID                 = '0008'             #本指令的序列号，每次RESP返回的序列号需要跟指令请求过来的序列号一致
USER_AGENT                  = '0009'             #客户端版本
MSG_SEQUENCE                = '000D'             #区分接收到的指令，是当时那个阶段所发的指令，防止因网络延迟，造成相关自动操作现象
                            
TABLE_LIST                  = '1001'             #牌桌清单                          
TABLE_ID                    = '1002'             #牌桌id                            
TABLE_TYPE                  = '1003'             #牌桌类型                          
GAME_SPEED                  = '1004'             #游戏速度                          
BLIND_INFO                  = '1005'             #盲注信息                          
ANTE                        = '1006'             #底注   
TABLE_NAME                  = '1007'             #牌桌名称
TABLE_INFO                  = '1008'             #牌桌信息
INS_STATE                   = '110F'             # 保险功能状态   '0':关闭   '1':开启
SUB_TABLE_TYPE				= '1110'			 # 牌桌子类
AUTO_BLIND 					= '1111'			 # 系统是否自动扣除大小盲  1:自动扣除  0：不扣除
BOTT_BBTIMES				= '1112'			 # 庄前注BB倍数
PK_FIRST_BET			 = '1113'			 # PK时修改默认规则  0:默认   1:修改
COMSUMP_TYPE				= '1114'             # 创建牌桌时消耗类型   0:  默认值   1: 房卡   2: 货币
REDU_CHIP_FLAG              = '1116'			  # 6+卸码功能是否开启 
REDU_CHIP_LIMIT             = '1117'			  # 6+卸码额度界限
REDU_CHIP_SERVICE_RATE      = '1118'			  # 6+卸码手续费(百分比)
TABLE_FINISH_UTC			= '1119'			 # 桌子结束时间(UTC)
CARD_COMPARE_TYPE			= '111E'			 # 牌桌比牌类型，0:普通牌桌，1:6+,22:6+花式
APPLY_BUYIN_OPEN            = '12E0'             # 是否有批准买入功能
PT_POT_OPEN                 = '12E1'             # 是否有保险池分配功能

FAST_TABLE                  = '100E'             #快速桌  

SERVER_GROUP                = '100F'             #服务组名
SERVER_NAME                 = '1010'             #服务名
BUYIN_TIMES					= '1011'			 #有效buyin次数统计，目前统计的是最大买入
                      
LEFT_COMMUNITY_CARDS        = '2000' 			 #剩余公共牌                    
PLAYER_LIST                 = '2001'             #玩家清单                          
SEAT_NUM                    = '2002'             #座位数                            
USER_ID                     = '2003'             #用户id                            
USER_NAME                   = '2004'             #用户名                            
USER_CHIPS                  = '2005'             #用户筹码                          
HAND_ID                     = '2006'             #这一手的id（每一手都会有唯一的id）
DEALER_BUTTON               = '2007'             #庄家                              
SMALL_BLIND                 = '2008'             #小盲                              
BIG_BLIND                   = '2009'             #大盲                              
POT_INFO                    = '200A'             #奖池信息                          
COMMUNITY_CARDS             = '200B'             #公共牌                            
BET_CHIPS                   = '200C'             #下注（加注）筹码数                
ROUND_CHIPS                 = '200D'             #这一圈（街）筹码数                
HAND_CHIPS                  = '200E'             #这一手筹码数
SEAT_NO                     = '200F'             #座位编号                                                
GAME_STATUS                 = '2010'             #游戏状态              
PLAYER_STATUS               = '2011'             #玩家状态              
REMAIN_TIME                 = '2012'             #玩家剩余下注时间      
BUTTON_NO                   = '2013'             #庄家位置              
SBLIND_NO                   = '2014'             #小盲位置              
BBLIND_NO                   = '2015'             #大盲位置              
WAIT_FOR_NO                 = '2016'             #轮到下注者的座位号    
LAST_POTS                   = '2017'             #上一街底池            
CARD_LIST                   = '2018'             #牌的列表，亮牌的时候用
PRIZE_LIST                  = '2019'             #派奖list              
ABSENT_LIST                 = '201A'             #缺席（等待玩家）列表  
WAITING_LIST                = '201B'             #排队玩家列表  
POCKET_CARDS                = '201C'             #手牌        
REMOTE_NAME                 = '201D'             #远程服务名 ，就是目前的remotename，包括group_name,server_name
HANDS_NUM                   = '201E'             #打了多少手
ANTE_INFO                   = '201F'             #玩家下的底注信息
CARD_TYPE                   = '2020'             #牌型
MAX_CARD                    = '2021'             #最大牌
WIN_CHIPS                   = '2022'             #玩家赢得的筹码数
OPTIONAL_ACTIONS            = '2023'             #可选择操作
CALL                        = '2024'             #跟注多少
RAISE                       = '2025'             #加注(上限和下限)
IS_TRUSTEE                  = '2026'             #玩家是否托管
IS_AUTO_BLIND               = '2027'             #是否自动缴纳盲注
IS_AUTO_ANTE                = '2028'             #是否自动缴纳底注
PLAYER_MYINFO               = '2029'             #玩家自己的私有信息
TOTAL_POT                   = '202A'             #牌桌上的所有筹码（不包括玩家身上的)
SHOWDOWN_OPTIONAL           = '202B'             #是否可选择亮牌
SHOWDOWN_TYPE               = '202C'             #选择亮牌类型，详情参考Config.py           
RAKE_CHIPS                  = '202D'             #抽水筹码数
SITOUT_TIME                 = '202E'             #玩家站起的时间
AUTO_BLIND_TYPE             = '202F'             #设置玩家缴纳盲注类型
NEW_BLIND_CHIPS             = '2030'             #新手盲注            
NEW_BLIND_INFO              = '2031'             #新手盲注缴纳信息    
BUY_CHIPS_MIN               = '2032'             #买入最小筹码数      
BUY_CHIPS_MAX               = '2033'             #买入最大筹码数      
RAKE_CHIPS_SUM_BF_FLOP      = '2034'             #翻牌前抽水筹码数            
RAKE_CHIPS_PER_BF_FLOP      = '2035'             #翻牌前额定每个玩家抽水筹码数
RAKE_CHIPS_SUM_AF_FLOP      = '2036'             #翻牌后抽水筹码数            
RAKE_CHIPS_MAX_AF_FLOP      = '2037'             #翻牌后抽水最大筹码数        
RAKE_CHIPS_RATIO_AF_FLOP    = '2038'             #翻牌后抽水比例    
RAKE_INFO_BF_FLOP            = '2039'             #翻牌前抽水信息
BUY_CHIPS                   = '203A'             #买入筹码
PLAYER_ID                    = '203B'               #玩家（临时）ID
PUNISH_BLIND_INFO            = '203C'             #惩罚盲注信息
IS_PLAYING                    = '203D'             #是否玩的用户
PUNISH_BLIND_CHIPS            = '203E'             #惩罚盲注大小
BUY_TYPE                    = '203F'             #买入类型：BUY_IN或者RE_BUY 
CASH_OUT                    = '2040'             #用户现金桌兑换的筹码数    
GAIN_POINTS                 = '2041'             #用户现金桌获得的积分数    
STAY_TIME                   = '2042'             #用户在牌桌上的待的持续时间
BLIND_NAME                  = '2043'             #盲注名称                  
RAKE_CHIPS_BF_FLOP          = '2044'             #翻牌前该玩家抽水筹码数    
RAKE_CHIPS_AF_FLOP          = '2045'             #翻牌后该玩家抽水筹码数    
HAND_START_REMAIN_TIME      = '2046'             #（下一手）牌局开始的剩余时间
SBLIND_DODGE_NUM            = '2047'             #逃小盲次数
BBLIND_DODGE_NUM            = '2048'             #逃大盲次数
IS_NEW_PLAYER               = '2049'             #是否新玩家（坐下了但还没进入牌局的）


USER_NICK_NAME              = '2050'             #玩家别名，QQ号名字 、、、、、、、、、、这个地方与原来定义的地方有冲突了
USER_SEX                    = '2051'             #玩家性别


CASH_TABLE_RULE_TYPE        = '2055'             #现金桌游戏规则类型（专业规则，快速入住规则）

CURRENT_TIME                = '2057'             #后台当前时间
IS_ADDON_STATE              = '2058'             #是否处在addon等待期间
REBUY_COUNT                 = '2059'             #玩家成功rebuy次数

CARD_PRIZE_LIST             = '2060'             #抽到奖的牌，列表[ '0_A', '1_3']可以获奖
PLAYER_ONLINE_IP            = '2061'             #玩家在线ip
PRIZE_PUBLIC_CARD           = '2062'             #玩家能够抽奖的牌（公共牌）
TOTAL_BUY_CHIPS             = '2063'             #玩家总买入筹码
PRIZE_PRIVATE_CARD          = '2064'             #玩家能够抽奖的牌（底牌）
CARD                        = '2065'             #玩家选择的牌
PROFIT_MONEY                = '2066'             #玩家盈利情况 正数为赢，负数为亏  

GAME_INFO                   = '2070'             #传给另一个游戏服务，所带的游戏服务消息
FAST_PLAYER_INFO            = '2071'             #传给另一个游戏服务，所带的玩家消息
APPOINT_BBLIND              = '2072'             #YES/NO 是否指定大盲注，用于快速找座
KICKED_INFO                 = '2073'             #玩家被踢信息
REWARD_OUT_INFO				= '2074'			 #没个pot中获胜者及allin玩家uid列表
APPLY_UID                   = '2075'
APPLY_USERNAME              = '2076'
SERVICE_TYPE                = '2077'
SERVICE_ARGS                = '2078'
APPLY_DELAY_TIMES           = '2079'             #在当前街已经申请延时次数
KEEP_SEAT_STIME             = '2080'

CHIPS_SITOUT        		= '208F'             # 玩家离桌时所剩筹码  

BOTTON_PRE_CHIPS			= '2090'			 # 庄前注
BOTTON_PRE_INFO             = '2091'             #庄前注缴纳信息   

                          
MATCH_ID                    = '3001'             #赛事ID  
MATCH_NAME                  = '3002'             #赛事名称
MATCH_TYPE                  = '3003'             #赛事类型  
COMMON_RULE                 = '3004'             #普通规则  
SPECIFIC_RULE               = '3005'             #特殊规则  
TOURNEY_TYPE                = '3006'             #锦标赛类型
START_TIME                  = '3007'             #开始时间  
END_TIME                    = '3008'             #结束时间  
MATCH_STATUS                = '3009'             #赛事状态  
MATCH_STATUS                = '3009'             #赛事状态          
MIN_UNUM                    = '300A'             #最小开赛人数      
MAX_UNUM                    = '300B'             #最大报名人数      
CUR_UNUM                    = '300C'             #当前（已报名）人数
PAY_INFO                    = '300D'             #报名支付信息  

BLIND_LEVEL                 = '3011'             #当前盲注级别  

  
PAY_TYPE                    = '3026'             #支付类型 
SERVICE_CHARGE              = '3028'


IS_REBUY                    = '306C'             #是否rebuy赛,‘YES’ 'NO'
REBUY_LIMIT_COUNT           = '306D'             #成功rebuy限制次数
LEGAL_BLIND_LEVEL           = '306E'             #合法rebuy盲注级别
REBUY_VALUE                 = '306F'             #rebuy一次所增加的筹码数目
REBUY_PAY_MONEY             = '3071'             #rebuy一次花费的钱
PLAYER_INIT_CHIPS           = '3078'             #赛事当前牌局，玩家的初始筹码
REBUY_TYPE                  = '3079'             #rebuy类型
TABLE_INIT_CHIPS            = '100C'             #赛事开始时，每个玩家的初始筹码 
ADDON_WAIT_TIME             = '3072'             #addon一次所等待的时间
ADDON_VALUE                 = '3073'             #addon一次所能增加的筹码
ADDON_PAYMONEY              = '3074'             #addon一次所花费的钱
PASSIVE_REBUY_USER          = '3075'             #可以被动rebuy的玩家列表 [userid, ]
PLAYER_CHIPS_LIST           = '3076'             #在发送派奖消息里，带上玩家最终所剩筹码 { userid:chips , } 
REBUY_MODE                  = '3080'             #rebuy类型，自动=0， 手动=1
ADDON_ST_TIME               = '3081'             #addon的开始时间 
VALID_REBUY_TIME            = '3082'             #开始多少时间内可以rebuy
PASSIVE_REBUY_WAIT_TIME     = '3085'             #被动rebuy玩家还可以等待的时间
IS_SUC_ADDON                = '3086'             #玩家是否成功addon  
IS_PASSIVE_REBUY            = '3087'             #牌桌是否处于被动rebuy状态
IS_SUC_REBUY                = '3089'             #玩家当前牌局，是否成功rebuy过一次
IS_WATI_TO_ADDON            = '3090'             #是否等待进入addon


IS_SIT_OUT                  = '3095'             #参与牌局的玩家是否中途离开牌桌
IS_ALLIN                    = '3096'             #是否是allin桌 ‘YES'  'NO'
IS_FAST_SIT                 = '3098'             #是否是快速开始入座 是'YES', 不是'NO'
PRE_BUY_CHIPS               = '309A'             #现金桌，玩家成功中途补充的玩家筹码数
FINALLY_CHIPS               = '309B'             #玩家牌桌上的最终筹码
PRE_BUY_CHIPS_A             = '309C'             #玩家当前一次预买成功的筹码
WAIT_REASON                 = '309D'
IS_SYNC_RULE                = '309E'             #是否同步了牌桌规则

PLAY_TYPE                   = '30A5'             #游戏类型

TABLE_OWNER                 = '30A8'             #房间属主  'sys'系统创建的。  ‘userid’玩家创建的
PLAYER_PAYBACK_LIST         = '30B4'             #翻牌前抽水返还列表


REDU_CHIP_OPER			 = '30C1'			  # 操作枚举   1： 一键卸码  2: 手动卸码   3:上码 
REDU_CHIP_CHIP			 = '30C2'			  # 操作筹码数
REDU_CHIP_SERVICE_FEE    = '30C3'			  # 卸码手续费， 百分比  1% = 1
REDU_CHIP_OPER_TIME      = '30C4'			  # 卸码操作时间 utc
REDU_CHIP_BOX_TOTAL      = '30C5'			  # 玩家在保管箱中的筹码总量
REDUCE_CHIP_FLAG         = '30C6'			  # 卸码功能是否开启
REDUCE_CHIP_LIMIT        = '30C7'			  # 卸码界限

# 33**开头为保险相关  added by wj
PT_OUTS_TOTAL				= '3300'			# 保险中的单元信息列表
PT_OUTS						= '3301'			# 保险单元信息中的outs
PT_POTS						= '3302'			# 保险中的底池信息（主及边池）
PT_RATES					= '3303'			# 保险中的赔率
PT_OPERATE					= '3304'            # 保险操作枚举   -1: 默认值   0: 拒绝购买    1： 半pot   2: 全pot   3: 背回保险   4: 保本
PT_POT_TYPE					= '3305'			# 底池类型       1: 主池        2： 边池
PT_BACK_MONEY				= '3306'			# 背回保险所需金额(主池)
PT_STREET_FLAG				= '3307'			# 保险信息属于那个阶段  1: 转牌前    2: 和牌前
PT_ACTIVE_MONEY				= '3308'			# 玩家激活保险操作需金额
PT_OPER_LIST				= '3309'			# 玩家保险操作列表 
PT_REAL_REDUCE				= '330A'			# 是否真实成功扣除买保险所需的筹码 (结算时用到)
# 以下几个key 用于同步相关信息
PT_ALL_INFO					= '330B'			# 一局所有的保险信息(用于同步matchserver)
PT_USER_UNIT				= '330C'			# 保险信息中每一玩家的信息 包括: username, 底牌， 购险筹码, 系统赔付筹码
PT_TOTAL_POTS				= '330D'			# 一局中的底池的总额
PT_USER_MONEY				= '330E'			# 一局中玩家的总投保额
PT_USER_BACK_MONEY			= '330F'			# 一局中玩家的投中保险系统赔还的额度
PT_USER_ALL_UNIT			= '3310'			# 所有玩家信息单元
PT_USER_CHIPS				= '3311'			# 玩家一局结束后，筹码的输赢情况   正数表示赢， 负数表示输
PT_USER_HEAD_IMG			= '3312'			# 玩家头像url
PT_SYS_PT_INFO				= '3313'			# 系统保险中亏盈数额
PT_USER_MAX_CARD			= '3314'			# 玩家最大牌(5张)
PT_MAX_HALF_POT				= '3315'			# 玩家半pot最大投保额
PT_MAX_FULL_POT				= '3316'			# 玩家全pot最大投保额
PT_MAX_HALF_BACK			= '3317'			# 半pot最大赔付额
PT_MAX_FULL_BACK			= '3318'			# 全pot最大赔付额
PT_PAY_TYPE					= '3319'			# 支付类型  POINT:钻    GOLD: 金币
PT_TABLE_NAME				= '331A'			# 牌桌名称
PT_BACK_MONEY_OTHER			= '331C'			# 背回保险所需金额(边池)
OUTS_RATE_LISTS  			= '331D'			# outs的rate列表
OUTS_NUMB					= '331E'			# outs个数
OUTS_RATE                   = '331F'			# outs赔率
IS_OPER_PT_2_STREET			= '3320'			# 转牌前是否有保险操作
IS_USER_PT_WIN				= '3322'			# 玩家是否买中保险
PT_WIN_WILL_BACK_CHIP       = '3323'            # 玩家买中保险将获得的赔偿（这里仅仅是给客户端显示）
PT_MAX_BASE_BACK			= '3324'			# 保本最大赔付额
PT_SAME_OUTS				= '3325'			# 平分的outs列表
PT_USER_SELECT_OUTS			= '3326'			# 玩家选择购买保险的outs列表
PT_RESULT_LISTS				= '3327'			# 广播玩家保险结果的列表
PT_OPER_LISTS				= '3328'			# 广播玩家保险操作的列表
PT_USER_GET_POT				= '3330'			# 玩家在一手牌中获得的底池
PT_GET_POT_BACK_LISTS		= '3331'			# 广播一手牌玩家获取底池与保险赔付的列表
PT_OPER_REMAIN_TIME			= '3332'			# 保险操作剩余的时间(秒)
USER_PT_OPER_WIN_OR_LOST	= '3333'			# 玩家本局保险盈亏情况  正数表示玩家投保赚了，负数表示玩家投保亏了
USER_STREET_PT_RESULT		= '3334'			# 玩家当前阶段(当前只有转牌前与和牌前二个阶段)保险盈亏情况  正数表示玩家中了保险，负数表示玩家没中保险
USER_PT_DETAIL_LIST			= '3335'			# 玩家在一手牌中保险的详细操作列表
UNSELECT_OUTS_NUMB			= '3336'			# 没有选择的outs个数
UNSELECT_ACTIVE_MONEY		= '3337'			# 没有选择的outs系统自动投保额
UNSELECT_PT_RESULT			= '3338'			# 没有选择的outs是否中保  0：没有中保   1:中保
PT_MAIN_POT_BACK			= '3339'			# 一手牌从主池中保险赔付额
PT_SUB_POT_BACK				= '333A'			# 一手牌从边池中保险赔付额
WIN_MAIN_POT				= '333B'			# 一手牌获得主池筹码
WIN_SUB_POT					= '333C'			# 一手牌获得边池筹码
MAIN_POT_PUT_MONEY			= '333D'			# 一手牌主池中实际扣除的保费
SUB_POT_PUT_MONEY			= '333E'			# 一手牌边池中实际扣除的保费
TABLE_REMAIN_TIME			= '333F'			# 朋友局牌桌剩余时间(秒)
PT_ADJUST_LIST				= '3340'			# 保险池分配列表
PT_POT_PERCENT				= '3341'			# 玩家分配保险池所占比例
ONE_KEY_PASS_BUYIN_LIST		= '3342'			# 一键通过买入申请的用户列表

REDUCE_CHIPS_INFOS		    = '3997'			# 短牌中卸码信息
SAVE_SUCC_FLAG				= '3998'			# 记录成功进入牌桌信息标示(不用再输密码)

PASSWORD                    = '4001'             #密码    
USER_TYPE                   = '4002'             #用户类型
USER_STATUS                 = '4003'             #用户状态            
MOD_TIME                    = '4004'             #（最后）修改时间    
CRT_TIME                    = '4005'             #创建（添加）时间    
MONEY_BALANCE               = '4006'             #余额                
ADMIN_NAME                  = '4007'             #管理员（操作员）名称
ADMIN_NOTE                  = '4008'             #管理（操作）说明   

IS_IMAGE_CHARG              = '4051'             #聊天信息为图像表情,是否扣钱
IMAGE_CHARG                 = '4052'             #聊天信息为表情，扣的钱数目


CHAT_MSG_TYPE               = '4070'             #聊天消息类型 普通处理：'COMMON'  只允许flash: 'ONLY_FALSH'


USER_IDENTITY               = '600F'             # 玩家身份,在曹冰那边是USER_GROUP '1,2,3'

ORDER_ID                    = '500B'             #订单id 
 

DEBAO_BALANCE               = '5028'             #德堡币余额
GOLD_BALANCE                = '5029'             #金币余额
SILVER_BALANCE              = '502A'             #银币余额

TOTAL_GOLD_BALANCE          = '504C'             #玩家总金币余额
TOTAL_SILVER_BALANCE        = '504D'             #玩家总银币余额 


CONTENT                     = '6004'             #(信息)内容
WHITE_LIST                  = '6007'             #白名单

TABLE_CREATE_TIME			= '8900'			 # 桌子创建时间戳

DEADLINE                    = 'A009'            #截止时间  玩家自创的牌桌截止日期

TIMER_INTERVAL              = 'B001'             #integer   定时器请求时间(ms)
TIMER_USAGE                 = 'B002'             #string    定时器用途（靠这个来做业务处理)


MONEY_AMOUNT                = 'E001'              #float   操作的钱数额
NEED_RESP                   = 'E002'              #bool    是否需要返回
MONEY_TYPE                  = 'E003'              #string  钱类型
MONEY_RESULT                = 'E004'              #integer 返回结果
MONEY_CURRENT_AMOUNT        = 'E005'              #float    操作后，玩家当前于额
MONEY_BUSINESS_UNIQUE_NUM   = 'E006'              #string  业务唯一标示码


LOG_TYPE                    = 'F001'              #string 业务
LOG_COST                    = 'F002'              #float 耗时
