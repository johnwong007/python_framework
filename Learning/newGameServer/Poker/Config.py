#coding=gbk
''' 配置项模块 '''
# 消息超时时间
MESSAGE_TIME_OUT         = 1000                         # 单位是秒

# 围观玩家，无响应超时时间
WATCHER_TIME_OUT         = 900                          # 15分钟。单位是秒有6分钟改为15分钟 

# 暂离托管超时时间

TRUSTEE_TIME_OUT         = 600                          # 单位是秒 
# 赛桌相关配置
FLOAT_PRECISION          = 2                            # 浮点精度数
MISS_BBLIND_OUT          = 3                            # 逃脱N次盲注剔除
MIN_START_PEOPLE         = 2                            # 最小开赛人数 

INTERVAL_HAND            = 5                           # 每手间隔时间 

INTERVAL_ROUND           = 2                            # 每街间隔时间 

SHOW_DOWN_TIMEOUT        = 3                            # 亮牌超时时间 

TRUSTEE_TIME             = 0.5                          # 等待托管玩家处理时间

BF_START_TIMEOUT         = 6                            # 开始前等待时间 

REMAIN_LEAVE_TIME        = 1800                         # 保留离开玩家的时间

REMAIN_TIMEOUT_TIME      = 30                           # 留座玩家等待超时时间

REMAIN_TIMEOUT_TIME_VGOLD= 300                           # 留座玩家等待超时时间

THOUSAND                 = 1000                         # 1秒=1000毫秒

STREE_FINISH             = 0.1                          #一街下注完成通知

NEW_OPER_WAIT            = 0.5                          #进入下注区间等待

STATE_FINISH             = 1                            #进入下一状态的间隔时间

TRUSTEESHIP_FINISH       = 1.5                          #一个托管玩家处理之后，间隔0.5秒处理下一个玩家

SAME_IP_NUM              = 2                            #同桌同ip数目限制

VOTE_TIMEOUT_TIME        = 10                           #投票时间

KICKED_CARD_OUTTIME      = 3600                         #踢人卡有效时长 1小时

RAKE_BF_LIMIT_BB         = 10                           #翻牌前抽水限制，玩家余额最低10BB起抽
RAKE_BF_BB_NUM           = 3                            #翻牌前固定抽水，3个BB

PROTECTED_MAX_TIME       = 30							# 买保险最大时间 (秒)



# 错误码
_OK_ERROR_                  = 10000       # 正常
_OPERATION_ERROR_           = -10001      # 通用错误
_SYSTEM_ERROR_              = -10000      # 系统错误
                            
_PARAM_ERROR_               = -11000      # 入参错误
_HAS_TABLE_ERROR_           = -11001      # 已经存在的赛桌
_TABLE_NOTFOUND_ERROR_      = -11002      # 不存在的赛桌
_NOT_ENOUGH_SEATS_ERROR_    = -11003      # 赛桌的座位不充足
_NOT_SYNC_STATE_ERROR_      = -11004      # 不是同步赛事规则的状态
_NOT_SIT_TABLE_ERROR_       = -11005      # 不允许玩家入座的桌子（锦标赛赛桌只能有赛事引导入座）
_NOTEXSIT_TABLE_TYPE_ERROR_ = -11006      # 不存在的赛桌类型 
                             
_QUEUE_NOHAS_ERROR_         = -11007      # 队列里没有该玩家
_HAS_SEAT_ERROR_            = -11008      # 还有空座，不需要加入等待
_JOINED_PLAYER_ERROR_       = -11009      # 已经加入等待的玩家
_HAS_JOINED_ERROR_          = -11010      # 已经进入赛桌                           
_NOTEXSIT_SEAT_ERROR_       = -11011      # 不存在的座位号
_USER_NOCHIPS_ERROR_        = -11012      # 玩家剩余筹码不足
_SEAT_NO_PLAYER_ERROR_      = -11013      # 该座位不存在玩家
_HAS_SEATED_POS_ERROR_      = -11014      # 该座位号已经有玩家
_PLAYER_NOHAS_SEAT_ERROR_   = -11015      # 该用户没有座位
_CAN_NOT_SHOW_DOWN_ERROR_   = -11016      # 该玩家没有亮牌的权利                           
_NOT_ACT_TABLE_TYPE_ERROR_  = -11017      # 不允许玩家操作的赛桌类型 
_SITED_PLAYER_ERROR_        = -11018      # 已经在该桌入座的玩家
_PLAYING_SIT_ERROR_         = -11019      # 在玩玩家离开不允许本手再次入座                           
                            
