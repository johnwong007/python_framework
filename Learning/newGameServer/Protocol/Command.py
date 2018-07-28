#coding=gbk

''' �¼�����ʹ���ָ�� '''

# ָ��˵��
PING                     = 0x00000001         #��·���                             
PING_RESP                = 0x80000001         #��·����Ӧ                         
CONNECT                  = 0x00000002         #���������������session��Ϣ��������
CONNECT_RESP             = 0x80000002         #���ӻ�Ӧ�����أ��½��ģ�session��Ϣ  
QUIT                     = 0x00000003         #�˳�����                             
QUIT_RESP                = 0x80000003         #�˳���Ӧ                             

LOGIN                    = 0x00050001         #��¼����                                           
LOGIN_RESP               = 0x80050001         #��¼��Ӧ������ɹ��Ļ���Ҫ֪ͨuser��Ϣ�󶨵�session
LOGOUT                   = 0x00050002         #�ǳ�����                                           
LOGOUT_RESP              = 0x80050002         #�ǳ���Ӧ                                           
CREATE_ACCOUNT           = 0x00050003         #�����˺ţ�ע�ᣩ                                   
CREATE_ACCOUNT_RESP      = 0x80050003         #�����˺Ż�Ӧ                                       
USER_GET_INFO            = 0x00050004         #��ȡ�û���Ϣ    
USER_GET_INFO_RESP       = 0x80050004         #��ȡ�û���Ϣ��Ӧ


MATCH_REGISTER           = 0x00060001         #�Ǽǣ��μӣ����£���������
MATCH_REGISTER_RESP      = 0x80060001         #�Ǽǻ�Ӧ                  
MATCH_UNREGISTER         = 0x00060002         #�˳�����                  
MATCH_UNREGISTER_RESP    = 0x80060002         #�˳���Ӧ                  
MATCH_LIST               = 0x00060003         #�����б�                  
MATCH_LIST_RESP          = 0x80060003         #�б��Ӧ                  
MATCH_GET_TABLE          = 0x00060004         #��ȡ��������              
MATCH_GET_TABLE_RESP     = 0x80060004         #���Ż�Ӧ                  
MATCH_INFO               = 0x00060005         #��ȡ������Ϣ    
MATCH_INFO_RESP          = 0x80060005         #��ȡ������Ϣ��Ӧ

KICK_USER_CARD_REQ       = 0x00060010
TABLE_WAIT_MSG           = 0X00060013

TABLE_LIST               = 0x00010001         #��ȡ�����б�    
TABLE_LIST_RESP          = 0x80010001         #��ȡ�����б��Ӧ

TABLE_JOIN               = 0x00020001         #��������          131073
TABLE_JOIN_RESP          = 0x80020001         #����������Ӧ      2147614721
TABLE_LEAVE              = 0x00020002         #�뿪����          131074
TABLE_LEAVE_RESP         = 0x80020002         #�뿪������Ӧ      2147614722
TABLE_INFO               = 0x00020003         #��ȡ������Ϣ      131075
TABLE_INFO_RESP          = 0x80020003         #��ȡ������Ϣ��Ӧ  2147614723 2147614723
SIT                      = 0x00020004         #����            
SIT_MSG                  = 0x80020004         #������Ϣ        2147614724
SIT_OUT                  = 0x00020005         #�뿪��λ      131077    
SIT_OUT_MSG              = 0x80020005         #�뿪��λ��Ϣ  2147614725  
BUY_IN                   = 0x00020006         #����            
BUY_IN_RESP              = 0x80020006         #�����Ӧ        
TABLE_MJOIN              = 0x00020007         #���û������������ڲ��������ã�131079
TABLE_MJOIN_RESP         = 0x80020007         #���û�����������Ӧ              
TABLE_MLEAVE             = 0x00020008         #���û������������ڲ��������ã�
TABLE_MLEAVE_RESP        = 0x80020008         #���û�����������Ӧ              
BUY_CHIPS_PLAYER         = 0x00020009         #����֪ͨ��Ϸ�����û�������루���붩��ID������ID���û�ID��131081
BUY_CHIPS_PLAYER_RESP     = 0x80020009          #����֪ͨ��Ϸ�����û���������Ӧ 2147614729
CORRECT_PLAYER_CHIPS     = 0x0002000A         #����֪ͨ��Ϸ�����������£��û�����    
CORRECT_PLAYER_CHIPS_RESP= 0x8002000A         #����֪ͨ��Ϸ�����������£��û������Ӧ
JOIN_WAITING             = 0x0002000B          #�����Ŷӵȴ�      131083  
JOIN_WAITING_RESP        = 0x8002000B          #����ȴ���Ӧ  
UNJOIN_WAITING             = 0x0002000C          #ȡ���Ŷӵȴ�
UNJOIN_WAITING_RESP      = 0x8002000C          #ȡ���ȴ���Ӧ
END_WAITING              = 0x0002000D         #�����ȴ���֪ͨ����  131085
KEEP_TABLE             = 0x0002000E          #�������ӣ�����Χ�ۣ� 131086  
KEEP_TABLE_RESP             = 0x8002000E          #�������ӣ�����Χ�ۣ���Ӧ  

