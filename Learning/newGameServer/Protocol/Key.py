#coding=gbk       
                            
''' ����key��Ӧ '''
                            
CODE                        = '0001'             #���������أ��룬���ձ����                                  
SESSION_ID                  = '0002'             #session id                                                        
HEADER                      = '0003'             #��Ϣͷ                                                            
BODY                        = '0004'             #��Ϣ��                                                            
COMMAND_ID                  = '0005'             #ָ��id                                                            
CONNECT_ID                  = '0006'             #����id                                                            
TIMESTAMP                   = '0007'             #unixʱ���                                                        
SEQUENCE_ID                 = '0008'             #��ָ������кţ�ÿ��RESP���ص����к���Ҫ��ָ��������������к�һ��
USER_AGENT                  = '0009'             #�ͻ��˰汾
MSG_SEQUENCE                = '000D'             #���ֽ��յ���ָ��ǵ�ʱ�Ǹ��׶�������ָ���ֹ�������ӳ٣��������Զ���������
                            
TABLE_LIST                  = '1001'             #�����嵥                          
TABLE_ID                    = '1002'             #����id                            
TABLE_TYPE                  = '1003'             #��������                          
GAME_SPEED                  = '1004'             #��Ϸ�ٶ�                          
BLIND_INFO                  = '1005'             #äע��Ϣ                          
ANTE                        = '1006'             #��ע   
TABLE_NAME                  = '1007'             #��������
TABLE_INFO                  = '1008'             #������Ϣ
INS_STATE                   = '110F'             # ���չ���״̬   '0':�ر�   '1':����
SUB_TABLE_TYPE				= '1110'			 # ��������
AUTO_BLIND 					= '1111'			 # ϵͳ�Ƿ��Զ��۳���Сä  1:�Զ��۳�  0�����۳�
BOTT_BBTIMES				= '1112'			 # ׯǰעBB����
PK_FIRST_BET			 = '1113'			 # PKʱ�޸�Ĭ�Ϲ���  0:Ĭ��   1:�޸�
COMSUMP_TYPE				= '1114'             # ��������ʱ��������   0:  Ĭ��ֵ   1: ����   2: ����
REDU_CHIP_FLAG              = '1116'			  # 6+ж�빦���Ƿ��� 
REDU_CHIP_LIMIT             = '1117'			  # 6+ж���Ƚ���
REDU_CHIP_SERVICE_RATE      = '1118'			  # 6+ж��������(�ٷֱ�)
TABLE_FINISH_UTC			= '1119'			 # ���ӽ���ʱ��(UTC)
CARD_COMPARE_TYPE			= '111E'			 # �����������ͣ�0:��ͨ������1:6+,22:6+��ʽ
APPLY_BUYIN_OPEN            = '12E0'             # �Ƿ�����׼���빦��
PT_POT_OPEN                 = '12E1'             # �Ƿ��б��ճط��书��

FAST_TABLE                  = '100E'             #������  

SERVER_GROUP                = '100F'             #��������
SERVER_NAME                 = '1010'             #������
BUYIN_TIMES					= '1011'			 #��Чbuyin����ͳ�ƣ�Ŀǰͳ�Ƶ����������
                      