_NOT_TURN_YOU_ERROR_        = -11020      # 没有轮到你下注
_CAN_NOT_CHECK_ERROR_       = -11021      # 没有看牌权利
_FEW_CHIPS_RAISE_ERROR_     = -11022      # 加注筹码过少
_NOT_BET_STATE_ERROR_       = -11023      # 不在下注的状态 
_HAS_BET_ERROR_             = -11024      # 已经下注，重复下注
                            
_WRONG_AUTO_TYPE_ERROR_     = -11029      # 错误的设置类型
_NOT_ALLOW_BUY_ERROR_       = -11030      # 现在不允许兑换筹码 
_WRONG_CHIPS_BUY_ERROR_     = -11031      # 错误的购买筹码数
_TRUSTEE_BET_ERROR_         = -11032      # 托管下玩家操作错误


# 实现现金卓入座权限功能时增加的
REGISTER_CHANNEL_ERROR      = -11033      # 返回注册渠道验证失败错误
REGISTER_TIME_ERROR         = -11034      # 返回注册时间验证失败错误

MSG_SEQUENCE_ERROR          = -11041      # 接收到的sequence和牌桌当时的sequence不一致（目前还没用到）
_IS_SIT_OUT_ERROR_          = -11042      # 中途点击离座的玩家，不能再通过预选按钮来执行下注行为

_NOTEXSIT_CASH_TABLE_RULE_TYPE_ERROR_  = -11045   # 不存在的现金桌游戏规则类型配置
_NOTEXSIT_PAY_TYPE_ERROR_              = -11046   # 不存在的支付类型（silver, gold)

_IS_NOT_REBUY_ERROR_        = -11047      # 不是rebuy赛
_INIT_CHIPS_TOO_MANY_       = -11048      # rebuy时，当前牌局初始筹码大于设定值（赛事开始玩家初始筹码）
_BLIND_LEVEL_TOO_HIGH_      = -11049      # rebuy时，当前牌局的盲注级别大于设定值（赛事设定的盲注级别）
_is_ADDON_STATE_            = -11055      # addon期间不能rebuy

_ONLINE_IP_TOO_MANY_        = -11060      #同桌在线ip人数过多

_PRE_BUY_FAIL_            = -11065      #已经买过了一次筹码，本局结束后会添加
_PRE_BUY_SUC_            = -11066      #预买成功

_PASSWORD_ERROR_        =   -11070          #输入密码错误  

_TABLE_STATE_ERROR_            =    -12000        #    牌桌状态错误
_FAST_SIT_ERROR_            =    -12001        #新快速入座错误

_BALANCE_TOO_MANY_          = -12003       #总余额太多，不适合坐当前盲注级别的桌子

TIMES_LIMIT_ERROR           = -15020      #次数限制

VOTE_KICK_FAIL              = -17002      #投票踢人失败
VOTE_KICK_SUCCESS           = -17003
BEING_KICKED_OUT_RECORD     = -17004      #有被踢记录 
KICK_USER_NUM_ERR           = -17005      #只有1个人的时候怎么踢？
VOTING_NOT_END_ERR          = -17006      #上一轮投票未结束
_NOT_THE_TABLE_OWNER_       = -18001	  #

OUTS_LARGE_LIMIT_HALF_POT	= -19000	  # outs>=12时，限半pot

NOT_ENOUGH_CHIP_FOR_REDUCE  = -19100	  # 当前无足够筹码可供卸码
                    
                           
# 赛桌状态                 
TABLE_STATE_WAIT_SYNC      = 20000        # 等待赛事同步规则
TABLE_STATE_INIT           = 20001        # 初始
TABLE_STATE_SETBUTTON      = 20002        # 设置庄家
TABLE_STATE_WAIT_BLIND     = 20003        # 等待玩家下盲注和底注
TABLE_STATE_SET_FBETER     = 20004        # 设置第一位下注者
TABLE_STATE_HAND           = 20005        # 发手牌
TABLE_STATE_FIRST_BET      = 20006        # 荷官循环等待玩家下注
TABLE_STATE_FLOP           = 20007        # 发翻牌
TABLE_STATE_SECOND_BET     = 20008        # 荷官循环再次等待玩家下注
TABLE_STATE_TURN           = 20009        # 发转牌
TABLE_STATE_THIRD_BET      = 20010        # 荷官循环三次等待玩家下注
TABLE_STATE_RIVER          = 20011        # 发河牌
TABLE_STATE_FOURTH_BET     = 20012        # 荷官循环四次等待玩家下注 
TABLE_STATE_PRIZE          = 20013        # 荷官分配奖池
TABLE_STATE_SHOWDOWN       = 20014        # 荷官等待亮牌玩家亮牌
TABLE_STATE_END            = 20015        # 荷官清理牌桌,上传一手牌局信息
# added by jason
TABLE_STATE_PROTECTED      = 20016		  # 转牌前 激活保险态 
TABLE_STATE_PROTECTED_2    = 20017		  # 和牌前 激活保险态
                           
                           
# 玩家状态                 
PLAYER_STATE_INIT          = 30000        # 初始
PLAYER_STATE_REMAIN        = 30003        # 留座
PLAYER_STATE_CAN_PLAY      = 30005        # 可以比赛
PLAYER_STATE_PLAY          = 30006        # 比赛
PLAYER_STATE_ALLIN         = 30007        # allin
PLAYER_STATE_FOLD          = 30008        # 弃牌


