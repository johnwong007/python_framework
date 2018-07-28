#coding=gbk
''' ������ģ�� '''
# ��Ϣ��ʱʱ��
MESSAGE_TIME_OUT         = 1000                         # ��λ����

# Χ����ң�����Ӧ��ʱʱ��
WATCHER_TIME_OUT         = 900                          # 15���ӡ���λ������6���Ӹ�Ϊ15���� 

# �����йܳ�ʱʱ��

TRUSTEE_TIME_OUT         = 600                          # ��λ���� 
# �����������
FLOAT_PRECISION          = 2                            # ���㾫����
MISS_BBLIND_OUT          = 3                            # ����N��äע�޳�
MIN_START_PEOPLE         = 2                            # ��С�������� 

INTERVAL_HAND            = 5                           # ÿ�ּ��ʱ�� 

INTERVAL_ROUND           = 2                            # ÿ�ּ��ʱ�� 

SHOW_DOWN_TIMEOUT        = 3                            # ���Ƴ�ʱʱ�� 

TRUSTEE_TIME             = 0.5                          # �ȴ��й���Ҵ���ʱ��

BF_START_TIMEOUT         = 6                            # ��ʼǰ�ȴ�ʱ�� 

REMAIN_LEAVE_TIME        = 1800                         # �����뿪��ҵ�ʱ��

REMAIN_TIMEOUT_TIME      = 30                           # ������ҵȴ���ʱʱ��

REMAIN_TIMEOUT_TIME_VGOLD= 300                           # ������ҵȴ���ʱʱ��

THOUSAND                 = 1000                         # 1��=1000����

STREE_FINISH             = 0.1                          #һ����ע���֪ͨ

NEW_OPER_WAIT            = 0.5                          #������ע����ȴ�

STATE_FINISH             = 1                            #������һ״̬�ļ��ʱ��

TRUSTEESHIP_FINISH       = 1.5                          #һ���й���Ҵ���֮�󣬼��0.5�봦����һ�����

SAME_IP_NUM              = 2                            #ͬ��ͬip��Ŀ����

VOTE_TIMEOUT_TIME        = 10                           #ͶƱʱ��

KICKED_CARD_OUTTIME      = 3600                         #���˿���Чʱ�� 1Сʱ

RAKE_BF_LIMIT_BB         = 10                           #����ǰ��ˮ���ƣ����������10BB���
RAKE_BF_BB_NUM           = 3                            #����ǰ�̶���ˮ��3��BB

PROTECTED_MAX_TIME       = 30							# �������ʱ�� (��)



# ������
_OK_ERROR_                  = 10000       # ����
_OPERATION_ERROR_           = -10001      # ͨ�ô���
_SYSTEM_ERROR_              = -10000      # ϵͳ����
                            
_PARAM_ERROR_               = -11000      # ��δ���
_HAS_TABLE_ERROR_           = -11001      # �Ѿ����ڵ�����
_TABLE_NOTFOUND_ERROR_      = -11002      # �����ڵ�����
_NOT_ENOUGH_SEATS_ERROR_    = -11003      # ��������λ������
_NOT_SYNC_STATE_ERROR_      = -11004      # ����ͬ�����¹����״̬
_NOT_SIT_TABLE_ERROR_       = -11005      # ������������������ӣ�����������ֻ������������������
_NOTEXSIT_TABLE_TYPE_ERROR_ = -11006      # �����ڵ��������� 
                             
_QUEUE_NOHAS_ERROR_         = -11007      # ������û�и����
_HAS_SEAT_ERROR_            = -11008      # ���п���������Ҫ����ȴ�
_JOINED_PLAYER_ERROR_       = -11009      # �Ѿ�����ȴ������
_HAS_JOINED_ERROR_          = -11010      # �Ѿ���������                           
_NOTEXSIT_SEAT_ERROR_       = -11011      # �����ڵ���λ��
_USER_NOCHIPS_ERROR_        = -11012      # ���ʣ����벻��
_SEAT_NO_PLAYER_ERROR_      = -11013      # ����λ���������
_HAS_SEATED_POS_ERROR_      = -11014      # ����λ���Ѿ������
_PLAYER_NOHAS_SEAT_ERROR_   = -11015      # ���û�û����λ
_CAN_NOT_SHOW_DOWN_ERROR_   = -11016      # �����û�����Ƶ�Ȩ��                           
_NOT_ACT_TABLE_TYPE_ERROR_  = -11017      # ��������Ҳ������������� 
_SITED_PLAYER_ERROR_        = -11018      # �Ѿ��ڸ������������
_PLAYING_SIT_ERROR_         = -11019      # ��������뿪���������ٴ�����                           
                            
