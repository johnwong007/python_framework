#coding=utf-8

PING                    = 0x00000001
PING_RESP               = 0x80000001
CONNECT                 = 0x00000002
CONNECT_RESP            = 0x80000002
QUIT                    = 0x00000003
QUIT_RESP               = 0x80000003

TABLE_LIST              = 0x00010001
TABLE_LIST_RESP         = 0x80010001
CASH_OUT_PLAYER         = 0x00010002
PRIZE_MATCH_PLAYER      = 0x00010003
SAVE_MATCH_PLAYER_STAT  = 0x00010004        #赛事通知代理：保存用户赛事统计数据（总的手数和总的被抽水数等）
REBUY_BACK_MONEY        = 0x00010005        #通知大厅代理给赛事中rebuy玩家退钱
REPEAT_APPLY_BACKMONEY  = 0x00010006        #给重复报名玩家退款
NOTIFY_MATCH_REGISTER   = 0x00010007        #赛事通知代理：有比赛可以报名了
APPLY_MATCH_NOTIFY      = 0x00010008       #赛事通知代理：有玩家报名了比赛
NOTIFY_MATCH_START      = 0x00010009        #赛事通知代理：有比赛开始了
NOTIFY_MATCH_END        = 0x0001000B        #赛事通知代理：有比赛结束了


TABLE_JOIN              = 0x00020001    #加入牌桌          131073
TABLE_JOIN_RESP         = 0x80020001    #加入牌桌回应      2147614721
TABLE_LEAVE             = 0x00020002    #离开牌桌          131074
TABLE_LEAVE_RESP        = 0x80020002    #离开牌桌回应      2147614722
TABLE_INFO              = 0x00020003    #获取牌桌信息      131075
TABLE_INFO_RESP         = 0x80020003    #获取牌桌信息回应  2147614723 2147614723
SIT                     = 0x00020004    #坐下  
SIT_MSG                 = 0x80020004    #坐下消息        2147614724
SIT_OUT                 = 0x00020005    #离开座位      131077 
SIT_OUT_MSG             = 0x80020005    #离开座位消息  2147614725
BUY_IN                  = 0x00020006    #买入
BUY_IN_RESP             = 0x80020006    #买入回应
TABLE_MJOIN             = 0x00020007    #把用户带入牌桌（内部服务间调用）
TABLE_MJOIN_RESP        = 0x80020007    #把用户带入牌桌回应
TABLE_MLEAVE            = 0x00020008    #把用户带离牌桌（内部服务间调用）
TABLE_MLEAVE_RESP       = 0x80020008    #把用户带离牌桌回应
BUY_CHIPS_PLAYER        = 0x00020009    #赛事通知游戏：有用户买入筹码（传入订单ID，赛桌ID，用户ID）131081
BUY_CHIPS_PLAYER_RESP   = 0x80020009    #赛事通知游戏：有用户买入筹码回应 2147614729
JOIN_QUEUE_RESP         = 0x8002000B
QUIT_QUEUE_RESP         = 0x8002000C          #取消等待响应

# 这个文件里很多变量的定义对应game服务代码lib/Protocal/command.py
TABLE_SYNC_MSG          = 0x0002020A    #同步牌桌信息（每手结束以后同步信息到赛事） 131594
TABLE_CREATE            = 0x00020301    #创建牌桌
TABLE_CREATE_RESP       = 0x80020301    #创建牌桌回应
TABLE_START             = 0x00020302    #启动赛桌
TABLE_START_RESP        = 0x80020302    #启动赛桌回应
TABLE_DESTROY           = 0x00020304    #销毁赛桌
TABLE_DESTROY_RESP      = 0x80020304    #销毁赛桌回应
TABLE_SYNC_RULE         = 0x00020305    #同步赛事规则 
TABLE_SYNC_RULE_RESP    = 0x80020305    #同步赛事规则回应
TABLE_GUIDE             = 0x00020306    #引导用户加入赛桌
TABLE_GUIDE_RESP        = 0x80020306    #引导用户加入赛桌回应
TABLE_PAUSE             = 0x00020303    #通知玩家赛桌暂停
TABLE_ADDON             = 0x00020308    #通知Game牌桌开始addon
TABLE_WAIT_ADDON        = 0x00020309    #等待所有桌子停下来addon
DESTROY_CASH_TABLE      = 0x0002030C    #销毁现金桌