LEFT_COMMUNITY_CARDS        = '2000' 			 #ʣ�๫����                    
PLAYER_LIST                 = '2001'             #����嵥                          
SEAT_NUM                    = '2002'             #��λ��                            
USER_ID                     = '2003'             #�û�id                            
USER_NAME                   = '2004'             #�û���                            
USER_CHIPS                  = '2005'             #�û�����                          
HAND_ID                     = '2006'             #��һ�ֵ�id��ÿһ�ֶ�����Ψһ��id��
DEALER_BUTTON               = '2007'             #ׯ��                              
SMALL_BLIND                 = '2008'             #Сä                              
BIG_BLIND                   = '2009'             #��ä                              
POT_INFO                    = '200A'             #������Ϣ                          
COMMUNITY_CARDS             = '200B'             #������                            
BET_CHIPS                   = '200C'             #��ע����ע��������                
ROUND_CHIPS                 = '200D'             #��һȦ���֣�������                
HAND_CHIPS                  = '200E'             #��һ�ֳ�����
SEAT_NO                     = '200F'             #��λ���                                                
GAME_STATUS                 = '2010'             #��Ϸ״̬              
PLAYER_STATUS               = '2011'             #���״̬              
REMAIN_TIME                 = '2012'             #���ʣ����עʱ��      
BUTTON_NO                   = '2013'             #ׯ��λ��              
SBLIND_NO                   = '2014'             #Сäλ��              
BBLIND_NO                   = '2015'             #��äλ��              
WAIT_FOR_NO                 = '2016'             #�ֵ���ע�ߵ���λ��    
LAST_POTS                   = '2017'             #��һ�ֵ׳�            
CARD_LIST                   = '2018'             #�Ƶ��б����Ƶ�ʱ����
PRIZE_LIST                  = '2019'             #�ɽ�list              
ABSENT_LIST                 = '201A'             #ȱϯ���ȴ���ң��б�  
WAITING_LIST                = '201B'             #�Ŷ�����б�  
POCKET_CARDS                = '201C'             #����        
REMOTE_NAME                 = '201D'             #Զ�̷����� ������Ŀǰ��remotename������group_name,server_name
HANDS_NUM                   = '201E'             #���˶�����
ANTE_INFO                   = '201F'             #����µĵ�ע��Ϣ
CARD_TYPE                   = '2020'             #����
MAX_CARD                    = '2021'             #�����
WIN_CHIPS                   = '2022'             #���Ӯ�õĳ�����
OPTIONAL_ACTIONS            = '2023'             #��ѡ�����
CALL                        = '2024'             #��ע����
RAISE                       = '2025'             #��ע(���޺�����)
IS_TRUSTEE                  = '2026'             #����Ƿ��й�
IS_AUTO_BLIND               = '2027'             #�Ƿ��Զ�����äע
IS_AUTO_ANTE                = '2028'             #�Ƿ��Զ����ɵ�ע
PLAYER_MYINFO               = '2029'             #����Լ���˽����Ϣ
TOTAL_POT                   = '202A'             #�����ϵ����г��루������������ϵ�)
SHOWDOWN_OPTIONAL           = '202B'             #�Ƿ��ѡ������
SHOWDOWN_TYPE               = '202C'             #ѡ���������ͣ�����ο�Config.py           
RAKE_CHIPS                  = '202D'             #��ˮ������
SITOUT_TIME                 = '202E'             #���վ���ʱ��
AUTO_BLIND_TYPE             = '202F'             #������ҽ���äע����
NEW_BLIND_CHIPS             = '2030'             #����äע            
NEW_BLIND_INFO              = '2031'             #����äע������Ϣ    
BUY_CHIPS_MIN               = '2032'             #������С������      
BUY_CHIPS_MAX               = '2033'             #������������      
RAKE_CHIPS_SUM_BF_FLOP      = '2034'             #����ǰ��ˮ������            
RAKE_CHIPS_PER_BF_FLOP      = '2035'             #����ǰ�ÿ����ҳ�ˮ������
RAKE_CHIPS_SUM_AF_FLOP      = '2036'             #���ƺ��ˮ������            
RAKE_CHIPS_MAX_AF_FLOP      = '2037'             #���ƺ��ˮ��������        
RAKE_CHIPS_RATIO_AF_FLOP    = '2038'             #���ƺ��ˮ����    
RAKE_INFO_BF_FLOP            = '2039'             #����ǰ��ˮ��Ϣ
BUY_CHIPS                   = '203A'             #�������
PLAYER_ID                    = '203B'               #��ң���ʱ��ID
PUNISH_BLIND_INFO            = '203C'             #�ͷ�äע��Ϣ
IS_PLAYING                    = '203D'             #�Ƿ�����û�
PUNISH_BLIND_CHIPS            = '203E'             #�ͷ�äע��С
BUY_TYPE                    = '203F'             #�������ͣ�BUY_IN����RE_BUY 
CASH_OUT                    = '2040'             #�û��ֽ����һ��ĳ�����    
GAIN_POINTS                 = '2041'             #�û��ֽ�����õĻ�����    
STAY_TIME                   = '2042'             #�û��������ϵĴ��ĳ���ʱ��
BLIND_NAME                  = '2043'             #äע����                  
RAKE_CHIPS_BF_FLOP          = '2044'             #����ǰ����ҳ�ˮ������    
RAKE_CHIPS_AF_FLOP          = '2045'             #���ƺ����ҳ�ˮ������    
HAND_START_REMAIN_TIME      = '2046'             #����һ�֣��ƾֿ�ʼ��ʣ��ʱ��
SBLIND_DODGE_NUM            = '2047'             #��Сä����
BBLIND_DODGE_NUM            = '2048'             #�Ӵ�ä����
IS_NEW_PLAYER               = '2049'             #�Ƿ�����ң������˵���û�����ƾֵģ�


