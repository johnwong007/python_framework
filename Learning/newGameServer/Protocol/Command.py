#coding=gbk

''' 事件请求和处理指令 '''

# 指令说明
PING                     = 0x00000001         #链路检查                             
PING_RESP                = 0x80000001         #链路检查回应                         
CONNECT                  = 0x00000002         #连接请求，如果带有session信息代表重连
CONNECT_RESP             = 0x80000002         #连接回应，返回（新建的）session信息  
QUIT                     = 0x00000003         #退出服务                             
QUIT_RESP                = 0x80000003         #退出回应                             

LOGIN                    = 0x00050001         #登录请求                                           
LOGIN_RESP               = 0x80050001         #登录回应，如果成功的话需要通知user信息绑定到session
LOGOUT                   = 0x00050002         #登出请求                                           
LOGOUT_RESP              = 0x80050002         #登出回应                                           
CREATE_ACCOUNT           = 0x00050003         #创建账号（注册）                                   
CREATE_ACCOUNT_RESP      = 0x80050003         #创建账号回应                                       
USER_GET_INFO            = 0x00050004         #获取用户信息    
USER_GET_INFO_RESP       = 0x80050004         #获取用户信息回应


MATCH_REGISTER           = 0x00060001         #登记（参加）赛事（竞标赛）
MATCH_REGISTER_RESP      = 0x80060001         #登记回应                  
MATCH_UNREGISTER         = 0x00060002         #退出比赛                  
MATCH_UNREGISTER_RESP    = 0x80060002         #退出回应                  
MATCH_LIST               = 0x00060003         #赛事列表                  
MATCH_LIST_RESP          = 0x80060003         #列表回应                  
MATCH_GET_TABLE          = 0x00060004         #获取比赛桌号              
MATCH_GET_TABLE_RESP     = 0x80060004         #桌号回应                  
MATCH_INFO               = 0x00060005         #获取赛事信息    
MATCH_INFO_RESP          = 0x80060005         #获取赛事信息回应

KICK_USER_CARD_REQ       = 0x00060010
TABLE_WAIT_MSG           = 0X00060013

TABLE_LIST               = 0x00010001         #获取牌桌列表    
TABLE_LIST_RESP          = 0x80010001         #获取牌桌列表回应

TABLE_JOIN               = 0x00020001         #加入牌桌          131073
TABLE_JOIN_RESP          = 0x80020001         #加入牌桌回应      2147614721
TABLE_LEAVE              = 0x00020002         #离开牌桌          131074
TABLE_LEAVE_RESP         = 0x80020002         #离开牌桌回应      2147614722
TABLE_INFO               = 0x00020003         #获取牌桌信息      131075
TABLE_INFO_RESP          = 0x80020003         #获取牌桌信息回应  2147614723 2147614723
SIT                      = 0x00020004         #坐下            
SIT_MSG                  = 0x80020004         #坐下消息        2147614724
SIT_OUT                  = 0x00020005         #离开座位      131077    
SIT_OUT_MSG              = 0x80020005         #离开座位消息  2147614725  
BUY_IN                   = 0x00020006         #买入            
BUY_IN_RESP              = 0x80020006         #买入回应        
TABLE_MJOIN              = 0x00020007         #把用户带入牌桌（内部服务间调用）131079
TABLE_MJOIN_RESP         = 0x80020007         #把用户带入牌桌回应              
TABLE_MLEAVE             = 0x00020008         #把用户带离牌桌（内部服务间调用）
TABLE_MLEAVE_RESP        = 0x80020008         #把用户带离牌桌回应              
BUY_CHIPS_PLAYER         = 0x00020009         #赛事通知游戏：有用户买入筹码（传入订单ID，赛桌ID，用户ID）131081
BUY_CHIPS_PLAYER_RESP     = 0x80020009          #赛事通知游戏：有用户买入筹码回应 2147614729
CORRECT_PLAYER_CHIPS     = 0x0002000A         #赛事通知游戏：纠正（更新）用户筹码    
CORRECT_PLAYER_CHIPS_RESP= 0x8002000A         #赛事通知游戏：纠正（更新）用户筹码回应
JOIN_WAITING             = 0x0002000B          #加入排队等待      131083  
JOIN_WAITING_RESP        = 0x8002000B          #加入等待响应  
UNJOIN_WAITING             = 0x0002000C          #取消排队等待
UNJOIN_WAITING_RESP      = 0x8002000C          #取消等待响应
END_WAITING              = 0x0002000D         #结束等待，通知入座  131085
KEEP_TABLE             = 0x0002000E          #保持桌子（继续围观） 131086  
KEEP_TABLE_RESP             = 0x8002000E          #保持桌子（继续围观）回应  