_NOT_TURN_YOU_ERROR_        = -11020      # û���ֵ�����ע
_CAN_NOT_CHECK_ERROR_       = -11021      # û�п���Ȩ��
_FEW_CHIPS_RAISE_ERROR_     = -11022      # ��ע�������
_NOT_BET_STATE_ERROR_       = -11023      # ������ע��״̬ 
_HAS_BET_ERROR_             = -11024      # �Ѿ���ע���ظ���ע
                            
_WRONG_AUTO_TYPE_ERROR_     = -11029      # �������������
_NOT_ALLOW_BUY_ERROR_       = -11030      # ���ڲ�����һ����� 
_WRONG_CHIPS_BUY_ERROR_     = -11031      # ����Ĺ��������
_TRUSTEE_BET_ERROR_         = -11032      # �й�����Ҳ�������


# ʵ���ֽ�׿����Ȩ�޹���ʱ���ӵ�
REGISTER_CHANNEL_ERROR      = -11033      # ����ע��������֤ʧ�ܴ���
REGISTER_TIME_ERROR         = -11034      # ����ע��ʱ����֤ʧ�ܴ���

MSG_SEQUENCE_ERROR          = -11041      # ���յ���sequence��������ʱ��sequence��һ�£�Ŀǰ��û�õ���
_IS_SIT_OUT_ERROR_          = -11042      # ��;�����������ң�������ͨ��Ԥѡ��ť��ִ����ע��Ϊ

_NOTEXSIT_CASH_TABLE_RULE_TYPE_ERROR_  = -11045   # �����ڵ��ֽ�����Ϸ������������
_NOTEXSIT_PAY_TYPE_ERROR_              = -11046   # �����ڵ�֧�����ͣ�silver, gold)

_IS_NOT_REBUY_ERROR_        = -11047      # ����rebuy��
_INIT_CHIPS_TOO_MANY_       = -11048      # rebuyʱ����ǰ�ƾֳ�ʼ��������趨ֵ�����¿�ʼ��ҳ�ʼ���룩
_BLIND_LEVEL_TOO_HIGH_      = -11049      # rebuyʱ����ǰ�ƾֵ�äע��������趨ֵ�������趨��äע����
_is_ADDON_STATE_            = -11055      # addon�ڼ䲻��rebuy

_ONLINE_IP_TOO_MANY_        = -11060      #ͬ������ip��������

_PRE_BUY_FAIL_            = -11065      #�Ѿ������һ�γ��룬���ֽ���������
_PRE_BUY_SUC_            = -11066      #Ԥ��ɹ�

_PASSWORD_ERROR_        =   -11070          #�����������  

_TABLE_STATE_ERROR_            =    -12000        #    ����״̬����
_FAST_SIT_ERROR_            =    -12001        #�¿�����������

_BALANCE_TOO_MANY_          = -12003       #�����̫�࣬���ʺ�����ǰäע���������

TIMES_LIMIT_ERROR           = -15020      #��������

VOTE_KICK_FAIL              = -17002      #ͶƱ����ʧ��
VOTE_KICK_SUCCESS           = -17003
BEING_KICKED_OUT_RECORD     = -17004      #�б��߼�¼ 
KICK_USER_NUM_ERR           = -17005      #ֻ��1���˵�ʱ����ô�ߣ�
VOTING_NOT_END_ERR          = -17006      #��һ��ͶƱδ����
_NOT_THE_TABLE_OWNER_       = -18001	  #

OUTS_LARGE_LIMIT_HALF_POT	= -19000	  # outs>=12ʱ���ް�pot

NOT_ENOUGH_CHIP_FOR_REDUCE  = -19100	  # ��ǰ���㹻����ɹ�ж��
                    
                           
# ����״̬                 
TABLE_STATE_WAIT_SYNC      = 20000        # �ȴ�����ͬ������
TABLE_STATE_INIT           = 20001        # ��ʼ
TABLE_STATE_SETBUTTON      = 20002        # ����ׯ��
TABLE_STATE_WAIT_BLIND     = 20003        # �ȴ������äע�͵�ע
TABLE_STATE_SET_FBETER     = 20004        # ���õ�һλ��ע��
TABLE_STATE_HAND           = 20005        # ������
TABLE_STATE_FIRST_BET      = 20006        # �ɹ�ѭ���ȴ������ע
TABLE_STATE_FLOP           = 20007        # ������
TABLE_STATE_SECOND_BET     = 20008        # �ɹ�ѭ���ٴεȴ������ע
TABLE_STATE_TURN           = 20009        # ��ת��
TABLE_STATE_THIRD_BET      = 20010        # �ɹ�ѭ�����εȴ������ע
TABLE_STATE_RIVER          = 20011        # ������
TABLE_STATE_FOURTH_BET     = 20012        # �ɹ�ѭ���Ĵεȴ������ע 
TABLE_STATE_PRIZE          = 20013        # �ɹٷ��佱��
TABLE_STATE_SHOWDOWN       = 20014        # �ɹٵȴ������������
TABLE_STATE_END            = 20015        # �ɹ���������,�ϴ�һ���ƾ���Ϣ
# added by jason
TABLE_STATE_PROTECTED      = 20016		  # ת��ǰ �����̬ 
TABLE_STATE_PROTECTED_2    = 20017		  # ����ǰ �����̬
                           
                           
# ���״̬                 
PLAYER_STATE_INIT          = 30000        # ��ʼ
PLAYER_STATE_REMAIN        = 30003        # ����
PLAYER_STATE_CAN_PLAY      = 30005        # ���Ա���
PLAYER_STATE_PLAY          = 30006        # ����
PLAYER_STATE_ALLIN         = 30007        # allin
PLAYER_STATE_FOLD          = 30008        # ����


# �����������
SHOW_DOWN_NOT              = 0            # ������
SHOW_DOWN_FIRST            = 1            # ����һ��
SHOW_DOWN_SECOND           = 2            # ���ڶ���
SHOW_DOWN_ALL              = 3            # �����е�
                           
                           
# �����˿˵�����           
                           
ROYAL_FLUSH                = 9            # �ʼ�ͬ��˳   
                           
STRAIGHT_FLUSH             = 8            # ͬ��˳
                           
FOUR_OF_A_KIND             = 7            # ����
                           
BOAT_OR_FULL_HOUSE         = 6            # ��«
                           
FLUSH                      = 5            # ͬ��
                           
STAIGHT                    = 4            # ˳��
                           
THREE_OF_A_KIND            = 3            # ����
                           
TWO_PAIRS                  = 2            # ����
                           
PAIR                       = 1            # һ��
                           
HIGH_HAND                  = 0            # ����

FOLD_WIN                   = -1           # �����������Ӯ��

INVALID_CHIPS_WIN          = -2           # ��Ч����Ӯ��

# ����Զ�����äע����
AUTO_BLIND_ACCEPT_ALL             = 0            #�Զ�֧������ä������������ǰע����äע

AUTO_BLIND_REFUSE_NEWBLIND        = 1            #�ܾ�����ä�����Զ�֧��������ǰע����äע

AUTO_BLIND_REFUSE_ALL             = 2            #ȫ���ܾ� �C �ܾ�����ä��Ҳ�ܾ�������ǰע��Сäע����äע

AUTO_BLIND_REFUSE_BBLIND          = 3            # ֻ�ܾ����ɴ�äע, ֧��������ǰע��Сäע ( ��һ�ִ�äע���� )

# ��������
TABLE_TYPE_TMT_SIT      =   'SITANDGO'     # �������ͣ���������
TABLE_TYPE_TMT_TIME     =   'TOURNEY'      # �������ͣ���ʱ���򾺱���
TABLE_TYPE_CASH         =   'CASH'         # �������ͣ��ֽ���

PASSIVE_RE_BUY_INIT     =   0              # ��ұ���rebuy����ʼ״̬
PASSIVE_RE_BUY_YES      =   1              # ��ұ���rebuy: �ɹ�����rebuy
PASSIVE_RE_BUY_NO       =   2              # ��ұ���rebuy: �ܾ�����rebuy

REBUY_MODE_AUTO         =   0              # rebuy��ʽ:�Զ�rebuy
REBUY_MODE_NOT_AUTO     =   1              # rebuy��ʽ:�ֶ�rebuy

PASSIVE_RE_BUY_PAUSE_TIME = 20             # ����rebuy������ͣ�ȴ�ʱ��

#�汾����
FLASH                   = 'FLASH'          #flash��
PC                      = 'PC'             #
ANDROID                 = 'ANDROID'        #
IOS                     = 'IOS'            #

TABLE_OWNER_SYS            =    'sys'                #ϵͳ����������
PRE_REMIND_END_TIME     =   300             #��ǰ5���ӣ���������Դ������������������������

FAST_ZHU_ZHAN       = 'COMMON'             #��վ
FAST_ANDROID        = 'FAST'             #��׿

CHAT_COMMON              = 'COMMON'        #��ͨ����
CHAT_ONLY_FALSH          = 'ONLY_FLASH'    #ֻflash�ͻ��˿��Կ���
CHAT_ALL                 = 'ALL'           #�������ߣ�FLASH,MOBILE�ͻ��˼���


#֧�ֵ������������
VALID_PAY_TYPE = (
    'GOLD',         #��� 
    'RAKEPOINT',    #����
    'VGOLD',        #����ң��ڵ±�����ʹ��
    'POINT'         #POINT �±���
)


# ��ֵ��������
VALUE_ADDED_OPERA_DELAY     = 'OPERATION_DELAY'     #������ʱ
VALUE_ADDED_VIEW_COMMON_CARD= 'VIEW_COMMON_CARD'    #��������
VALUE_ADDED_KEEP_SEAT       = 'KEEP_SEAT'           #��������
VALUE_ADDED_DELAY_TABLE_TIME= 'DELAY_TABLE'			#��������ʱ����  **jason**

