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
SAVE_MATCH_PLAYER_STAT  = 0x00010004        #����֪ͨ���������û�����ͳ�����ݣ��ܵ��������ܵı���ˮ���ȣ�
REBUY_BACK_MONEY        = 0x00010005        #֪ͨ���������������rebuy�����Ǯ
REPEAT_APPLY_BACKMONEY  = 0x00010006        #���ظ���������˿�
NOTIFY_MATCH_REGISTER   = 0x00010007        #����֪ͨ�����б������Ա�����
APPLY_MATCH_NOTIFY      = 0x00010008       #����֪ͨ��������ұ����˱���
NOTIFY_MATCH_START      = 0x00010009        #����֪ͨ�����б�����ʼ��
NOTIFY_MATCH_END        = 0x0001000B        #����֪ͨ�����б���������


TABLE_JOIN              = 0x00020001    #��������          131073
TABLE_JOIN_RESP         = 0x80020001    #����������Ӧ      2147614721
TABLE_LEAVE             = 0x00020002    #�뿪����          131074
TABLE_LEAVE_RESP        = 0x80020002    #�뿪������Ӧ      2147614722
TABLE_INFO              = 0x00020003    #��ȡ������Ϣ      131075
TABLE_INFO_RESP         = 0x80020003    #��ȡ������Ϣ��Ӧ  2147614723 2147614723
SIT                     = 0x00020004    #����  
SIT_MSG                 = 0x80020004    #������Ϣ        2147614724
SIT_OUT                 = 0x00020005    #�뿪��λ      131077 
SIT_OUT_MSG             = 0x80020005    #�뿪��λ��Ϣ  2147614725
BUY_IN                  = 0x00020006    #����
BUY_IN_RESP             = 0x80020006    #�����Ӧ
TABLE_MJOIN             = 0x00020007    #���û������������ڲ��������ã�
TABLE_MJOIN_RESP        = 0x80020007    #���û�����������Ӧ
TABLE_MLEAVE            = 0x00020008    #���û������������ڲ��������ã�
TABLE_MLEAVE_RESP       = 0x80020008    #���û�����������Ӧ
BUY_CHIPS_PLAYER        = 0x00020009    #����֪ͨ��Ϸ�����û�������루���붩��ID������ID���û�ID��131081
BUY_CHIPS_PLAYER_RESP   = 0x80020009    #����֪ͨ��Ϸ�����û���������Ӧ 2147614729
JOIN_QUEUE_RESP         = 0x8002000B
QUIT_QUEUE_RESP         = 0x8002000C          #ȡ���ȴ���Ӧ

# ����ļ���ܶ�����Ķ����Ӧgame�������lib/Protocal/command.py
TABLE_SYNC_MSG          = 0x0002020A    #ͬ��������Ϣ��ÿ�ֽ����Ժ�ͬ����Ϣ�����£� 131594
TABLE_CREATE            = 0x00020301    #��������
TABLE_CREATE_RESP       = 0x80020301    #����������Ӧ
TABLE_START             = 0x00020302    #��������
TABLE_START_RESP        = 0x80020302    #����������Ӧ
TABLE_DESTROY           = 0x00020304    #��������
TABLE_DESTROY_RESP      = 0x80020304    #����������Ӧ
TABLE_SYNC_RULE         = 0x00020305    #ͬ�����¹��� 
TABLE_SYNC_RULE_RESP    = 0x80020305    #ͬ�����¹����Ӧ
TABLE_GUIDE             = 0x00020306    #�����û���������
TABLE_GUIDE_RESP        = 0x80020306    #�����û�����������Ӧ
TABLE_PAUSE             = 0x00020303    #֪ͨ���������ͣ
TABLE_ADDON             = 0x00020308    #֪ͨGame������ʼaddon
TABLE_WAIT_ADDON        = 0x00020309    #�ȴ���������ͣ����addon
DESTROY_CASH_TABLE      = 0x0002030C    #�����ֽ���

REPORT_REDUCE_CHIPS_INFO = 0x00020400   # �ϱ�ж�������Ϣ