#下面是做现金桌入座权限功能时增加的指令
SIT_PERMISSION_VERIFY           = 0x0002000F    #请求match端判断入座权限验证   131087
SIT_PERMISSION_VERIFY_FINISH    = 0x8002000F    #入座权限验证完成指令
JOIN_WAITING_VERIFY             = 0x00020010    #请求加入等待列表权限验证
JOIN_WAITING_VERIFY_FINISH      = 0x80020010    #加入等待列表权限验证完成指令

FOLD_MATCH               = 0x00020012           #放弃锦标赛 131090    
FOLD_MATCH_RESP          = 0x80020012           #放弃锦标赛回应

FAST_SIT                        = 0x00020018    #快速开始入座指令   131096
FAST_SIT_RESP                   = 0x80020018    #快速开始入座指令回复   2147614744L
BUY_REQ                         = 0x00020019    #玩家请求买入筹码
BUY_RESP                        = 0x80020019    #玩家买入筹码返回
SET_TRUSTEESHIP                 = 0x0002001B    #牌局开始，只有一个人坐在牌桌上，玩家主动设置暂离
SET_TRUSTEESHIP_RESP            = 0x8002001B    #回复
FAST_SIT_ZHU_ZHAN               = 0x0002001C    #跨游戏服务的快速开始，只针对主站版的
FAST_SIT_ZHU_ZHAN_RESP          = 0x8002001C    #跨游戏服务的快速开始，只针对主站版的回复




TABLE_CREATE             = 0x00020301         #创建牌桌        
TABLE_CREATE_RESP        = 0x80020301         #创建牌桌回应    
TABLE_START              = 0x00020302         #启动赛桌        
TABLE_START_RESP         = 0x80020302         #启动赛桌回应    
TABLE_PAUSE              = 0x00020303         #锦标暂停赛桌，通知旁观玩家        
TABLE_PAUSE_RESP         = 0x80020303         #暂停赛桌回应        
TABLE_DESTROY            = 0x00020304         #销毁赛桌             131844
TABLE_DESTROY_RESP       = 0x80020304         #销毁赛桌回应         2147615492
TABLE_SYNC_RULE          = 0x00020305         #同步赛事规则    
TABLE_SYNC_RULE_RESP     = 0x80020305         #同步赛事规则回应
TABLE_GUIDE              = 0x00020306         #引导用户加入赛桌    
TABLE_GUIDE_RESP         = 0x80020306         #引导用户加入赛桌回应  

GET_PLAYERS              = 0x00020307         #询问桌子玩家 131847
GET_PLAYERS_RESP         = 0x80020307         #返回信息 2147615495


TABLE_ADDON              = 0x00020308         #通知Game牌桌开始addon   131848    
TABLE_WAIT_ADDON         = 0x00020309         #通知牌桌，等待其他桌子进入addon状态 

PRE_BUY_CHIPS_MSG        = 0x0002030A         #预买成功回复（提示本局结束后把钱加上）131850