# 玩家亮牌类型
SHOW_DOWN_NOT              = 0            # 不亮牌
SHOW_DOWN_FIRST            = 1            # 亮第一张
SHOW_DOWN_SECOND           = 2            # 亮第二张
SHOW_DOWN_ALL              = 3            # 亮所有的
                           
                           
# 德州扑克的牌型           
                           
ROYAL_FLUSH                = 9            # 皇家同花顺   
                           
STRAIGHT_FLUSH             = 8            # 同花顺
                           
FOUR_OF_A_KIND             = 7            # 四条
                           
BOAT_OR_FULL_HOUSE         = 6            # 葫芦
                           
FLUSH                      = 5            # 同花
                           
STAIGHT                    = 4            # 顺子
                           
THREE_OF_A_KIND            = 3            # 三条
                           
TWO_PAIRS                  = 2            # 两对
                           
PAIR                       = 1            # 一对
                           
HIGH_HAND                  = 0            # 高牌

FOLD_WIN                   = -1           # 其他玩家弃牌赢得

INVALID_CHIPS_WIN          = -2           # 无效筹码赢得

# 玩家自动缴纳盲注类型
AUTO_BLIND_ACCEPT_ALL             = 0            #自动支付新手盲、或者正常的前注、大盲注

AUTO_BLIND_REFUSE_NEWBLIND        = 1            #拒绝新手盲、但自动支付正常的前注、大盲注

AUTO_BLIND_REFUSE_ALL             = 2            #全部拒绝 – 拒绝新手盲，也拒绝正常的前注、小盲注、大盲注

AUTO_BLIND_REFUSE_BBLIND          = 3            # 只拒绝缴纳大盲注, 支付正常的前注和小盲注 ( 下一手大盲注离座 )

# 赛桌类型
TABLE_TYPE_TMT_SIT      =   'SITANDGO'     # 牌桌类型：坐满即玩
TABLE_TYPE_TMT_TIME     =   'TOURNEY'      # 牌桌类型：定时开打竞标赛
TABLE_TYPE_CASH         =   'CASH'         # 牌桌类型：现金赛

PASSIVE_RE_BUY_INIT     =   0              # 玩家被动rebuy：初始状态
PASSIVE_RE_BUY_YES      =   1              # 玩家被动rebuy: 成功被动rebuy
PASSIVE_RE_BUY_NO       =   2              # 玩家被动rebuy: 拒绝被动rebuy

REBUY_MODE_AUTO         =   0              # rebuy方式:自动rebuy
REBUY_MODE_NOT_AUTO     =   1              # rebuy方式:手动rebuy

PASSIVE_RE_BUY_PAUSE_TIME = 20             # 被动rebuy赛的暂停等待时间

#版本类型
FLASH                   = 'FLASH'          #flash版
PC                      = 'PC'             #
ANDROID                 = 'ANDROID'        #
IOS                     = 'IOS'            #

TABLE_OWNER_SYS            =    'sys'                #系统创建的桌子
PRE_REMIND_END_TIME     =   300             #提前5分钟，告诉玩家自创的桌上上面的牌桌即将销毁

FAST_ZHU_ZHAN       = 'COMMON'             #主站
FAST_ANDROID        = 'FAST'             #安卓

CHAT_COMMON              = 'COMMON'        #普通聊天
CHAT_ONLY_FALSH          = 'ONLY_FLASH'    #只flash客户端可以看到
CHAT_ALL                 = 'ALL'           #表情或道具，FLASH,MOBILE客户端兼容


#支持的牌桌买入币种
VALID_PAY_TYPE = (
    'GOLD',         #金币 
    'RAKEPOINT',    #积分
    'VGOLD',        #虚拟币，在德堡局中使用
    'POINT'         #POINT 德堡钻
)


# 增值服务类型
VALUE_ADDED_OPERA_DELAY     = 'OPERATION_DELAY'     #操作延时
VALUE_ADDED_VIEW_COMMON_CARD= 'VIEW_COMMON_CARD'    #看公共牌
VALUE_ADDED_KEEP_SEAT       = 'KEEP_SEAT'           #离桌留座
VALUE_ADDED_DELAY_TABLE_TIME= 'DELAY_TABLE'			#好友桌延时消耗  **jason**