USER_NICK_NAME              = '2050'             #��ұ�����QQ������ ������������������������ط���ԭ������ĵط��г�ͻ��
USER_SEX                    = '2051'             #����Ա�


CASH_TABLE_RULE_TYPE        = '2055'             #�ֽ�����Ϸ�������ͣ�רҵ���򣬿�����ס����

CURRENT_TIME                = '2057'             #��̨��ǰʱ��
IS_ADDON_STATE              = '2058'             #�Ƿ���addon�ȴ��ڼ�
REBUY_COUNT                 = '2059'             #��ҳɹ�rebuy����

CARD_PRIZE_LIST             = '2060'             #�鵽�����ƣ��б�[ '0_A', '1_3']���Ի�
PLAYER_ONLINE_IP            = '2061'             #�������ip
PRIZE_PUBLIC_CARD           = '2062'             #����ܹ��齱���ƣ������ƣ�
TOTAL_BUY_CHIPS             = '2063'             #������������
PRIZE_PRIVATE_CARD          = '2064'             #����ܹ��齱���ƣ����ƣ�
CARD                        = '2065'             #���ѡ�����
PROFIT_MONEY                = '2066'             #���ӯ����� ����ΪӮ������Ϊ��  

GAME_INFO                   = '2070'             #������һ����Ϸ������������Ϸ������Ϣ
FAST_PLAYER_INFO            = '2071'             #������һ����Ϸ���������������Ϣ
APPOINT_BBLIND              = '2072'             #YES/NO �Ƿ�ָ����äע�����ڿ�������
KICKED_INFO                 = '2073'             #��ұ�����Ϣ
REWARD_OUT_INFO				= '2074'			 #û��pot�л�ʤ�߼�allin���uid�б�
APPLY_UID                   = '2075'
APPLY_USERNAME              = '2076'
SERVICE_TYPE                = '2077'
SERVICE_ARGS                = '2078'
APPLY_DELAY_TIMES           = '2079'             #�ڵ�ǰ���Ѿ�������ʱ����
KEEP_SEAT_STIME             = '2080'

CHIPS_SITOUT        		= '208F'             # �������ʱ��ʣ����  

BOTTON_PRE_CHIPS			= '2090'			 # ׯǰע
BOTTON_PRE_INFO             = '2091'             #ׯǰע������Ϣ   

                          
MATCH_ID                    = '3001'             #����ID  
MATCH_NAME                  = '3002'             #��������
MATCH_TYPE                  = '3003'             #��������  
COMMON_RULE                 = '3004'             #��ͨ����  
SPECIFIC_RULE               = '3005'             #�������  
TOURNEY_TYPE                = '3006'             #����������
START_TIME                  = '3007'             #��ʼʱ��  
END_TIME                    = '3008'             #����ʱ��  
MATCH_STATUS                = '3009'             #����״̬  
MATCH_STATUS                = '3009'             #����״̬          
MIN_UNUM                    = '300A'             #��С��������      
MAX_UNUM                    = '300B'             #���������      
CUR_UNUM                    = '300C'             #��ǰ���ѱ���������
PAY_INFO                    = '300D'             #����֧����Ϣ  

BLIND_LEVEL                 = '3011'             #��ǰäע����  

  
PAY_TYPE                    = '3026'             #֧������ 
SERVICE_CHARGE              = '3028'