# **jason**
TABLE_TIME_DELAY		 = 0x0002030B		  #朋友局房主延时 (C->S)
TABLE_TIME_DELAY_RESP	 = 0x8002030B		  #朋友局房主延时响应 (S->C)
TABLE_PUSH_REMAIN_TIME	 = 0x0002030C		  #推送：广播桌止玩家新的剩余时间(单位：秒)  (S->C)
TABLE_OWNER_DESTORY      = 0x0002030D		  #朋友局房主主动（提前）销毁牌桌
TABLE_OWNER_DESTORY_RESP = 0x8002030D
TABLE_PROTCTED_REQU      = 0x0002030E         #用户保险操作(买保险或不卖二种)
TABLE_PROTCTED_RESP      = 0x8002030E
TABLE_PUSH_PROTCTED_INFO = 0x8002030F         #推送:保险信息
TABLE_PUSH_PROTCTED_BACK = 0x80020310         #推送指定用户：保险背回信息
TABLE_REDUCE_CHIP		 = 0x00020311		  # 用户卸码上码操作
TABLE_REDUCE_CHIP_RESP   = 0x80020311
TABLE_GET_OUTS_RATES	 = 0x00020312		  # 获取outs与赔率列表
TABLE_GET_OUTS_RATES_RESP = 0x80020312
TABLE_PUSH_PT_RESULT     = 0x80020313         # 广播：当前阶段保险结果
TABLE_PUSH_PT_OPERATE    = 0x80020314         # 广播：当前阶段保险操作
TABLE_PUSH_PT_LAST_RESULT= 0x80020315		  # 广播：当前这手牌玩家获得底池与保险赔付的结果
TABLE_PT_OPER_DELAY      = 0x00020316		  # 保险操作延时
TABLE_PT_OPER_DELAY_RESP = 0x80020316
PUSH_PT_OPER_REMAIN_TIME = 0x80020317		  # 广播：保险操作剩余时间(秒)
TABLE_PT_ADJUST_REQU     = 0x00020318		  # 保险池分配列表操作
TABLE_PT_ADJUST_RESP     = 0x80020318
MATCH_PT_ADJUST_PUSH     = 0x00020319		  # 通过match保存保险池分配列表
ONE_KEY_PASS_BUYIN_APPLY = 0x0002031A    	  # 一键通过所有买入请求

CALL                     = 0x00020101         #跟注      131329
CALL_MSG                 = 0x80020101         #跟注消息   
RAISE                    = 0x00020102         #加注      131330
RAISE_MSG                = 0x80020102         #加注消息  
FOLD                     = 0x00020103         #弃牌        131331
FOLD_MSG                 = 0x80020103         #弃牌消息     2147614979
CHECK                    = 0x00020104         #看牌        131332
CHECK_MSG                = 0x80020104         #看牌消息  
ALL_IN                   = 0x00020105         #all in        131333
ALL_IN_MSG               = 0x80020105         #all in消息
CANCEL_TRUSTEESHIP       = 0x00020106         #取消托管        131334
CANCEL_TRUSTEESHIP_MSG   = 0x80020106         #取消托管消息    2147614982
SHOWDOWN                 = 0x00020107         #设置亮牌        131335
SHOWDOWN_RESP            = 0x80020107         #设置亮牌消息    2147614983 
SET_AUTO_BLIND           = 0x00020108         #设置自动缴纳盲注类型    
SET_AUTO_BLIND_RESP      = 0x80020108         #设置自动缴纳盲注类型回应

REBUY                    = 0x00020110         #主动rebuy筹码 131344
REBUY_RESP               = 0x80020110         #主动rebuy筹码回应2147614992
PASSIVE_RE_BUY_REQ       = 0x00020111         #请求可以被动rebuy的玩家，是否rebuy   131345
ADDON_FINISH             = 0x00020112         #转发addon完成情况 

LEAVE_CHIPS_STATE        = 0x00020116         #玩家离开牌桌时，玩家在该牌桌的盈利状况131350
CARD_INFO                = 0x00020117         #圣诞活动，玩家点击选择了获奖牌，则给后台回一个131351