#���������ֽ�������Ȩ�޹���ʱ���ӵ�ָ��
SIT_PERMISSION_VERIFY           = 0x0002000F    #����match���ж�����Ȩ����֤   131087
SIT_PERMISSION_VERIFY_FINISH    = 0x8002000F    #����Ȩ����֤���ָ��
JOIN_WAITING_VERIFY             = 0x00020010    #�������ȴ��б�Ȩ����֤
JOIN_WAITING_VERIFY_FINISH      = 0x80020010    #����ȴ��б�Ȩ����֤���ָ��

FOLD_MATCH               = 0x00020012           #���������� 131090    
FOLD_MATCH_RESP          = 0x80020012           #������������Ӧ

FAST_SIT                        = 0x00020018    #���ٿ�ʼ����ָ��   131096
FAST_SIT_RESP                   = 0x80020018    #���ٿ�ʼ����ָ��ظ�   2147614744L
BUY_REQ                         = 0x00020019    #��������������
BUY_RESP                        = 0x80020019    #���������뷵��
SET_TRUSTEESHIP                 = 0x0002001B    #�ƾֿ�ʼ��ֻ��һ�������������ϣ����������������
SET_TRUSTEESHIP_RESP            = 0x8002001B    #�ظ�
FAST_SIT_ZHU_ZHAN               = 0x0002001C    #����Ϸ����Ŀ��ٿ�ʼ��ֻ�����վ���
FAST_SIT_ZHU_ZHAN_RESP          = 0x8002001C    #����Ϸ����Ŀ��ٿ�ʼ��ֻ�����վ��Ļظ�




TABLE_CREATE             = 0x00020301         #��������        
TABLE_CREATE_RESP        = 0x80020301         #����������Ӧ    
TABLE_START              = 0x00020302         #��������        
TABLE_START_RESP         = 0x80020302         #����������Ӧ    
TABLE_PAUSE              = 0x00020303         #������ͣ������֪ͨ�Թ����        
TABLE_PAUSE_RESP         = 0x80020303         #��ͣ������Ӧ        
TABLE_DESTROY            = 0x00020304         #��������             131844
TABLE_DESTROY_RESP       = 0x80020304         #����������Ӧ         2147615492
TABLE_SYNC_RULE          = 0x00020305         #ͬ�����¹���    
TABLE_SYNC_RULE_RESP     = 0x80020305         #ͬ�����¹����Ӧ
TABLE_GUIDE              = 0x00020306         #�����û���������    
TABLE_GUIDE_RESP         = 0x80020306         #�����û�����������Ӧ  

GET_PLAYERS              = 0x00020307         #ѯ��������� 131847
GET_PLAYERS_RESP         = 0x80020307         #������Ϣ 2147615495


TABLE_ADDON              = 0x00020308         #֪ͨGame������ʼaddon   131848    
TABLE_WAIT_ADDON         = 0x00020309         #֪ͨ�������ȴ��������ӽ���addon״̬ 

PRE_BUY_CHIPS_MSG        = 0x0002030A         #Ԥ��ɹ��ظ�����ʾ���ֽ������Ǯ���ϣ�131850