#����Ȩ��У��,����ָ��
SIT_PERMISSION_VERIFY           = 0x0002000F        #��������Ȩ���ж�
SIT_WAITING_VERIFY_FINISH       = 0x8002000F        #����Ȩ���жϻظ�ָ��
JOIN_WAITING_VERIFY             = 0x00020010        #�����ж��Ƿ���Ȩ�޼���ȴ��б�
JOIN_WAITING_VERIFY_FINISH      = 0x80020010        #���������ȴ��б�Ȩ���жϻظ�ָ��

FOLD_MATCH                      = 0x00020012        #���������� 131090 

MATCH_PLAYER_REBUY              = 0x00020110         #����rebuy����
REBUY_CHIPS_FINISH              = 0x80020110         #������rebuy����,������Ӧ
REQUEST_REBUY                   = 0x00020111         #�����������rebuy
ADDON_FINISH                    = 0x00020112         #addon����������ظ�Match
VALUE_ADDED_REPORT              = 0x00020235         #ʹ����ֵ�������ѱ���
DESTORY_TABLE_BACK_MONEY        = 0x00020238         #������ǰ��������ʱ������
MATCH_PT_ADJUST_PUSH            = 0x00020319         # ͨ��match���汣�ճط����б�



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
BUY_CHIPS_FINISH        = 0x00060008    # ����֪ͨ���£����û��������
BUY_CHIPS_FINISH_RESP   = 0x80060008 
CASH_TABLE_GUIDE        = 0x0006000E    #�����������
USER_CREATE_TABLE       = 0x0006000F    # ��Ҵ�������

KICK_USER_CARD_REQ      = 0x00060010 
JOIN_TABLE_ASYNC_NOTIFY = 0x00060011    #���¼����������첽֪ͨ
MATCH_DELAY_APPLY       = 0x00060012    #�ӳٱ�������
TABLE_WAIT_MSG          = 0x00060013    #֪ͨ��������ҵȺ����Ϣ
BUYIN_APPLY             = 0x00060014    #��������
BUYIN_APPLY_RESP        = 0x80060014    #��������
USER_START_MATCH        = 0x00060015    #�Զ����������������������
VALUE_ADDED_DEDUCT_NOTIFY = 0x00060016  #��ֵ����۷�֪ͨ
DESTORY_TABLE_BACK_NOTIFY = 0x00060017  #��ǰ�������ӷ�����֪ͨ
REAL_USER_APPLY_BUYIN   = 0x00060018    #��׼������ʵ�ۿ�





CODE                = '0001'
CONN_ID             = '0002' 
HEAD                = '0003'
BODY                = '0004'
COMMAND_ID          = '0005'
CONNECT_ID          = '0006'
TIMESTAMP           = '0007'
SEQUENCE_ID         = '0008'
USER_AGENT          = '0009'             #�ͻ��˰汾
 
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
INS_STATE           = '110F'                # ���չ���״̬
SUB_TABLE_TYPE      = '1110'
AUTO_BLIND          = '1111'
BOTT_BBTIMES        = '1112'             # ׯǰעBB����
PK_FIRST_BET             = '1113'            # PKʱ�޸�Ĭ�Ϲ���  0:Ĭ��   1:�޸�
COMSUMP_TYPE        = '1114'
PUMP_RATE           = '1115'
REDU_CHIP_FLAG           = '1116'             # 6+ж�빦���Ƿ��� 
REDU_CHIP_LIMIT          = '1117'             # 6+ж���Ƚ���
REDU_CHIP_SERVICE_RATE   = '1118'             # 6+ж��������(�ٷֱ�)
CARD_COMPARE_TYPE           = '111E'             # �����������ͣ�0:��ͨ������1:6+,22:6+��ʽ
APPLY_BUYIN_OPEN    = '12E0'                  # �Ƿ�����׼���빦��
PT_POT_OPEN         = '12E1'                  # �Ƿ��б��ճط��书��

LEFT_COMMUNITY_CARDS        = '2000'             #ʣ�๫���� 
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
HANDS_NUM           = '201E'             #�������˵ڼ���
WIN_CHIPS           = '2022'
IS_TRUSTEE          = '2026'             #����Ƿ��й�
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
PLAYER_ONLINE_IP    = '2061'			#�������ip
REWARD_OUT_INFO     = '2074'            #ÿ��pot�л�ʤ�߼�allin���uid�б�
APPLY_UID           = '2075'