WAIT_FOR_MSG             = 0x00020201         #正在等待谁（座位号用户id等）操作（或者什么事件） 131585
HAND_START_MSG           = 0x00020202         #这手牌局开始       131586                                  
POCKET_CARD              = 0x00020203         #手牌               131587                                             
FLOP_CARD_MSG            = 0x00020204         #翻牌               131588                                         
TURN_CARD_MSG            = 0x00020205         #转牌               131589                                        
RIVER_CARD_MSG           = 0x00020206         #河牌               131590                                   
SHOWDOWN_MSG             = 0x00020207         #亮牌               131591                                    
POT_MSG                  = 0x00020208         #奖池（变动）消息   131592                          
PRIZE_MSG                = 0x00020209         #（奖池）派奖消息   131593
TABLE_SYNC_MSG           = 0x0002020A         #同步牌桌信息（每手结束以后同步信息到赛事） 131594
SELECT_BUTTON_MSG        = 0x0002020B         #抽牌决定庄家，结果信息    131595                 
TABLE_BLIND_MSG          = 0x0002020C         #盲注缴纳消息（小盲和大盲信息）   131596          
TABLE_ANTE_MSG           = 0x0002020D         #底注缴纳消息          131597                      
TABLE_BUTTON_MSG         = 0x0002020E         #庄家位置信息（包括小盲和大盲位置）  131598       
TRUSTEESHIP_MSG          = 0x0002020F         #处理托管玩家消息    131599                       
PLAYER_TIMEOUT_MSG       = 0x00020210         #处理玩家超时消息    131600    
SHOWDOWN_REQ             = 0x00020211         #荷官请求亮牌        131601    
TABLE_RAKE_BF_FLOP_MSG   = 0x00020212          #翻牌前抽水消息      131602
BUY_CHIPS_MSG             = 0x00020213          #玩家筹码购买成功    131603
TABLE_DESTROY_MSG        = 0x00020214          #销毁赛桌消息        131604
PUNISH_BLIND_TO_BET     = 0x00020215          #盲注惩罚（归入下注）消息     小盲注 131605
PUNISH_BLIND_NO_BET     = 0x00020216          #盲注惩罚（不归入下注）消息   大盲注 131606
HAND_FINISH_MSG             = 0x00020217          #本手牌结束  131607
BUYIN_APPLY_ANSWER      = 0x00020218            #131608
BUYIN_APPLY_ANSWER_RESP = 0x80020218            #对房主的回复应答  2147615256
REPORT_REDUCE_CHIPS_INFO = 0x00020400   # 上报卸码相关信息


WATCHER_TIMEOUT_MSG      = 0x00020220          #剔除玩家无响应超时的旁观玩家
IS_SIT_OUT                = 0x00020221          #玩家是牌局过程中中途离开牌桌的

UPDATE_PLAYER_CHIPS       = 0x00020224         #更新玩家余额131620
UPDATE_SIT_OUT_PLAYER_CHIPS = 0x00020225       #提醒客户端更新离座玩家的余额 131621


REMIND_USER_TABLE_WILL_DESTROY=0x00020228      #提醒客户端，5分钟后，牌桌即将销毁    131624
REMIND_USER_TABLE_CARD_DESTROY=0x00020229      #提醒客户端，此局结束后，牌桌即将销毁 131625

VOTE_KICK_USER_MSG        = 0x00020230         #131632      踢人投票  服务器->客户端
VOTE_KICK_USER_MSG_RESP   = 0x80020230         #2147615280  投票选择  客户端->服务器
VOTE_KICK_RESULT          = 0x00020231         #131633      投票结果  服务器->客户端
APPLY_OPERATION_DELAY     = 0x00020233         #申请操作延时
APPLY_OPERATION_DELAY_RESP= 0x80020233         #申请操作延时
USER_OPERATE_DELAY_MSG    = 0x00020234         #玩家申请延时后通知牌桌内玩家
VALUE_ADDED_REPORT        = 0x00020235         #使用增值服务消费报告
APPLY_PUBLIC_CARD         = 0x00020236         #牌局结束后申请查看未发出的公共牌
APPLY_PUBLIC_CARD_RESP    = 0x80020236
TRUSTEESHIP_PROTECT       = 0x00020237         #申请托管留座保护
TRUSTEESHIP_PROTECT_RESP  = 0x80020237
DESTORY_TABLE_BACK_MONEY  = 0x00020238         #房主提前销毁桌子时返消耗         
 

DESTROY_CASH_TABLE        = 0x0002030C         #通知match销毁玩家自创的现金桌




TIMER_START               = 0x00040001         #启动一个定时器任务 262145
TIMER_CANCEL              = 0x00040002         #取消一个定时器任务 262146
TIMER_OUT                 = 0x00040003         #定时器任务超时
TIMER_UPDATE              = 0x00040004         #更新定时器