# **jason**
TABLE_TIME_DELAY		 = 0x0002030B		  #���Ѿַ�����ʱ (C->S)
TABLE_TIME_DELAY_RESP	 = 0x8002030B		  #���Ѿַ�����ʱ��Ӧ (S->C)
TABLE_PUSH_REMAIN_TIME	 = 0x0002030C		  #���ͣ��㲥��ֹ����µ�ʣ��ʱ��(��λ����)  (S->C)
TABLE_OWNER_DESTORY      = 0x0002030D		  #���Ѿַ�����������ǰ����������
TABLE_OWNER_DESTORY_RESP = 0x8002030D
TABLE_PROTCTED_REQU      = 0x0002030E         #�û����ղ���(���ջ�������)
TABLE_PROTCTED_RESP      = 0x8002030E
TABLE_PUSH_PROTCTED_INFO = 0x8002030F         #����:������Ϣ
TABLE_PUSH_PROTCTED_BACK = 0x80020310         #����ָ���û������ձ�����Ϣ
TABLE_REDUCE_CHIP		 = 0x00020311		  # �û�ж���������
TABLE_REDUCE_CHIP_RESP   = 0x80020311
TABLE_GET_OUTS_RATES	 = 0x00020312		  # ��ȡouts�������б�
TABLE_GET_OUTS_RATES_RESP = 0x80020312
TABLE_PUSH_PT_RESULT     = 0x80020313         # �㲥����ǰ�׶α��ս��
TABLE_PUSH_PT_OPERATE    = 0x80020314         # �㲥����ǰ�׶α��ղ���
TABLE_PUSH_PT_LAST_RESULT= 0x80020315		  # �㲥����ǰ��������һ�õ׳��뱣���⸶�Ľ��
TABLE_PT_OPER_DELAY      = 0x00020316		  # ���ղ�����ʱ
TABLE_PT_OPER_DELAY_RESP = 0x80020316
PUSH_PT_OPER_REMAIN_TIME = 0x80020317		  # �㲥�����ղ���ʣ��ʱ��(��)
TABLE_PT_ADJUST_REQU     = 0x00020318		  # ���ճط����б����
TABLE_PT_ADJUST_RESP     = 0x80020318
MATCH_PT_ADJUST_PUSH     = 0x00020319		  # ͨ��match���汣�ճط����б�
ONE_KEY_PASS_BUYIN_APPLY = 0x0002031A    	  # һ��ͨ��������������

CALL                     = 0x00020101         #��ע      131329
CALL_MSG                 = 0x80020101         #��ע��Ϣ   
RAISE                    = 0x00020102         #��ע      131330
RAISE_MSG                = 0x80020102         #��ע��Ϣ  
FOLD                     = 0x00020103         #����        131331
FOLD_MSG                 = 0x80020103         #������Ϣ     2147614979
CHECK                    = 0x00020104         #����        131332
CHECK_MSG                = 0x80020104         #������Ϣ  
ALL_IN                   = 0x00020105         #all in        131333
ALL_IN_MSG               = 0x80020105         #all in��Ϣ
CANCEL_TRUSTEESHIP       = 0x00020106         #ȡ���й�        131334
CANCEL_TRUSTEESHIP_MSG   = 0x80020106         #ȡ���й���Ϣ    2147614982
SHOWDOWN                 = 0x00020107         #��������        131335
SHOWDOWN_RESP            = 0x80020107         #����������Ϣ    2147614983 
SET_AUTO_BLIND           = 0x00020108         #�����Զ�����äע����    
SET_AUTO_BLIND_RESP      = 0x80020108         #�����Զ�����äע���ͻ�Ӧ

REBUY                    = 0x00020110         #����rebuy���� 131344
REBUY_RESP               = 0x80020110         #����rebuy�����Ӧ2147614992
PASSIVE_RE_BUY_REQ       = 0x00020111         #������Ա���rebuy����ң��Ƿ�rebuy   131345
ADDON_FINISH             = 0x00020112         #ת��addon������ 

LEAVE_CHIPS_STATE        = 0x00020116         #����뿪����ʱ������ڸ�������ӯ��״��131350
CARD_INFO                = 0x00020117         #ʥ�������ҵ��ѡ���˻��ƣ������̨��һ��131351