REPORT_REDUCE_CHIPS_INFO = 0x00020400   # 上报卸码相关信息


#入座权限校验,新增指令
SIT_PERMISSION_VERIFY           = 0x0002000F        #请求入座权限判断
SIT_WAITING_VERIFY_FINISH       = 0x8002000F        #入座权限判断回复指令
JOIN_WAITING_VERIFY             = 0x00020010        #请求判断是否有权限加入等待列表
JOIN_WAITING_VERIFY_FINISH      = 0x80020010        #加入牌桌等待列表权限判断回复指令

FOLD_MATCH                      = 0x00020012        #放弃锦标赛 131090 

MATCH_PLAYER_REBUY              = 0x00020110         #主动rebuy筹码
REBUY_CHIPS_FINISH              = 0x80020110         #比赛中rebuy筹码,大厅回应
REQUEST_REBUY                   = 0x00020111         #请求大厅代理，rebuy
ADDON_FINISH                    = 0x00020112         #addon结果大厅返回给Match
VALUE_ADDED_REPORT              = 0x00020235         #使用增值服务消费报告
DESTORY_TABLE_BACK_MONEY        = 0x00020238         #房主提前销毁桌子时返消耗
MATCH_PT_ADJUST_PUSH            = 0x00020319         # 通过match保存保险池分配列表



CALL                 = 0x00030001
CALL_MSG             = 0x80030001
RAISE                = 0x00030002
RAISE_MSG            = 0x80030002
FOLD                 = 0x00030003
FOLD_MSG             = 0x80030003
CHECK                = 0x00030004
CHECK_MSG            = 0x80030004
ALL_IN               = 0x00030005
ALL_IN_MSG           = 0x80030005
KICKOUT_OFFLINE_USER = 0x00030006
  


IN_POSITION          = 0x00040001
HAND_START_MSG       = 0x00040002
POCKET_CARD          = 0x00040003
FLOP_CARD_MSG        = 0x00040004
TURN_CARD_MSG        = 0x00040005
RIVER_CARD_MSG       = 0x00040006
SHOWDOWN_MSG         = 0x00040007
POT_MSG              = 0x00040008
PRIZE_MSG            = 0x00040009  


MATCH_REGISTER          = 0x00060001
MATCH_REGISTER_RESP     = 0x80060001
MATCH_UNREGISTER        = 0x00060002
MATCH_UNREGISTER_RESP   = 0x80060002
ELIMINATED_MSG          = 0x00060006
BUY_CHIPS_FINISH        = 0x00060008    # 大厅通知赛事：有用户买入筹码
BUY_CHIPS_FINISH_RESP   = 0x80060008 
CASH_TABLE_GUIDE        = 0x0006000E    #引导玩家入桌
USER_CREATE_TABLE       = 0x0006000F    # 玩家创建牌桌

KICK_USER_CARD_REQ      = 0x00060010 
JOIN_TABLE_ASYNC_NOTIFY = 0x00060011    #赛事加入牌桌后异步通知
MATCH_DELAY_APPLY       = 0x00060012    #延迟报名请求
TABLE_WAIT_MSG          = 0x00060013    #通知牌桌内玩家等候的消息
BUYIN_APPLY             = 0x00060014    #申请买入
BUYIN_APPLY_RESP        = 0x80060014    #申请买入
USER_START_MATCH        = 0x00060015    #自定义比赛房主申请立即开赛
VALUE_ADDED_DEDUCT_NOTIFY = 0x00060016  #增值服务扣费通知
DESTORY_TABLE_BACK_NOTIFY = 0x00060017  #提前销毁桌子返消耗通知
REAL_USER_APPLY_BUYIN   = 0x00060018    #批准买入真实扣款





