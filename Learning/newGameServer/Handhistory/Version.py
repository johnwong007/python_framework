#coding=gbk

#命令字 CHR -> INT
CMD = {
'PING':{'server':'CONN','code':'0x00000001','type':'C<->S','comment':'链路检查'},
'PING_RESP':{'server':'CONN','code':'0x80000001','type':'C<->S','comment':'链路检查回应'},
'CONNECT':{'server':'CONN','code':'0x00000002','type':'C->S','comment':'连接请求，如果带有session信息代表重连'},
'CONNECT_RESP':{'server':'CONN','code':'0x80000002','type':'S->C','comment':'连接回应，返回（新建的）session信息'},
'QUIT':{'server':'CONN','code':'0x00000003','type':'C->S','comment':'退出服务'},
'QUIT_RESP':{'server':'CONN','code':'0x80000003','type':'S->C','comment':'退出回应'},
'CLOSED_BY_NEW':{'server':'CONN','code':'0x00000004','type':'S->C','comment':'有新的连接建立，关闭本连接'},
'LOGIN':{'server':'ACCT','code':'0x00050001','type':'C->S','comment':'登录请求'},
'LOGIN_RESP':{'server':'ACCT','code':'0x80050001','type':'S->C','comment':'登录回应，如果成功的话需要通知user信息绑定到session'},
'LOGOUT':{'server':'ACCT','code':'0x00050002','type':'C->S','comment':'登出请求'},
'LOGOUT_RESP':{'server':'ACCT','code':'0x80050002','type':'S->C','comment':'登出回应'},
'CREATE_ACCOUNT':{'server':'ACCT','code':'0x00050003','type':'C->S','comment':'创建账号（注册）'},
'CREATE_ACCOUNT_RESP':{'server':'ACCT','code':'0x80050003','type':'S->C','comment':'创建账号回应'},
'USER_GET_INFO':{'server':'ACCT','code':'0x00050004','type':'C->S','comment':'获取用户信息'},
'USER_GET_INFO_RESP':{'server':'ACCT','code':'0x80050004','type':'S->C','comment':'获取用户信息回应'},
'MATCH_REGISTER':{'server':'MTCH','code':'0x00060001','type':'C->S','comment':'登记（参加）赛事（锦标赛）'},
'MATCH_REGISTER_RESP':{'server':'MTCH','code':'0x80060001','type':'S->C','comment':'登记回应'},
'MATCH_UNREGISTER':{'server':'MTCH','code':'0x00060002','type':'C->S','comment':'退出比赛'},
'MATCH_UNREGISTER_RESP':{'server':'MTCH','code':'0x80060002','type':'S->C','comment':'退出回应'},
'MATCH_LIST':{'server':'MTCH','code':'0x00060003','type':'C->S','comment':'赛事列表'},
'MATCH_LIST_RESP':{'server':'MTCH','code':'0x80060003','type':'S->C','comment':'列表回应'},
'MATCH_GET_TABLE':{'server':'MTCH','code':'0x00060004','type':'C->S','comment':'获取比赛桌号'},
'MATCH_GET_TABLE_RESP':{'server':'MTCH','code':'0x80060004','type':'S->C','comment':'桌号回应'},
'MATCH_INFO':{'server':'MTCH','code':'0x00060005','type':'C->S','comment':'获取赛事信息'},
'MATCH_INFO_RESP':{'server':'MTCH','code':'0x80060005','type':'S->C','comment':'获取赛事信息回应'},
'ELIMINATED_MSG':{'server':'MTCH','code':'0x00060006','type':'S->C','comment':'淘汰（出局）消息'},
'TABLE_LIST':{'server':'LOBB','code':'0x00010001','type':'C->S','comment':'获取牌桌列表'},
'TABLE_LIST_RESP':{'server':'LOBB','code':'0x80010001','type':'S->C','comment':'获取牌桌列表回应'},
'TABLE_JOIN':{'server':'GAME','code':'0x00020001','type':'C->S','comment':'加入牌桌'},
'TABLE_JOIN_RESP':{'server':'GAME','code':'0x80020001','type':'S->C','comment':'加入牌桌回应'},
'TABLE_LEAVE':{'server':'GAME','code':'0x00020002','type':'C->S','comment':'离开牌桌'},
'TABLE_LEAVE_RESP':{'server':'GAME','code':'0x80020002','type':'S->C','comment':'离开牌桌回应'},
'TABLE_INFO':{'server':'GAME','code':'0x00020003','type':'C->S','comment':'获取牌桌信息'},
'TABLE_INFO_RESP':{'server':'GAME','code':'0x80020003','type':'S->C','comment':'获取牌桌信息回应'},
'SIT':{'server':'GAME','code':'0x00020004','type':'C->S','comment':'坐下'},
'SIT_MSG':{'server':'GAME','code':'0x80020004','type':'S=>C','comment':'坐下消息'},
'SIT_OUT':{'server':'GAME','code':'0x00020005','type':'C->S','comment':'离开座位'},
'SIT_OUT_MSG':{'server':'GAME','code':'0x80020005','type':'S=>C','comment':'离开座位消息'},
'BUY_IN':{'server':'GAME','code':'0x00020006','type':'C->S','comment':'买入'},
'BUY_IN_RESP':{'server':'GAME','code':'0x80020006','type':'S->C','comment':'买入回应'},
'TABLE_MJOIN':{'server':'GAME','code':'0x00020007','type':'','comment':'把用户带入牌桌（内部服务间调用）'},
'TABLE_MJOIN_RESP':{'server':'GAME','code':'0x80020007','type':'','comment':'把用户带入牌桌回应'},
'TABLE_MLEAVE':{'server':'GAME','code':'0x00020008','type':'','comment':'把用户带离牌桌（内部服务间调用）'},
'TABLE_MLEAVE_RESP':{'server':'GAME','code':'0x80020008','type':'','comment':'把用户带离牌桌回应'},
'TABLE_CREATE':{'server':'GAME','code':'0x00020301','type':'','comment':'创建牌桌'},
'TABLE_CREATE_RESP':{'server':'GAME','code':'0x80020301','type':'','comment':'创建牌桌回应'},
'TABLE_START':{'server':'GAME','code':'0x00020302','type':'','comment':'启动赛桌'},
'TABLE_START_RESP':{'server':'GAME','code':'0x80020302','type':'','comment':'启动赛桌回应'},
'TABLE_PAUSE':{'server':'GAME','code':'0x00020303','type':'','comment':'暂停赛桌'},
'TABLE_PAUSE_RESP':{'server':'GAME','code':'0x80020303','type':'','comment':'暂停赛桌回应'},
'TABLE_DESTROY':{'server':'GAME','code':'0x00020304','type':'','comment':'销毁赛桌'},
'TABLE_DESTROY_RESP':{'server':'GAME','code':'0x80020304','type':'','comment':'销毁赛桌回应'},
'TABLE_SYNC_RULE':{'server':'GAME','code':'0x00020305','type':'','comment':'同步赛事规则'},
'TABLE_SYNC_RULE_RESP':{'server':'GAME','code':'0x80020305','type':'','comment':'同步赛事规则回应'},
'TABLE_GUIDE':{'server':'GAME','code':'0x00020306','type':'S->C','comment':'引导用户加入赛桌'},
'TABLE_GUIDE_RESP':{'server':'GAME','code':'0x80020306','type':'C->S','comment':'引导用户加入赛桌回应'},
'CALL':{'server':'GAME','code':'0x00020101','type':'C->S','comment':'跟注'},
'CALL_MSG':{'server':'GAME','code':'0x80020101','type':'S=>C','comment':'跟注消息'},
'RAISE':{'server':'GAME','code':'0x00020102','type':'C->S','comment':'加注'},
'RAISE_MSG':{'server':'GAME','code':'0x80020102','type':'S=>C','comment':'加注消息'},
'FOLD':{'server':'GAME','code':'0x00020103','type':'C->S','comment':'弃牌'},
'FOLD_MSG':{'server':'GAME','code':'0x80020103','type':'S=>C','comment':'弃牌消息'},
'CHECK':{'server':'GAME','code':'0x00020104','type':'C->S','comment':'看牌'},
'CHECK_MSG':{'server':'GAME','code':'0x80020104','type':'S=>C','comment':'看牌消息'},
'ALL_IN':{'server':'GAME','code':'0x00020105','type':'C->S','comment':'allin'},
'ALL_IN_MSG':{'server':'GAME','code':'0x80020105','type':'S=>C','comment':'allin消息'},
'CANCEL_TRUSTEESHIP':{'server':'GAME','code':'0x00020106','type':'C->S','comment':'取消托管'},
'CANCEL_TRUSTEESHIP_RESP':{'server':'GAME','code':'0x80020106','type':'S->C','comment':'取消托管回应'},
'WAIT_FOR_MSG':{'server':'GAME','code':'0x00020201','type':'S=>C','comment':'正在等待谁（座位号用户id等）操作（或者什么事件）'},
'HAND_START_MSG':{'server':'GAME','code':'0x00020202','type':'S=>C','comment':'这手牌局开始'},
'POCKET_CARD':{'server':'GAME','code':'0x00020203','type':'S->C','comment':'手牌'},
'FLOP_CARD_MSG':{'server':'GAME','code':'0x00020204','type':'S=>C','comment':'翻牌'},
'TURN_CARD_MSG':{'server':'GAME','code':'0x00020205','type':'S=>C','comment':'转牌'},
'RIVER_CARD_MSG':{'server':'GAME','code':'0x00020206','type':'S=>C','comment':'河牌'},
'SHOWDOWN_MSG':{'server':'GAME','code':'0x00020207','type':'S=>C','comment':'亮牌'},
'POT_MSG':{'server':'GAME','code':'0x00020208','type':'S=>C','comment':'奖池（变动）消息'},
'PRIZE_MSG':{'server':'GAME','code':'0x00020209','type':'S=>C','comment':'（奖池）派奖消息'},
'TABLE_SYNC_MSG':{'server':'GAME','code':'0x0002020A','type':'S=>C','comment':'同步牌桌信息（每手结束以后同步信息到赛事）'},
'SELECT_BUTTON_MSG':{'server':'GAME','code':'0x0002020B','type':'S=>C','comment':'抽牌决定庄家，结果信息'},
'TABLE_BLIND_MSG':{'server':'GAME','code':'0x0002020C','type':'S=>C','comment':'盲注缴纳消息（小盲和大盲信息）'},
'TABLE_ANTE_MSG':{'server':'GAME','code':'0x0002020D','type':'S=>C','comment':'底注缴纳消息'},
'TABLE_BUTTON_MSG':{'server':'GAME','code':'0x0002020E','type':'S=>C','comment':'庄家位置信息（包括小盲和大盲位置）'},
'TRUSTEESHIP_MSG':{'server':'GAME','code':'0x0002020F','type':'S=>C','comment':'处理托管玩家消息'},
'PLAYER_TIMEOUT_MSG':{'server':'GAME','code':'0x00020210','type':'S=>C','comment':'处理玩家超时消息'}

}

