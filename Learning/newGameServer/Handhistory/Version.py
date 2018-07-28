#coding=gbk

#������ CHR -> INT
CMD = {
'PING':{'server':'CONN','code':'0x00000001','type':'C<->S','comment':'��·���'},
'PING_RESP':{'server':'CONN','code':'0x80000001','type':'C<->S','comment':'��·����Ӧ'},
'CONNECT':{'server':'CONN','code':'0x00000002','type':'C->S','comment':'���������������session��Ϣ��������'},
'CONNECT_RESP':{'server':'CONN','code':'0x80000002','type':'S->C','comment':'���ӻ�Ӧ�����أ��½��ģ�session��Ϣ'},
'QUIT':{'server':'CONN','code':'0x00000003','type':'C->S','comment':'�˳�����'},
'QUIT_RESP':{'server':'CONN','code':'0x80000003','type':'S->C','comment':'�˳���Ӧ'},
'CLOSED_BY_NEW':{'server':'CONN','code':'0x00000004','type':'S->C','comment':'���µ����ӽ������رձ�����'},
'LOGIN':{'server':'ACCT','code':'0x00050001','type':'C->S','comment':'��¼����'},
'LOGIN_RESP':{'server':'ACCT','code':'0x80050001','type':'S->C','comment':'��¼��Ӧ������ɹ��Ļ���Ҫ֪ͨuser��Ϣ�󶨵�session'},
'LOGOUT':{'server':'ACCT','code':'0x00050002','type':'C->S','comment':'�ǳ�����'},
'LOGOUT_RESP':{'server':'ACCT','code':'0x80050002','type':'S->C','comment':'�ǳ���Ӧ'},
'CREATE_ACCOUNT':{'server':'ACCT','code':'0x00050003','type':'C->S','comment':'�����˺ţ�ע�ᣩ'},
'CREATE_ACCOUNT_RESP':{'server':'ACCT','code':'0x80050003','type':'S->C','comment':'�����˺Ż�Ӧ'},
'USER_GET_INFO':{'server':'ACCT','code':'0x00050004','type':'C->S','comment':'��ȡ�û���Ϣ'},
'USER_GET_INFO_RESP':{'server':'ACCT','code':'0x80050004','type':'S->C','comment':'��ȡ�û���Ϣ��Ӧ'},
'MATCH_REGISTER':{'server':'MTCH','code':'0x00060001','type':'C->S','comment':'�Ǽǣ��μӣ����£���������'},
'MATCH_REGISTER_RESP':{'server':'MTCH','code':'0x80060001','type':'S->C','comment':'�Ǽǻ�Ӧ'},
'MATCH_UNREGISTER':{'server':'MTCH','code':'0x00060002','type':'C->S','comment':'�˳�����'},
'MATCH_UNREGISTER_RESP':{'server':'MTCH','code':'0x80060002','type':'S->C','comment':'�˳���Ӧ'},
'MATCH_LIST':{'server':'MTCH','code':'0x00060003','type':'C->S','comment':'�����б�'},
'MATCH_LIST_RESP':{'server':'MTCH','code':'0x80060003','type':'S->C','comment':'�б��Ӧ'},
'MATCH_GET_TABLE':{'server':'MTCH','code':'0x00060004','type':'C->S','comment':'��ȡ��������'},
'MATCH_GET_TABLE_RESP':{'server':'MTCH','code':'0x80060004','type':'S->C','comment':'���Ż�Ӧ'},
'MATCH_INFO':{'server':'MTCH','code':'0x00060005','type':'C->S','comment':'��ȡ������Ϣ'},
'MATCH_INFO_RESP':{'server':'MTCH','code':'0x80060005','type':'S->C','comment':'��ȡ������Ϣ��Ӧ'},
'ELIMINATED_MSG':{'server':'MTCH','code':'0x00060006','type':'S->C','comment':'��̭�����֣���Ϣ'},
'TABLE_LIST':{'server':'LOBB','code':'0x00010001','type':'C->S','comment':'��ȡ�����б�'},
'TABLE_LIST_RESP':{'server':'LOBB','code':'0x80010001','type':'S->C','comment':'��ȡ�����б��Ӧ'},
'TABLE_JOIN':{'server':'GAME','code':'0x00020001','type':'C->S','comment':'��������'},
'TABLE_JOIN_RESP':{'server':'GAME','code':'0x80020001','type':'S->C','comment':'����������Ӧ'},
'TABLE_LEAVE':{'server':'GAME','code':'0x00020002','type':'C->S','comment':'�뿪����'},
'TABLE_LEAVE_RESP':{'server':'GAME','code':'0x80020002','type':'S->C','comment':'�뿪������Ӧ'},
'TABLE_INFO':{'server':'GAME','code':'0x00020003','type':'C->S','comment':'��ȡ������Ϣ'},
'TABLE_INFO_RESP':{'server':'GAME','code':'0x80020003','type':'S->C','comment':'��ȡ������Ϣ��Ӧ'},
'SIT':{'server':'GAME','code':'0x00020004','type':'C->S','comment':'����'},
'SIT_MSG':{'server':'GAME','code':'0x80020004','type':'S=>C','comment':'������Ϣ'},
'SIT_OUT':{'server':'GAME','code':'0x00020005','type':'C->S','comment':'�뿪��λ'},
'SIT_OUT_MSG':{'server':'GAME','code':'0x80020005','type':'S=>C','comment':'�뿪��λ��Ϣ'},
'BUY_IN':{'server':'GAME','code':'0x00020006','type':'C->S','comment':'����'},
'BUY_IN_RESP':{'server':'GAME','code':'0x80020006','type':'S->C','comment':'�����Ӧ'},
'TABLE_MJOIN':{'server':'GAME','code':'0x00020007','type':'','comment':'���û������������ڲ��������ã�'},
'TABLE_MJOIN_RESP':{'server':'GAME','code':'0x80020007','type':'','comment':'���û�����������Ӧ'},
'TABLE_MLEAVE':{'server':'GAME','code':'0x00020008','type':'','comment':'���û������������ڲ��������ã�'},
'TABLE_MLEAVE_RESP':{'server':'GAME','code':'0x80020008','type':'','comment':'���û�����������Ӧ'},
'TABLE_CREATE':{'server':'GAME','code':'0x00020301','type':'','comment':'��������'},
'TABLE_CREATE_RESP':{'server':'GAME','code':'0x80020301','type':'','comment':'����������Ӧ'},
'TABLE_START':{'server':'GAME','code':'0x00020302','type':'','comment':'��������'},
'TABLE_START_RESP':{'server':'GAME','code':'0x80020302','type':'','comment':'����������Ӧ'},
'TABLE_PAUSE':{'server':'GAME','code':'0x00020303','type':'','comment':'��ͣ����'},
'TABLE_PAUSE_RESP':{'server':'GAME','code':'0x80020303','type':'','comment':'��ͣ������Ӧ'},
'TABLE_DESTROY':{'server':'GAME','code':'0x00020304','type':'','comment':'��������'},
'TABLE_DESTROY_RESP':{'server':'GAME','code':'0x80020304','type':'','comment':'����������Ӧ'},
'TABLE_SYNC_RULE':{'server':'GAME','code':'0x00020305','type':'','comment':'ͬ�����¹���'},
'TABLE_SYNC_RULE_RESP':{'server':'GAME','code':'0x80020305','type':'','comment':'ͬ�����¹����Ӧ'},
'TABLE_GUIDE':{'server':'GAME','code':'0x00020306','type':'S->C','comment':'�����û���������'},
'TABLE_GUIDE_RESP':{'server':'GAME','code':'0x80020306','type':'C->S','comment':'�����û�����������Ӧ'},
'CALL':{'server':'GAME','code':'0x00020101','type':'C->S','comment':'��ע'},
'CALL_MSG':{'server':'GAME','code':'0x80020101','type':'S=>C','comment':'��ע��Ϣ'},
'RAISE':{'server':'GAME','code':'0x00020102','type':'C->S','comment':'��ע'},
'RAISE_MSG':{'server':'GAME','code':'0x80020102','type':'S=>C','comment':'��ע��Ϣ'},
'FOLD':{'server':'GAME','code':'0x00020103','type':'C->S','comment':'����'},
'FOLD_MSG':{'server':'GAME','code':'0x80020103','type':'S=>C','comment':'������Ϣ'},
'CHECK':{'server':'GAME','code':'0x00020104','type':'C->S','comment':'����'},
'CHECK_MSG':{'server':'GAME','code':'0x80020104','type':'S=>C','comment':'������Ϣ'},
'ALL_IN':{'server':'GAME','code':'0x00020105','type':'C->S','comment':'allin'},
'ALL_IN_MSG':{'server':'GAME','code':'0x80020105','type':'S=>C','comment':'allin��Ϣ'},
'CANCEL_TRUSTEESHIP':{'server':'GAME','code':'0x00020106','type':'C->S','comment':'ȡ���й�'},
'CANCEL_TRUSTEESHIP_RESP':{'server':'GAME','code':'0x80020106','type':'S->C','comment':'ȡ���йܻ�Ӧ'},
'WAIT_FOR_MSG':{'server':'GAME','code':'0x00020201','type':'S=>C','comment':'���ڵȴ�˭����λ���û�id�ȣ�����������ʲô�¼���'},
'HAND_START_MSG':{'server':'GAME','code':'0x00020202','type':'S=>C','comment':'�����ƾֿ�ʼ'},
'POCKET_CARD':{'server':'GAME','code':'0x00020203','type':'S->C','comment':'����'},
'FLOP_CARD_MSG':{'server':'GAME','code':'0x00020204','type':'S=>C','comment':'����'},
'TURN_CARD_MSG':{'server':'GAME','code':'0x00020205','type':'S=>C','comment':'ת��'},
'RIVER_CARD_MSG':{'server':'GAME','code':'0x00020206','type':'S=>C','comment':'����'},
'SHOWDOWN_MSG':{'server':'GAME','code':'0x00020207','type':'S=>C','comment':'����'},
'POT_MSG':{'server':'GAME','code':'0x00020208','type':'S=>C','comment':'���أ��䶯����Ϣ'},
'PRIZE_MSG':{'server':'GAME','code':'0x00020209','type':'S=>C','comment':'�����أ��ɽ���Ϣ'},
'TABLE_SYNC_MSG':{'server':'GAME','code':'0x0002020A','type':'S=>C','comment':'ͬ��������Ϣ��ÿ�ֽ����Ժ�ͬ����Ϣ�����£�'},
'SELECT_BUTTON_MSG':{'server':'GAME','code':'0x0002020B','type':'S=>C','comment':'���ƾ���ׯ�ң������Ϣ'},
'TABLE_BLIND_MSG':{'server':'GAME','code':'0x0002020C','type':'S=>C','comment':'äע������Ϣ��Сä�ʹ�ä��Ϣ��'},
'TABLE_ANTE_MSG':{'server':'GAME','code':'0x0002020D','type':'S=>C','comment':'��ע������Ϣ'},
'TABLE_BUTTON_MSG':{'server':'GAME','code':'0x0002020E','type':'S=>C','comment':'ׯ��λ����Ϣ������Сä�ʹ�äλ�ã�'},
'TRUSTEESHIP_MSG':{'server':'GAME','code':'0x0002020F','type':'S=>C','comment':'�����й������Ϣ'},
'PLAYER_TIMEOUT_MSG':{'server':'GAME','code':'0x00020210','type':'S=>C','comment':'������ҳ�ʱ��Ϣ'}

}