CODE                = '0001'
CONN_ID             = '0002' 
HEAD                = '0003'
BODY                = '0004'
COMMAND_ID          = '0005'
CONNECT_ID          = '0006'
TIMESTAMP           = '0007'
SEQUENCE_ID         = '0008'
USER_AGENT          = '0009'             #客户端版本
 
TABLE_LIST          = '1001' 
TABLE_ID            = '1002' 
TABLE_TYPE          = '1003' 
GAME_SPEED          = '1004' 
BLIND_INFO          = '1005' 
ANTE                = '1006'
TABLE_NAME          = '1007'
FROM_TABLE_ID       = '1009'
TABLE_LEVEL         = '100A'
TABLE_INIT_CHIPS    = '100C'
FAST_TABLE          = '100E'
INS_STATE           = '110F'                # 保险功能状态
SUB_TABLE_TYPE      = '1110'
AUTO_BLIND          = '1111'
BOTT_BBTIMES        = '1112'             # 庄前注BB倍数
PK_FIRST_BET             = '1113'            # PK时修改默认规则  0:默认   1:修改
COMSUMP_TYPE        = '1114'
PUMP_RATE           = '1115'
REDU_CHIP_FLAG           = '1116'             # 6+卸码功能是否开启 
REDU_CHIP_LIMIT          = '1117'             # 6+卸码额度界限
REDU_CHIP_SERVICE_RATE   = '1118'             # 6+卸码手续费(百分比)
CARD_COMPARE_TYPE           = '111E'             # 牌桌比牌类型，0:普通牌桌，1:6+,22:6+花式
APPLY_BUYIN_OPEN    = '12E0'                  # 是否有批准买入功能
PT_POT_OPEN         = '12E1'                  # 是否有保险池分配功能

LEFT_COMMUNITY_CARDS        = '2000'             #剩余公共牌 
PLAYER_LIST         = '2001' 
SEAT_NUM            = '2002' 
USER_ID             = '2003' 
USER_NAME           = '2004' 
USER_CHIPS          = '2005' 
HAND_ID             = '2006' 
DEALER_BUTTON       = '2007' 
SMALL_BLIND         = '2008' 
BIG_BLIND           = '2009' 
POT_INFO            = '200A' 
COMMUNITY_CARDS     = '200B' 
BOARD               = '200C'
HAND_CHIPS          = '200E' 
SEAT_NO             = '200F'
REMOTE_NAME         = '201D'
BUTTON_NO           = '2013'
SBLIND_NO           = '2014'
BBLIND_NO           = '2015'
HANDS_NUM           = '201E'             #赛桌打了第几手
WIN_CHIPS           = '2022'
IS_TRUSTEE          = '2026'             #玩家是否托管
TOTAL_POT           = '202A'
RAKE_CHIPS          = '202D'
NEW_BLIND_CHIPS     = '2030'
BUY_CHIPS_MIN       = '2032'
BUY_CHIPS_MAX       = '2033'
RAKE_CHIPS_PER_BF_FLOP = '2035'
RAKE_CHIPS_SUM_AF_FLOP = '2036'
RAKE_CHIPS_MAX_AF_FLOP = '2037'
RAKE_CHIPS_RATIO_AF_FLOP = '2038'
BUY_CHIPS           = '203A'
IS_PLAYING          = '203D'
BUY_TYPE            = '203F'
RAKE_CHIPS_BF_FLOP  = '2044'
RAKE_CHIPS_AF_FLOP  = '2045'
RULE_TYPE           = '2055'
REBUY_COUNT         = '2059'
PLAYER_ONLINE_IP    = '2061'			#玩家在线ip
REWARD_OUT_INFO     = '2074'            #每个pot中获胜者及allin玩家uid列表
APPLY_UID           = '2075'

CHIPS_SITOUT        = '208F'            # 玩家离桌时所剩筹码

BLIND_LEVEL         = '3011'