#命令字 INT -> CHR
R_CMD = {}
for k in CMD.keys():
    R_CMD[ eval( CMD[k][ 'code' ] ) ] = k


PARAMETERS = {
'CODE':{'code':'0001','type':'integer','comment':'操作（返回）码，对照表待定。。。'},
'SESSION_ID':{'code':'0002','type':'string','comment':'sessionid'},
'HEADER':{'code':'0003','type':'hash(dict)','comment':'消息头'},
'BODY':{'code':'0004','type':'hash(dict)','comment':'消息体'},
'COMMAND_ID':{'code':'0005','type':'integer','comment':'指令id'},
'CONNECT_ID':{'code':'0006','type':'string','comment':'连接id'},
'TIMESTAMP':{'code':'0007','type':'integer','comment':'unix时间戳'},
'SEQUENCE_ID':{'code':'0008','type':'integer','comment':'本指令的序列号，每次RESP返回的序列号需要跟指令请求过来的序列号一致'},
'USER_AGENT':{'code':'0009','type':'string','comment':'用户代理（客户端类型版本标识）'},
'TABLE_LIST':{'code':'1001','type':'array(list)','comment':'牌桌清单'},
'TABLE_ID':{'code':'1002','type':'string','comment':'牌桌id'},
'TABLE_TYPE':{'code':'1003','type':'integer','comment':'牌桌类型'},
'GAME_SPEED':{'code':'1004','type':'integer','comment':'游戏速度'},
'BLIND_INFO':{'code':'1005','type':'array(list)','comment':'盲注信息'},
'ANTE':{'code':'1006','type':'integer','comment':'底注'},
'TABLE_NAME':{'code':'1007','type':'string','comment':'牌桌名称'},
'TABLE_INFO':{'code':'1008','type':'hash(dict)','comment':'牌桌信息'},
'PLAYER_LIST':{'code':'2001','type':'array(list)','comment':'玩家清单'},
'SEAT_NUM':{'code':'2002','type':'integer','comment':'座位数'},
'USER_ID':{'code':'2003','type':'integer','comment':'用户id'},
'USER_NAME':{'code':'2004','type':'string','comment':'用户名'},
'USER_CHIPS':{'code':'2005','type':'integer','comment':'用户筹码'},
'HAND_ID':{'code':'2006','type':'integer','comment':'这一手的id（每一手都会有唯一的id）'},
'DEALER_BUTTON':{'code':'2007','type':'integer','comment':'庄家'},
'SMALL_BLIND':{'code':'2008','type':'integer','comment':'小盲'},
'BIG_BLIND':{'code':'2009','type':'integer','comment':'大盲'},
'POT_INFO':{'code':'200A','type':'array(list)','comment':'奖池信息'},
'COMMUNITY_CARDS':{'code':'200B','type':'array(list)','comment':'公共牌'},
'BET_CHIPS':{'code':'200C','type':'integer','comment':'下注（加注）筹码数'},
'ROUND_CHIPS':{'code':'200D','type':'integer','comment':'这一圈（街）筹码数'},
'HAND_CHIPS':{'code':'200E','type':'integer','comment':'这一手筹码数'},
'SEAT_NO':{'code':'200F','type':'integer','comment':'座位编号'},
'GAME_STATUS':{'code':'2010','type':'string','comment':'游戏状态'},
'PLAYER_STATUS':{'code':'2011','type':'string','comment':'玩家状态'},
'REMAIN_TIME':{'code':'2012','type':'integer','comment':'玩家剩余下注时间'},
'BUTTON_NO':{'code':'2013','type':'integer','comment':'庄家位置'},
'SBLIND_NO':{'code':'2014','type':'integer','comment':'小盲位置'},
'BBLIND_NO':{'code':'2015','type':'integer','comment':'大盲位置'},
'WAIT_FOR_NO':{'code':'2016','type':'integer','comment':'轮到下注者的座位号'},
'LAST_POTS':{'code':'2017','type':'array(list)','comment':'上一街底池'},
'CARD_LIST':{'code':'2018','type':'array(list)','comment':'牌的列表，亮牌的时候用'},
'PRIZE_LIST':{'code':'2019','type':'array(list)','comment':'派奖list'},
'ABSENT_LIST':{'code':'201A','type':'array(list)','comment':'缺席（等待玩家）列表'},
'WAITING_LIST':{'code':'201B','type':'array(list)','comment':'排队玩家列表'},
'POCKET_CARDS':{'code':'201C','type':'array(list)','comment':'手牌'},
'REMOTE_NAME':{'code':'201D','type':'string','comment':'远程服务名，就是目前的remotename，包括group_name,server_name'},
'HANDS_NUM':{'code':'201E','type':'integer','comment':'打了多少手'},
'ANTE_INFO':{'code':'201F','type':'array(list)','comment':'玩家下的底注信息'},
'CARD_TYPE':{'code':'2020','type':'integer','comment':'牌型'},
'MAX_CARD':{'code':'2021','type':'array(list)','comment':'最大的牌'},
'WIN_CHIPS':{'code':'2022','type':'integer','comment':'赢得的筹码数'},
'OPTIONAL_ACTIONS':{'code':'2023','type':'hash(dict)','comment':'可选的操作（行动）'},
'CALL':{'code':'2024','type':'integer','comment':'跟注（多少）'},
'RAISE':{'code':'2025','type':'array(list)','comment':'加注（下限和上限）'},
'IS_TRUSTEE':{'code':'2026','type':'boolean','comment':'是否托管'},
'IS_AUTO_BLIND':{'code':'2027','type':'boolean','comment':'是否自动缴纳盲注'},
'IS_AUTO_ANTE':{'code':'2028','type':'boolean','comment':'是否自动缴纳底注'},
'MATCH_ID':{'code':'3001','type':'integer','comment':'赛事ID'},
'MATCH_NAME':{'code':'3002','type':'string','comment':'赛事名称'},
'MATCH_TYPE':{'code':'3003','type':'integer','comment':'赛事类型'},
'COMMON_RULE':{'code':'3004','type':'integer','comment':'普通规则'},
'SPECIFIC_RULE':{'code':'3005','type':'integer','comment':'特殊规则'},
'TOURNEY_TYPE':{'code':'3006','type':'integer','comment':'锦标赛类型'},
'START_TIME':{'code':'3007','type':'string','comment':'开始时间'},
'END_TIME':{'code':'3008','type':'string','comment':'结束时间'},
'MATCH_STATUS':{'code':'3009','type':'string','comment':'赛事状态'},
'MIN_UNUM':{'code':'300A','type':'integer','comment':'最小开赛人数'},
'MAX_UNUM':{'code':'300B','type':'integer','comment':'最大报名人数'},
'CUR_UNUM':{'code':'300C','type':'integer','comment':'当前（已报名）人数'},
'PAY_INFO':{'code':'300D','type':'string','comment':'报名支付信息'},
'USER_RANKING':{'code':'300E','type':'integer','comment':'玩家排名'},
'CUR_TNUM':{'code':'300F','type':'integer','comment':'当前牌桌数'},
'AWARDS':{'code':'3010','type':'array(list)','comment':'奖品'},
'BLIND_LEVEL':{'code':'3011','type':'integer','comment':'盲注等级'},
'PRIZE_NAME':{'code':'3012','type':'string','comment':'奖品名称'},
'PRIZE_DESC':{'code':'3013','type':'string','comment':'奖品描述'},
'PRIZE_BEGIN_RANK':{'code':'3014','type':'integer','comment':'获奖人范围上限'},
'PRIZE_END_RANK':{'code':'3015','type':'integer','comment':'获奖人范围下限'},
'PLAYERS_RANGE_MIN':{'code':'3016','type':'integer','comment':'参赛人数范围上限'},
'PLAYERS_RANGE_MAX':{'code':'3017','type':'integer','comment':'参赛人数范围下限'},
'RESOURCE_TYPE':{'code':'3018','type':'string','comment':'资源组名'},
'PRIZE_POOL':{'code':'3019','type':'integer','comment':'彩池'},
'INIT_CHIPS':{'code':'301A','type':'integer','comment':'初始筹码'},
'WAITING_UNUM':{'code':'301B','type':'integer','comment':'等待列表玩家人数'},
'ANNOUNCE_TIME':{'code':'301C','type':'string','comment':'比赛通告时间'},
'REG_BEGIN_TIME':{'code':'301D','type':'string','comment':'报名开始时间'},
'REG_DELAY_TIME':{'code':'301E','type':'integer','comment':'延迟报名时间'},
'MIN_UCHIPS':{'code':'301F','type':'integer','comment':'最低玩家筹码数'},
'MAX_UCHIPS':{'code':'3020','type':'integer','comment':'最高玩家筹码数'},
'BLIND_TYPE':{'code':'3021','type':'string','comment':'盲注类型'},
'REG_STATUS':{'code':'3022','type':'integer','comment':'报名状态'},
'BLIND_DURATION':{'code':'3023','type':'integer','comment':'升盲时间'},
'PASSWORD':{'code':'4001','type':'string','comment':'密码'},
'USER_TYPE':{'code':'4002','type':'integer','comment':'用户类型'},
'USER_STATUS':{'code':'4003','type':'string','comment':'用户状态'},
'MOD_TIME':{'code':'4004','type':'string','comment':'（最后）修改时间'},
'CRT_TIME':{'code':'4005','type':'string','comment':'创建（添加）时间'},
'MONEY_BALANCE':{'code':'4006','type':'float','comment':'余额'},
'ADMIN_NAME':{'code':'4007','type':'string','comment':'管理员（操作员）名称'},
'ADMIN_NOTE':{'code':'4008','type':'string','comment':'管理（操作）说明'},
'ORDER_ID':{'code':'4009','type':'integer','comment':'账务系统交易订单号'}
}

R_PARAMETERS = {}
for k in PARAMETERS.keys():
    R_PARAMETERS[PARAMETERS[k]['code']] = k

#组装
def formator(inp):
    if type(inp) == dict:
        newDic = {}
        for k in inp:
            newDic[PARAMETERS.get(k, {'code':k})['code']] = formator(inp[k])
        return newDic
    elif type(inp) == list:
        newList = []
        for v in inp:
            newList.append(formator(v))
        return newList
    else:
        return inp

#解析
def deformator(inp):
    if type(inp) == dict:
        newDic = {}
        for k in inp:
            newDic[R_PARAMETERS.get(k, k)] = deformator(inp[k])
        return newDic
    elif type(inp) == list:
        newList = []
        for v in inp:
            newList.append(deformator(v))
        return newList
    else:
        return inp