TIMER_BUY_CHIPS           = 0x00050001         #注册买入筹码等待时间327681
TIMER_SIT_OUT             = 0x00050002         #玩家离开牌桌时间（去掉筹码记忆功能）327682
TIMER_TRUSTEE_OUT         = 0x00050003         #玩家托管超时 327683
TIMER_WATCHER_OUT         = 0x00050004         #旁观玩家定时器（踢出长时间没有响应的旁观玩家）327684
TIMER_OPERATION           = 0x00050005         #玩家操作超时327685
TIMER_TRUSTEE_OPER_OUT    = 0x00050006         #玩家托管处理超时327686
TIMER_NEW_ROUND           = 0x00050007         #新一街下注定时327687
TIMER_BF_START_TIMEOUT    = 0x00050008         #开始前等待时间327688
TIMER_SHOW_DOWN_TIMEOUT   = 0x00050009         #设置亮牌超时通知327689
TIMER_PASSIVE_RE_BUY_PAUSE_TIME = 0x0005000A   #被动rebuy超时通知327690
TIMER_INTERVAL_HAND       = 0x0005000B         #新一手等待时间327691
TIMER_STREE_FINISH        = 0x0005000C         #一街下注完成通知327692
TIMER_NEW_OPER_WAIT       = 0x0005000D         #进入下注期间钱等待327693
TIMER_STATE_FINISH        = 0x0005000E         #进入下一状态的间隔时间327694
TIMER_TRUSTEESHIP_FINISH  = 0x0005000F         #一个托管玩家处理之后，间隔0.5秒处理下一个玩家327695
TIMER_GO_SETBUTTON        = 0x00050010         #进入setbutton状态327696
TIMER_GO_WAITEBLIND       = 0x00050011         #进入waiteblind状态327697
TIMER_GO_HAND             = 0x00050012         #进入hand状态327698
TIMER_GO_SET_FIRST_BETER  = 0x00050013         #进入设置地位下注者状态327699
TIMER_GO_FIRST_BET        = 0x00050014         #进入第一次下注327700
TIMER_UN_EXCEPT_LEAVE     = 0x00050015         #确定盲注过程中离开牌桌      

TIMER_GO_PRIZE            = 0x00050017         #进入派奖阶段327703
TIMER_GO_FINISH           = 0x00050018         #进入牌局结束状态327704

TIMER_TO_GAME             = 0x00050019         #通知game进入下一状态327705
TIMER_PAUSE_SERVER        = 0x0005001A         #让游戏服务暂停在一个虚拟牌桌上 327706   
TIMER_FORCE_SIT_OUT       = 0x0005001B         #伪装站起退钱  327707
TIMER_STOP_SERVER_SIGNAL  = 0x0005001C         #告诉服务，即将停服，改变服务端一个标记

TIMER_DESTROY_USER_TABLE  = 0x0005001D         #告诉玩家，此手牌结束之后，即将销毁
TIMER_PRE_REMIND_DESTROY  = 0x0005001E         #提前5分钟，告诉玩家，此牌桌，5分钟后即将销毁
TIMER_VOTE_KICK           = 0x0005001F         #投票踢人时间截止 327711

TIMER_FAST_SIT_ZHU_ZHAN   = 0x00050020         #通知另一个游戏服务，去找座位，只针对主站版

TIMER_KICK_CARD_OUTTIME   = 0x00050021         #踢人卡过期
TIMER_PROCTED_OUTTIME     = 0x00050023         #购买保险过期
BUYIN_APPLY_RESP          = 0x80060014         #申请买入的结果
   
MONEY_IN_QUEUE_REQUEST    = 0x00090001          #退钱  589825
MONEY_OUT_QUEUE_REQUEST   = 0x00090002          #要钱   589826
MONEY_IN_QUEUE_RESP       = 0x80090001          #退钱回复0x80090001
MONEY_OUT_QUEUE_RESP      = 0x80090002          #要钱回复   2148073474


LOGSERVER                 = 0x000A0001          #记录性能日志