IS_REBUY                    = '306C'             #�Ƿ�rebuy��,��YES�� 'NO'
REBUY_LIMIT_COUNT           = '306D'             #�ɹ�rebuy���ƴ���
LEGAL_BLIND_LEVEL           = '306E'             #�Ϸ�rebuyäע����
REBUY_VALUE                 = '306F'             #rebuyһ�������ӵĳ�����Ŀ
REBUY_PAY_MONEY             = '3071'             #rebuyһ�λ��ѵ�Ǯ
PLAYER_INIT_CHIPS           = '3078'             #���µ�ǰ�ƾ֣���ҵĳ�ʼ����
REBUY_TYPE                  = '3079'             #rebuy����
TABLE_INIT_CHIPS            = '100C'             #���¿�ʼʱ��ÿ����ҵĳ�ʼ���� 
ADDON_WAIT_TIME             = '3072'             #addonһ�����ȴ���ʱ��
ADDON_VALUE                 = '3073'             #addonһ���������ӵĳ���
ADDON_PAYMONEY              = '3074'             #addonһ�������ѵ�Ǯ
PASSIVE_REBUY_USER          = '3075'             #���Ա���rebuy������б� [userid, ]
PLAYER_CHIPS_LIST           = '3076'             #�ڷ����ɽ���Ϣ��������������ʣ���� { userid:chips , } 
REBUY_MODE                  = '3080'             #rebuy���ͣ��Զ�=0�� �ֶ�=1
ADDON_ST_TIME               = '3081'             #addon�Ŀ�ʼʱ�� 
VALID_REBUY_TIME            = '3082'             #��ʼ����ʱ���ڿ���rebuy
PASSIVE_REBUY_WAIT_TIME     = '3085'             #����rebuy��һ����Եȴ���ʱ��
IS_SUC_ADDON                = '3086'             #����Ƿ�ɹ�addon  
IS_PASSIVE_REBUY            = '3087'             #�����Ƿ��ڱ���rebuy״̬
IS_SUC_REBUY                = '3089'             #��ҵ�ǰ�ƾ֣��Ƿ�ɹ�rebuy��һ��
IS_WATI_TO_ADDON            = '3090'             #�Ƿ�ȴ�����addon


IS_SIT_OUT                  = '3095'             #�����ƾֵ�����Ƿ���;�뿪����
IS_ALLIN                    = '3096'             #�Ƿ���allin�� ��YES'  'NO'
IS_FAST_SIT                 = '3098'             #�Ƿ��ǿ��ٿ�ʼ���� ��'YES', ����'NO'
PRE_BUY_CHIPS               = '309A'             #�ֽ�������ҳɹ���;�������ҳ�����
FINALLY_CHIPS               = '309B'             #��������ϵ����ճ���
PRE_BUY_CHIPS_A             = '309C'             #��ҵ�ǰһ��Ԥ��ɹ��ĳ���
WAIT_REASON                 = '309D'
IS_SYNC_RULE                = '309E'             #�Ƿ�ͬ������������

PLAY_TYPE                   = '30A5'             #��Ϸ����

TABLE_OWNER                 = '30A8'             #��������  'sys'ϵͳ�����ġ�  ��userid����Ҵ�����
PLAYER_PAYBACK_LIST         = '30B4'             #����ǰ��ˮ�����б�


REDU_CHIP_OPER			 = '30C1'			  # ����ö��   1�� һ��ж��  2: �ֶ�ж��   3:���� 
REDU_CHIP_CHIP			 = '30C2'			  # ����������
REDU_CHIP_SERVICE_FEE    = '30C3'			  # ж�������ѣ� �ٷֱ�  1% = 1
REDU_CHIP_OPER_TIME      = '30C4'			  # ж�����ʱ�� utc
REDU_CHIP_BOX_TOTAL      = '30C5'			  # ����ڱ������еĳ�������
REDUCE_CHIP_FLAG         = '30C6'			  # ж�빦���Ƿ���
REDUCE_CHIP_LIMIT        = '30C7'			  # ж�����

# 33**��ͷΪ�������  added by wj
PT_OUTS_TOTAL				= '3300'			# �����еĵ�Ԫ��Ϣ�б�
PT_OUTS						= '3301'			# ���յ�Ԫ��Ϣ�е�outs
PT_POTS						= '3302'			# �����еĵ׳���Ϣ�������߳أ�
PT_RATES					= '3303'			# �����е�����
PT_OPERATE					= '3304'            # ���ղ���ö��   -1: Ĭ��ֵ   0: �ܾ�����    1�� ��pot   2: ȫpot   3: ���ر���   4: ����
PT_POT_TYPE					= '3305'			# �׳�����       1: ����        2�� �߳�
PT_BACK_MONEY				= '3306'			# ���ر���������(����)
PT_STREET_FLAG				= '3307'			# ������Ϣ�����Ǹ��׶�  1: ת��ǰ    2: ����ǰ
PT_ACTIVE_MONEY				= '3308'			# ��Ҽ���ղ�������
PT_OPER_LIST				= '3309'			# ��ұ��ղ����б� 
PT_REAL_REDUCE				= '330A'			# �Ƿ���ʵ�ɹ��۳���������ĳ��� (����ʱ�õ�)
# ���¼���key ����ͬ�������Ϣ
PT_ALL_INFO					= '330B'			# һ�����еı�����Ϣ(����ͬ��matchserver)
PT_USER_UNIT				= '330C'			# ������Ϣ��ÿһ��ҵ���Ϣ ����: username, ���ƣ� ���ճ���, ϵͳ�⸶����
PT_TOTAL_POTS				= '330D'			# һ���еĵ׳ص��ܶ�
PT_USER_MONEY				= '330E'			# һ������ҵ���Ͷ����
PT_USER_BACK_MONEY			= '330F'			# һ������ҵ�Ͷ�б���ϵͳ�⻹�Ķ��
PT_USER_ALL_UNIT			= '3310'			# ���������Ϣ��Ԫ
PT_USER_CHIPS				= '3311'			# ���һ�ֽ����󣬳������Ӯ���   ������ʾӮ�� ������ʾ��
PT_USER_HEAD_IMG			= '3312'			# ���ͷ��url
PT_SYS_PT_INFO				= '3313'			# ϵͳ�����п�ӯ����
PT_USER_MAX_CARD			= '3314'			# ��������(5��)
PT_MAX_HALF_POT				= '3315'			# ��Ұ�pot���Ͷ����
PT_MAX_FULL_POT				= '3316'			# ���ȫpot���Ͷ����
PT_MAX_HALF_BACK			= '3317'			# ��pot����⸶��
PT_MAX_FULL_BACK			= '3318'			# ȫpot����⸶��
PT_PAY_TYPE					= '3319'			# ֧������  POINT:��    GOLD: ���
PT_TABLE_NAME				= '331A'			# ��������
PT_BACK_MONEY_OTHER			= '331C'			# ���ر���������(�߳�)
OUTS_RATE_LISTS  			= '331D'			# outs��rate�б�
OUTS_NUMB					= '331E'			# outs����
OUTS_RATE                   = '331F'			# outs����
IS_OPER_PT_2_STREET			= '3320'			# ת��ǰ�Ƿ��б��ղ���
IS_USER_PT_WIN				= '3322'			# ����Ƿ����б���
PT_WIN_WILL_BACK_CHIP       = '3323'            # ������б��ս���õ��⳥����������Ǹ��ͻ�����ʾ��
PT_MAX_BASE_BACK			= '3324'			# ��������⸶��
PT_SAME_OUTS				= '3325'			# ƽ�ֵ�outs�б�
PT_USER_SELECT_OUTS			= '3326'			# ���ѡ�����յ�outs�б�
PT_RESULT_LISTS				= '3327'			# �㲥��ұ��ս�����б�
PT_OPER_LISTS				= '3328'			# �㲥��ұ��ղ������б�
PT_USER_GET_POT				= '3330'			# �����һ�����л�õĵ׳�
PT_GET_POT_BACK_LISTS		= '3331'			# �㲥һ������һ�ȡ�׳��뱣���⸶���б�
PT_OPER_REMAIN_TIME			= '3332'			# ���ղ���ʣ���ʱ��(��)
USER_PT_OPER_WIN_OR_LOST	= '3333'			# ��ұ��ֱ���ӯ�����  ������ʾ���Ͷ��׬�ˣ�������ʾ���Ͷ������
USER_STREET_PT_RESULT		= '3334'			# ��ҵ�ǰ�׶�(��ǰֻ��ת��ǰ�����ǰ�����׶�)����ӯ�����  ������ʾ������˱��գ�������ʾ���û�б���
USER_PT_DETAIL_LIST			= '3335'			# �����һ�����б��յ���ϸ�����б�
UNSELECT_OUTS_NUMB			= '3336'			# û��ѡ���outs����
UNSELECT_ACTIVE_MONEY		= '3337'			# û��ѡ���outsϵͳ�Զ�Ͷ����
UNSELECT_PT_RESULT			= '3338'			# û��ѡ���outs�Ƿ��б�  0��û���б�   1:�б�
PT_MAIN_POT_BACK			= '3339'			# һ���ƴ������б����⸶��
PT_SUB_POT_BACK				= '333A'			# һ���ƴӱ߳��б����⸶��
WIN_MAIN_POT				= '333B'			# һ���ƻ�����س���
WIN_SUB_POT					= '333C'			# һ���ƻ�ñ߳س���
MAIN_POT_PUT_MONEY			= '333D'			# һ����������ʵ�ʿ۳��ı���
SUB_POT_PUT_MONEY			= '333E'			# һ���Ʊ߳���ʵ�ʿ۳��ı���
TABLE_REMAIN_TIME			= '333F'			# ���Ѿ�����ʣ��ʱ��(��)
PT_ADJUST_LIST				= '3340'			# ���ճط����б�
PT_POT_PERCENT				= '3341'			# ��ҷ��䱣�ճ���ռ����
ONE_KEY_PASS_BUYIN_LIST		= '3342'			# һ��ͨ������������û��б�

REDUCE_CHIPS_INFOS		    = '3997'			# ������ж����Ϣ
SAVE_SUCC_FLAG				= '3998'			# ��¼�ɹ�����������Ϣ��ʾ(������������)

PASSWORD                    = '4001'             #����    
USER_TYPE                   = '4002'             #�û�����
USER_STATUS                 = '4003'             #�û�״̬            
MOD_TIME                    = '4004'             #������޸�ʱ��    
CRT_TIME                    = '4005'             #��������ӣ�ʱ��    
MONEY_BALANCE               = '4006'             #���                
ADMIN_NAME                  = '4007'             #����Ա������Ա������
ADMIN_NOTE                  = '4008'             #����������˵��   

IS_IMAGE_CHARG              = '4051'             #������ϢΪͼ�����,�Ƿ��Ǯ
IMAGE_CHARG                 = '4052'             #������ϢΪ���飬�۵�Ǯ��Ŀ


CHAT_MSG_TYPE               = '4070'             #������Ϣ���� ��ͨ����'COMMON'  ֻ����flash: 'ONLY_FALSH'


USER_IDENTITY               = '600F'             # ������,�ڲܱ��Ǳ���USER_GROUP '1,2,3'

ORDER_ID                    = '500B'             #����id 
 

DEBAO_BALANCE               = '5028'             #�±������
GOLD_BALANCE                = '5029'             #������
SILVER_BALANCE              = '502A'             #�������

TOTAL_GOLD_BALANCE          = '504C'             #����ܽ�����
TOTAL_SILVER_BALANCE        = '504D'             #������������ 


CONTENT                     = '6004'             #(��Ϣ)����
WHITE_LIST                  = '6007'             #������

TABLE_CREATE_TIME			= '8900'			 # ���Ӵ���ʱ���

DEADLINE                    = 'A009'            #��ֹʱ��  ����Դ���������ֹ����

TIMER_INTERVAL              = 'B001'             #integer   ��ʱ������ʱ��(ms)
TIMER_USAGE                 = 'B002'             #string    ��ʱ����;�����������ҵ����)


MONEY_AMOUNT                = 'E001'              #float   ������Ǯ����
NEED_RESP                   = 'E002'              #bool    �Ƿ���Ҫ����
MONEY_TYPE                  = 'E003'              #string  Ǯ����
MONEY_RESULT                = 'E004'              #integer ���ؽ��
MONEY_CURRENT_AMOUNT        = 'E005'              #float    ��������ҵ�ǰ�ڶ�
MONEY_BUSINESS_UNIQUE_NUM   = 'E006'              #string  ҵ��Ψһ��ʾ��


LOG_TYPE                    = 'F001'              #string ҵ��
LOG_COST                    = 'F002'              #float ��ʱ