CHIPS_SITOUT        = '208F'            # �������ʱ��ʣ����

BLIND_LEVEL         = '3011'

MATCH_ID            = '3001' 
MATCH_NAME          = '3002'
MATCH_TYPE          = '3003'
USER_RANKING        = '300E'                    
PAY_TYPE            = '3026'
PAY_NUM             = '3027'
SERVICE_CHARGE      = '3028'             #integer  �����
INTHEMONEY_RATIO    = '303A'
REJOIN_CHIPS_TIME   = '3049'
LEFT_TIME           = '306B'
REBUY               = '306C'
REBUY_TIMES         = '306D'                #����rebuy��������
LEGAL_REBUY_LEVEL   = '306E'
REBUY_VALUE         = '306F'
REBUY_PAYMONEY      = '3071'
ADDON_WAIT_TIME     = '3072'
ADDON_VALUE         = '3073'
ADDON_PAYMONEY      = '3074'
REBUY_TYPE          = '3080'
ADDON_START_TIME    = '3081'
VALID_REBUY_TIME    = '3082'
IS_FAST_SIT         = '3098'                #�Ƿ��ǿ��ٿ�ʼ���� ��'YES', ����'NO'
WAIT_REASON         = '309D'


IS_ALLIN            = '3096'
PLAY_TYPE           = '30A5'                #��Ϸ����
SERVER_ADDR         = '30A7'
TABLE_OWNER         = '30A8'                #����

USER_CHIPS_INFO     = '3078'                #����������ϵĳ�����Ϣ
HUNTING_REWARD      = '30AF'                #����������
IS_DELAY_APPLY      = '30B1'                #�Ƿ����ӳٱ����������

# ���¼���key ����ͬ�������Ϣ
PT_ALL_INFO                 = '330B'            # һ�����еı�����Ϣ(����ͬ��matchserver)
PT_USER_UNIT                = '330C'            # ������Ϣ��ÿһ��ҵ���Ϣ ����: username, ���ƣ� ���ճ���, ϵͳ�⸶����
PT_TOTAL_POTS               = '330D'            # һ���еĵ׳ص�Ͷ����
PT_USER_MONEY               = '330E'            # һ������ҵ���Ͷ����
PT_USER_BACK_MONEY          = '330F'            # һ������ҵ�Ͷ�б���ϵͳ�⻹�Ķ��
PT_USER_ALL_UNIT            = '3310'            # ���������Ϣ��Ԫ
PT_USER_CHIPS               = '3311'            # ���һ�ֽ����󣬳������Ӯ���   ������ʾӮ�� ������ʾ��
PT_USER_HEAD_IMG            = '3312'            # ���ͷ��url
PT_SYS_PT_INFO              = '3313'            # ϵͳ�����п�ӯ����
PT_PAY_TYPE                 = '3319'            # ֧������  POINT:��    GOLD: ���
PT_TABLE_NAME               = '331A'            # ��������
USER_PT_OPER_WIN_OR_LOST    = '3333'            # ��ұ��ֱ���ӯ�����  ������ʾ���Ͷ��׬�ˣ�������ʾ���Ͷ������

PT_ADJUST_LIST              = '3340'            # ���ճط����б�
PT_POT_PERCENT              = '3341'            # ��ҷ��䱣�ճ���ռ����

REDUCE_CHIPS_INFOS          = '3997'            # ������ж����Ϣ
SAVE_SUCC_FLAG              = '3998'           # ��¼�ɹ�����������Ϣ��ʾ(������������)


PASSWORD            = '4001'

ORDER_ID            = '500B'

BUSISORT            = '5012'
BUSINO              = '5013'
TOTAL_GOLD_BALANCE  = '504C'                #�ܽ�����
TOTAL_SILVER_BALANCE= '504D'                #���������

WHITE_LIST          = '6007'                #������
USER_GROUP          = '600F'                #�û�������
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