WAIT_FOR_MSG             = 0x00020201         #���ڵȴ�˭����λ���û�id�ȣ�����������ʲô�¼��� 131585
HAND_START_MSG           = 0x00020202         #�����ƾֿ�ʼ       131586                                  
POCKET_CARD              = 0x00020203         #����               131587                                             
FLOP_CARD_MSG            = 0x00020204         #����               131588                                         
TURN_CARD_MSG            = 0x00020205         #ת��               131589                                        
RIVER_CARD_MSG           = 0x00020206         #����               131590                                   
SHOWDOWN_MSG             = 0x00020207         #����               131591                                    
POT_MSG                  = 0x00020208         #���أ��䶯����Ϣ   131592                          
PRIZE_MSG                = 0x00020209         #�����أ��ɽ���Ϣ   131593
TABLE_SYNC_MSG           = 0x0002020A         #ͬ��������Ϣ��ÿ�ֽ����Ժ�ͬ����Ϣ�����£� 131594
SELECT_BUTTON_MSG        = 0x0002020B         #���ƾ���ׯ�ң������Ϣ    131595                 
TABLE_BLIND_MSG          = 0x0002020C         #äע������Ϣ��Сä�ʹ�ä��Ϣ��   131596          
TABLE_ANTE_MSG           = 0x0002020D         #��ע������Ϣ          131597                      
TABLE_BUTTON_MSG         = 0x0002020E         #ׯ��λ����Ϣ������Сä�ʹ�äλ�ã�  131598       
TRUSTEESHIP_MSG          = 0x0002020F         #�����й������Ϣ    131599                       
PLAYER_TIMEOUT_MSG       = 0x00020210         #������ҳ�ʱ��Ϣ    131600    
SHOWDOWN_REQ             = 0x00020211         #�ɹ���������        131601    
TABLE_RAKE_BF_FLOP_MSG   = 0x00020212          #����ǰ��ˮ��Ϣ      131602
BUY_CHIPS_MSG             = 0x00020213          #��ҳ��빺��ɹ�    131603
TABLE_DESTROY_MSG        = 0x00020214          #����������Ϣ        131604
PUNISH_BLIND_TO_BET     = 0x00020215          #äע�ͷ���������ע����Ϣ     Сäע 131605
PUNISH_BLIND_NO_BET     = 0x00020216          #äע�ͷ�����������ע����Ϣ   ��äע 131606
HAND_FINISH_MSG             = 0x00020217          #�����ƽ���  131607
BUYIN_APPLY_ANSWER      = 0x00020218            #131608
BUYIN_APPLY_ANSWER_RESP = 0x80020218            #�Է����Ļظ�Ӧ��  2147615256
REPORT_REDUCE_CHIPS_INFO = 0x00020400   # �ϱ�ж�������Ϣ


WATCHER_TIMEOUT_MSG      = 0x00020220          #�޳��������Ӧ��ʱ���Թ����
IS_SIT_OUT                = 0x00020221          #������ƾֹ�������;�뿪������

UPDATE_PLAYER_CHIPS       = 0x00020224         #����������131620
UPDATE_SIT_OUT_PLAYER_CHIPS = 0x00020225       #���ѿͻ��˸���������ҵ���� 131621


REMIND_USER_TABLE_WILL_DESTROY=0x00020228      #���ѿͻ��ˣ�5���Ӻ�������������    131624
REMIND_USER_TABLE_CARD_DESTROY=0x00020229      #���ѿͻ��ˣ��˾ֽ����������������� 131625

VOTE_KICK_USER_MSG        = 0x00020230         #131632      ����ͶƱ  ������->�ͻ���
VOTE_KICK_USER_MSG_RESP   = 0x80020230         #2147615280  ͶƱѡ��  �ͻ���->������
VOTE_KICK_RESULT          = 0x00020231         #131633      ͶƱ���  ������->�ͻ���
APPLY_OPERATION_DELAY     = 0x00020233         #���������ʱ
APPLY_OPERATION_DELAY_RESP= 0x80020233         #���������ʱ
USER_OPERATE_DELAY_MSG    = 0x00020234         #���������ʱ��֪ͨ���������
VALUE_ADDED_REPORT        = 0x00020235         #ʹ����ֵ�������ѱ���
APPLY_PUBLIC_CARD         = 0x00020236         #�ƾֽ���������鿴δ�����Ĺ�����
APPLY_PUBLIC_CARD_RESP    = 0x80020236
TRUSTEESHIP_PROTECT       = 0x00020237         #�����й���������
TRUSTEESHIP_PROTECT_RESP  = 0x80020237
DESTORY_TABLE_BACK_MONEY  = 0x00020238         #������ǰ��������ʱ������         
 

DESTROY_CASH_TABLE        = 0x0002030C         #֪ͨmatch��������Դ����ֽ���




TIMER_START               = 0x00040001         #����һ����ʱ������ 262145
TIMER_CANCEL              = 0x00040002         #ȡ��һ����ʱ������ 262146
TIMER_OUT                 = 0x00040003         #��ʱ������ʱ
TIMER_UPDATE              = 0x00040004         #���¶�ʱ��


TIMER_BUY_CHIPS           = 0x00050001         #ע���������ȴ�ʱ��327681
TIMER_SIT_OUT             = 0x00050002         #����뿪����ʱ�䣨ȥ��������书�ܣ�327682
TIMER_TRUSTEE_OUT         = 0x00050003         #����йܳ�ʱ 327683
TIMER_WATCHER_OUT         = 0x00050004         #�Թ���Ҷ�ʱ�����߳���ʱ��û����Ӧ���Թ���ң�327684
TIMER_OPERATION           = 0x00050005         #��Ҳ�����ʱ327685
TIMER_TRUSTEE_OPER_OUT    = 0x00050006         #����йܴ���ʱ327686
TIMER_NEW_ROUND           = 0x00050007         #��һ����ע��ʱ327687
TIMER_BF_START_TIMEOUT    = 0x00050008         #��ʼǰ�ȴ�ʱ��327688
TIMER_SHOW_DOWN_TIMEOUT   = 0x00050009         #�������Ƴ�ʱ֪ͨ327689
TIMER_PASSIVE_RE_BUY_PAUSE_TIME = 0x0005000A   #����rebuy��ʱ֪ͨ327690
TIMER_INTERVAL_HAND       = 0x0005000B         #��һ�ֵȴ�ʱ��327691
TIMER_STREE_FINISH        = 0x0005000C         #һ����ע���֪ͨ327692
TIMER_NEW_OPER_WAIT       = 0x0005000D         #������ע�ڼ�Ǯ�ȴ�327693
TIMER_STATE_FINISH        = 0x0005000E         #������һ״̬�ļ��ʱ��327694
TIMER_TRUSTEESHIP_FINISH  = 0x0005000F         #һ���й���Ҵ���֮�󣬼��0.5�봦����һ�����327695
TIMER_GO_SETBUTTON        = 0x00050010         #����setbutton״̬327696
TIMER_GO_WAITEBLIND       = 0x00050011         #����waiteblind״̬327697
TIMER_GO_HAND             = 0x00050012         #����hand״̬327698
TIMER_GO_SET_FIRST_BETER  = 0x00050013         #�������õ�λ��ע��״̬327699
TIMER_GO_FIRST_BET        = 0x00050014         #�����һ����ע327700
TIMER_UN_EXCEPT_LEAVE     = 0x00050015         #ȷ��äע�������뿪����      

TIMER_GO_PRIZE            = 0x00050017         #�����ɽ��׶�327703
TIMER_GO_FINISH           = 0x00050018         #�����ƾֽ���״̬327704

TIMER_TO_GAME             = 0x00050019         #֪ͨgame������һ״̬327705
TIMER_PAUSE_SERVER        = 0x0005001A         #����Ϸ������ͣ��һ������������ 327706   
TIMER_FORCE_SIT_OUT       = 0x0005001B         #αװվ����Ǯ  327707
TIMER_STOP_SERVER_SIGNAL  = 0x0005001C         #���߷��񣬼���ͣ�����ı�����һ�����

TIMER_DESTROY_USER_TABLE  = 0x0005001D         #������ң������ƽ���֮�󣬼�������
TIMER_PRE_REMIND_DESTROY  = 0x0005001E         #��ǰ5���ӣ�������ң���������5���Ӻ󼴽�����
TIMER_VOTE_KICK           = 0x0005001F         #ͶƱ����ʱ���ֹ 327711

TIMER_FAST_SIT_ZHU_ZHAN   = 0x00050020         #֪ͨ��һ����Ϸ����ȥ����λ��ֻ�����վ��

TIMER_KICK_CARD_OUTTIME   = 0x00050021         #���˿�����
TIMER_PROCTED_OUTTIME     = 0x00050023         #�����չ���
BUYIN_APPLY_RESP          = 0x80060014         #��������Ľ��
   
MONEY_IN_QUEUE_REQUEST    = 0x00090001          #��Ǯ  589825
MONEY_OUT_QUEUE_REQUEST   = 0x00090002          #ҪǮ   589826
MONEY_IN_QUEUE_RESP       = 0x80090001          #��Ǯ�ظ�0x80090001
MONEY_OUT_QUEUE_RESP      = 0x80090002          #ҪǮ�ظ�   2148073474


LOGSERVER                 = 0x000A0001          #��¼������־