MATCH_ID            = '3001' 
MATCH_NAME          = '3002'
MATCH_TYPE          = '3003'
USER_RANKING        = '300E'                    
PAY_TYPE            = '3026'
PAY_NUM             = '3027'
SERVICE_CHARGE      = '3028'             #integer  服务费
INTHEMONEY_RATIO    = '303A'
REJOIN_CHIPS_TIME   = '3049'
LEFT_TIME           = '306B'
REBUY               = '306C'
REBUY_TIMES         = '306D'                #可以rebuy的最大次数
LEGAL_REBUY_LEVEL   = '306E'
REBUY_VALUE         = '306F'
REBUY_PAYMONEY      = '3071'
ADDON_WAIT_TIME     = '3072'
ADDON_VALUE         = '3073'
ADDON_PAYMONEY      = '3074'
REBUY_TYPE          = '3080'
ADDON_START_TIME    = '3081'
VALID_REBUY_TIME    = '3082'
IS_FAST_SIT         = '3098'                #是否是快速开始入座 是'YES', 不是'NO'
WAIT_REASON         = '309D'


IS_ALLIN            = '3096'
PLAY_TYPE           = '30A5'                #游戏类型
SERVER_ADDR         = '30A7'
TABLE_OWNER         = '30A8'                #房主

USER_CHIPS_INFO     = '3078'                #比赛玩家身上的筹码信息
HUNTING_REWARD      = '30AF'                #猎人赛奖励
IS_DELAY_APPLY      = '30B1'                #是否是延迟报名进入比赛

# 以下几个key 用于同步相关信息
PT_ALL_INFO                 = '330B'            # 一局所有的保险信息(用于同步matchserver)
PT_USER_UNIT                = '330C'            # 保险信息中每一玩家的信息 包括: username, 底牌， 购险筹码, 系统赔付筹码
PT_TOTAL_POTS               = '330D'            # 一局中的底池的投保额
PT_USER_MONEY               = '330E'            # 一局中玩家的总投保额
PT_USER_BACK_MONEY          = '330F'            # 一局中玩家的投中保险系统赔还的额度
PT_USER_ALL_UNIT            = '3310'            # 所有玩家信息单元
PT_USER_CHIPS               = '3311'            # 玩家一局结束后，筹码的输赢情况   正数表示赢， 负数表示输
PT_USER_HEAD_IMG            = '3312'            # 玩家头像url
PT_SYS_PT_INFO              = '3313'            # 系统保险中亏盈数额
PT_PAY_TYPE                 = '3319'            # 支付类型  POINT:钻    GOLD: 金币
PT_TABLE_NAME               = '331A'            # 牌桌名称
USER_PT_OPER_WIN_OR_LOST    = '3333'            # 玩家本局保险盈亏情况  正数表示玩家投保赚了，负数表示玩家投保亏了

PT_ADJUST_LIST              = '3340'            # 保险池分配列表
PT_POT_PERCENT              = '3341'            # 玩家分配保险池所占比例

REDUCE_CHIPS_INFOS          = '3997'            # 短牌中卸码信息
SAVE_SUCC_FLAG              = '3998'           # 记录成功进入牌桌信息标示(不用再输密码)


PASSWORD            = '4001'

ORDER_ID            = '500B'

BUSISORT            = '5012'
BUSINO              = '5013'
TOTAL_GOLD_BALANCE  = '504C'                #总金币余额
TOTAL_SILVER_BALANCE= '504D'                #总银币余额

WHITE_LIST          = '6007'                #白名单
USER_GROUP          = '600F'                #用户所属组
DEADLINE            = 'A009'

class pack:
    def __init__(self):
        self.data = {
            HEAD : {},
            BODY : {},
        }

    def event(self, e):
        self.data[ HEAD ][ COMMAND_ID ] = e
        return self

    def mid(self, _sq):
        self.data[ HEAD ][ SEQUENCE_ID ] = _sq
        return self

    def connid(self, connid):
        self.data[ HEAD ][ CONNECT_ID ] = connid
        return self

    def body(self, b):
        self.data[ BODY ] = b
        return self

    def get(self):
        import JsonUtil as json
        import time
        self.data[ HEAD ][ TIMESTAMP ] = time.time()
        return json.write(self.data)





LOCAL_V = locals()