#������ INT -> CHR
R_CMD = {}
for k in CMD.keys():
    R_CMD[ eval( CMD[k][ 'code' ] ) ] = k


PARAMETERS = {
'CODE':{'code':'0001','type':'integer','comment':'���������أ��룬���ձ����������'},
'SESSION_ID':{'code':'0002','type':'string','comment':'sessionid'},
'HEADER':{'code':'0003','type':'hash(dict)','comment':'��Ϣͷ'},
'BODY':{'code':'0004','type':'hash(dict)','comment':'��Ϣ��'},
'COMMAND_ID':{'code':'0005','type':'integer','comment':'ָ��id'},
'CONNECT_ID':{'code':'0006','type':'string','comment':'����id'},
'TIMESTAMP':{'code':'0007','type':'integer','comment':'unixʱ���'},
'SEQUENCE_ID':{'code':'0008','type':'integer','comment':'��ָ������кţ�ÿ��RESP���ص����к���Ҫ��ָ��������������к�һ��'},
'USER_AGENT':{'code':'0009','type':'string','comment':'�û������ͻ������Ͱ汾��ʶ��'},
'TABLE_LIST':{'code':'1001','type':'array(list)','comment':'�����嵥'},
'TABLE_ID':{'code':'1002','type':'string','comment':'����id'},
'TABLE_TYPE':{'code':'1003','type':'integer','comment':'��������'},
'GAME_SPEED':{'code':'1004','type':'integer','comment':'��Ϸ�ٶ�'},
'BLIND_INFO':{'code':'1005','type':'array(list)','comment':'äע��Ϣ'},
'ANTE':{'code':'1006','type':'integer','comment':'��ע'},
'TABLE_NAME':{'code':'1007','type':'string','comment':'��������'},
'TABLE_INFO':{'code':'1008','type':'hash(dict)','comment':'������Ϣ'},
'PLAYER_LIST':{'code':'2001','type':'array(list)','comment':'����嵥'},
'SEAT_NUM':{'code':'2002','type':'integer','comment':'��λ��'},
'USER_ID':{'code':'2003','type':'integer','comment':'�û�id'},
'USER_NAME':{'code':'2004','type':'string','comment':'�û���'},
'USER_CHIPS':{'code':'2005','type':'integer','comment':'�û�����'},
'HAND_ID':{'code':'2006','type':'integer','comment':'��һ�ֵ�id��ÿһ�ֶ�����Ψһ��id��'},
'DEALER_BUTTON':{'code':'2007','type':'integer','comment':'ׯ��'},
'SMALL_BLIND':{'code':'2008','type':'integer','comment':'Сä'},
'BIG_BLIND':{'code':'2009','type':'integer','comment':'��ä'},
'POT_INFO':{'code':'200A','type':'array(list)','comment':'������Ϣ'},
'COMMUNITY_CARDS':{'code':'200B','type':'array(list)','comment':'������'},
'BET_CHIPS':{'code':'200C','type':'integer','comment':'��ע����ע��������'},
'ROUND_CHIPS':{'code':'200D','type':'integer','comment':'��һȦ���֣�������'},
'HAND_CHIPS':{'code':'200E','type':'integer','comment':'��һ�ֳ�����'},
'SEAT_NO':{'code':'200F','type':'integer','comment':'��λ���'},
'GAME_STATUS':{'code':'2010','type':'string','comment':'��Ϸ״̬'},
'PLAYER_STATUS':{'code':'2011','type':'string','comment':'���״̬'},
'REMAIN_TIME':{'code':'2012','type':'integer','comment':'���ʣ����עʱ��'},
'BUTTON_NO':{'code':'2013','type':'integer','comment':'ׯ��λ��'},
'SBLIND_NO':{'code':'2014','type':'integer','comment':'Сäλ��'},
'BBLIND_NO':{'code':'2015','type':'integer','comment':'��äλ��'},
'WAIT_FOR_NO':{'code':'2016','type':'integer','comment':'�ֵ���ע�ߵ���λ��'},
'LAST_POTS':{'code':'2017','type':'array(list)','comment':'��һ�ֵ׳�'},
'CARD_LIST':{'code':'2018','type':'array(list)','comment':'�Ƶ��б����Ƶ�ʱ����'},
'PRIZE_LIST':{'code':'2019','type':'array(list)','comment':'�ɽ�list'},
'ABSENT_LIST':{'code':'201A','type':'array(list)','comment':'ȱϯ���ȴ���ң��б�'},
'WAITING_LIST':{'code':'201B','type':'array(list)','comment':'�Ŷ�����б�'},
'POCKET_CARDS':{'code':'201C','type':'array(list)','comment':'����'},
'REMOTE_NAME':{'code':'201D','type':'string','comment':'Զ�̷�����������Ŀǰ��remotename������group_name,server_name'},
'HANDS_NUM':{'code':'201E','type':'integer','comment':'���˶�����'},
'ANTE_INFO':{'code':'201F','type':'array(list)','comment':'����µĵ�ע��Ϣ'},
'CARD_TYPE':{'code':'2020','type':'integer','comment':'����'},
'MAX_CARD':{'code':'2021','type':'array(list)','comment':'������'},
'WIN_CHIPS':{'code':'2022','type':'integer','comment':'Ӯ�õĳ�����'},
'OPTIONAL_ACTIONS':{'code':'2023','type':'hash(dict)','comment':'��ѡ�Ĳ������ж���'},
'CALL':{'code':'2024','type':'integer','comment':'��ע�����٣�'},
'RAISE':{'code':'2025','type':'array(list)','comment':'��ע�����޺����ޣ�'},
'IS_TRUSTEE':{'code':'2026','type':'boolean','comment':'�Ƿ��й�'},
'IS_AUTO_BLIND':{'code':'2027','type':'boolean','comment':'�Ƿ��Զ�����äע'},
'IS_AUTO_ANTE':{'code':'2028','type':'boolean','comment':'�Ƿ��Զ����ɵ�ע'},
'MATCH_ID':{'code':'3001','type':'integer','comment':'����ID'},
'MATCH_NAME':{'code':'3002','type':'string','comment':'��������'},
'MATCH_TYPE':{'code':'3003','type':'integer','comment':'��������'},
'COMMON_RULE':{'code':'3004','type':'integer','comment':'��ͨ����'},
'SPECIFIC_RULE':{'code':'3005','type':'integer','comment':'�������'},
'TOURNEY_TYPE':{'code':'3006','type':'integer','comment':'����������'},
'START_TIME':{'code':'3007','type':'string','comment':'��ʼʱ��'},
'END_TIME':{'code':'3008','type':'string','comment':'����ʱ��'},
'MATCH_STATUS':{'code':'3009','type':'string','comment':'����״̬'},
'MIN_UNUM':{'code':'300A','type':'integer','comment':'��С��������'},
'MAX_UNUM':{'code':'300B','type':'integer','comment':'���������'},
'CUR_UNUM':{'code':'300C','type':'integer','comment':'��ǰ���ѱ���������'},
'PAY_INFO':{'code':'300D','type':'string','comment':'����֧����Ϣ'},
'USER_RANKING':{'code':'300E','type':'integer','comment':'�������'},
'CUR_TNUM':{'code':'300F','type':'integer','comment':'��ǰ������'},
'AWARDS':{'code':'3010','type':'array(list)','comment':'��Ʒ'},
'BLIND_LEVEL':{'code':'3011','type':'integer','comment':'äע�ȼ�'},
'PRIZE_NAME':{'code':'3012','type':'string','comment':'��Ʒ����'},
'PRIZE_DESC':{'code':'3013','type':'string','comment':'��Ʒ����'},
'PRIZE_BEGIN_RANK':{'code':'3014','type':'integer','comment':'���˷�Χ����'},
'PRIZE_END_RANK':{'code':'3015','type':'integer','comment':'���˷�Χ����'},
'PLAYERS_RANGE_MIN':{'code':'3016','type':'integer','comment':'����������Χ����'},
'PLAYERS_RANGE_MAX':{'code':'3017','type':'integer','comment':'����������Χ����'},
'RESOURCE_TYPE':{'code':'3018','type':'string','comment':'��Դ����'},
'PRIZE_POOL':{'code':'3019','type':'integer','comment':'�ʳ�'},
'INIT_CHIPS':{'code':'301A','type':'integer','comment':'��ʼ����'},
'WAITING_UNUM':{'code':'301B','type':'integer','comment':'�ȴ��б��������'},
'ANNOUNCE_TIME':{'code':'301C','type':'string','comment':'����ͨ��ʱ��'},
'REG_BEGIN_TIME':{'code':'301D','type':'string','comment':'������ʼʱ��'},
'REG_DELAY_TIME':{'code':'301E','type':'integer','comment':'�ӳٱ���ʱ��'},
'MIN_UCHIPS':{'code':'301F','type':'integer','comment':'�����ҳ�����'},
'MAX_UCHIPS':{'code':'3020','type':'integer','comment':'�����ҳ�����'},
'BLIND_TYPE':{'code':'3021','type':'string','comment':'äע����'},
'REG_STATUS':{'code':'3022','type':'integer','comment':'����״̬'},
'BLIND_DURATION':{'code':'3023','type':'integer','comment':'��äʱ��'},
'PASSWORD':{'code':'4001','type':'string','comment':'����'},
'USER_TYPE':{'code':'4002','type':'integer','comment':'�û�����'},
'USER_STATUS':{'code':'4003','type':'string','comment':'�û�״̬'},
'MOD_TIME':{'code':'4004','type':'string','comment':'������޸�ʱ��'},
'CRT_TIME':{'code':'4005','type':'string','comment':'��������ӣ�ʱ��'},
'MONEY_BALANCE':{'code':'4006','type':'float','comment':'���'},
'ADMIN_NAME':{'code':'4007','type':'string','comment':'����Ա������Ա������'},
'ADMIN_NOTE':{'code':'4008','type':'string','comment':'����������˵��'},
'ORDER_ID':{'code':'4009','type':'integer','comment':'����ϵͳ���׶�����'}
}

R_PARAMETERS = {}
for k in PARAMETERS.keys():
    R_PARAMETERS[PARAMETERS[k]['code']] = k

#��װ
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

#����
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


