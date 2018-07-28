#coding=utf-8
'''
���¹��� 

���� ���� �ȵ� 
'''
import zlog as logging

import Object.Match as MatchData
import Match as MatchDB
import Player
import Message
import Protocol as P

from Config import *

class Manager:

    def __init__(self):
        ''' '''
        pass

    def apply_match(self, matchid, userid, username=''):
        ''' ���±��� 
            params int id ����id
        '''
        #�������µ��û��б�
        #logging.info('**** MatcherServer bg, mathid:%s, uid:%s', str(matchid), str(userid))
        match = MatchData.get(matchid)
        if not match:
            #logging.info('**** MatcherServer, apply_match, unknow match, id:%s', str(matchid))
            return False
            
        #�ظ�������Ҫ�˿�
        if match.user_list.count( str(userid) ) > 0:
            msg = {
            P.MATCH_ID  : matchid,
            P.USER_ID   : userid,
            P.USER_NAME : username,
            P.BUSISORT  : 'MATCH_GAME',
            P.BUSINO    : 'APPLY',
            }
            remotename = AGENT_ADDRESS
            c_sequence_id = ''   
            data = P.pack().event( P.REPEAT_APPLY_BACKMONEY ).mid( c_sequence_id ).body( msg ).get()
            Message.send( remotename, data )
            logging.info('REPEAT_APPLY_BACKMONEY---->%s'%msg)
            return False
            
        match.user_list.append( str(userid) )
        match.user_conf[ str(userid) ]                      = {}
        match.user_conf[ str(userid) ][ 'username' ]        = username
        match.user_conf[ str(userid) ][ 'user_agent' ]      = ''
        match.user_conf[ str(userid) ][ 'is_trustee' ]      = False #�Ƿ����й�״̬
        
        match.user_conf[ str(userid) ][ 'rebuy_times' ]     = 0     #����Ѿ�rebuy�Ĵ���
        match.user_conf[ str(userid) ][ 'rebuy_money' ]     = 0     #����Ѿ�rebuy���ĳ���
        match.user_conf[ str(userid) ][ 'pro_rebuy_money' ] = 0     #Ԥ����룬��û���ʵĳ��� 
        match.user_conf[ str(userid) ][ 'rebuy_orderid' ]   = []    #����id��(lobby_orderid, acct_orderid)

        # �羺�����⴦��  added by WangJian
        if (match.level == 'E_SPORTS'):
            lists = MatchDB.get_e_sport_extral_matchs(matchid)
            for i in lists:
                sub_match = MatchData.get( i['sub_id'] )
                if not sub_match:
                    continue
                sub_match.user_list.append( str(userid) )
                sub_match.user_conf[ str(userid) ]                      = {}
                sub_match.user_conf[ str(userid) ][ 'username' ]        = username
                sub_match.user_conf[ str(userid) ][ 'user_agent' ]      = ''
                sub_match.user_conf[ str(userid) ][ 'is_trustee' ]      = False #�Ƿ����й�״̬
                sub_match.user_conf[ str(userid) ][ 'rebuy_times' ]     = 0     #����Ѿ�rebuy�Ĵ���
                sub_match.user_conf[ str(userid) ][ 'rebuy_money' ]     = 0     #����Ѿ�rebuy���ĳ���
                sub_match.user_conf[ str(userid) ][ 'pro_rebuy_money' ] = 0     #Ԥ����룬��û���ʵĳ��� 
                sub_match.user_conf[ str(userid) ][ 'rebuy_orderid' ]   = []    #����id��(lobby_orderid, acct_orderid)                
        
    def delay_apply_match(self, match_obj, userid, username):
        '''�ӳٱ��������������Ϣ���ɹ�¼�뵽�ڴ���'''
        #�������µ��û��б�
            
        if not str(userid) in match_obj.user_list:
            match_obj.user_list.append( str(userid) )
        if not match_obj.user_conf.has_key(str(userid)):
            match_obj.user_conf[ str(userid) ]                      = {}
            match_obj.user_conf[ str(userid) ][ 'username' ]        = username
            match_obj.user_conf[ str(userid) ][ 'user_agent' ]      = ''
            match_obj.user_conf[ str(userid) ][ 'is_trustee' ]      = False #�Ƿ����й�״̬
            
            match_obj.user_conf[ str(userid) ][ 'rebuy_times' ]     = 0     #����Ѿ�rebuy�Ĵ���
            match_obj.user_conf[ str(userid) ][ 'rebuy_money' ]     = 0     #����Ѿ�rebuy���ĳ���
            match_obj.user_conf[ str(userid) ][ 'pro_rebuy_money' ] = 0     #Ԥ����룬��û���ʵĳ��� 
            match_obj.user_conf[ str(userid) ][ 'rebuy_orderid' ]   = []    #����id��(lobby_orderid, acct_orderid)

        #reEnter
        if match_obj.player_lose_list.has_key(str(userid)):
            match_obj.player_lose_list.pop(str(userid))


        # �羺�����⴦��  added by WangJian
        if (match_obj.level == 'E_SPORTS'):
            lists = MatchDB.get_e_sport_extral_matchs(matchid)
            for i in lists:
                sub_match = MatchData.get( i['sub_id'] )
                if not sub_match:
                    continue
                if not str(userid) in sub_match.user_list:
                    sub_match.user_list.append( str(userid) )
                if not sub_match.user_conf.has_key(str(userid)):
                    sub_match.user_conf[ str(userid) ]                      = {}
                    sub_match.user_conf[ str(userid) ][ 'username' ]        = username
                    sub_match.user_conf[ str(userid) ][ 'user_agent' ]      = ''
                    sub_match.user_conf[ str(userid) ][ 'is_trustee' ]      = False #�Ƿ����й�״̬
                    sub_match.user_conf[ str(userid) ][ 'rebuy_times' ]     = 0     #����Ѿ�rebuy�Ĵ���
                    sub_match.user_conf[ str(userid) ][ 'rebuy_money' ]     = 0     #����Ѿ�rebuy���ĳ���
                    sub_match.user_conf[ str(userid) ][ 'pro_rebuy_money' ] = 0     #Ԥ����룬��û���ʵĳ��� 
                    sub_match.user_conf[ str(userid) ][ 'rebuy_orderid' ]   = []    #����id��(lobby_orderid, acct_orderid) 
                #reEnter
                if sub_match.player_lose_list.has_key(str(userid)):
                    sub_match.player_lose_list.pop(str(userid))                    


    def clear_apply(self, matchid):
        '''
            ��ձ���
        '''
        match = MatchData.get(matchid)
        if not match:
            return False
        match.user_list = []
        match.user_conf = {}

        # �羺�����⴦��  added by WangJian
        if (match.level == 'E_SPORTS'):
            lists = MatchDB.get_e_sport_extral_matchs(matchid)
            for i in lists:
                sub_match = MatchData.get( i['sub_id'] )
                if not sub_match:
                    continue
                sub_match.user_list = []
                sub_match.user_conf = {}                                    
        

    def quit_match(self, matchid, userid):
        ''' ����
            params int matchid ����id
                   int userid  �û�id
        '''
        #logging.jsinfo('****** quit_match bg....')
        #������µĲ����û��б�
        MatchData.get(matchid).user_list.remove(userid)
        #����Ҳ�õ���pop����Ŷ��
        MatchData.get(matchid).user_conf.pop(userid, None)

        match = MatchData.get(matchid)
        if not match:
            logging.jsinfo('****** quit_match 1111')
            return 1

        # �羺�����⴦��  added by WangJian
        if (match.level == 'E_SPORTS'):
            #logging.jsinfo('****** quit_match 2222')
            lists = MatchDB.get_e_sport_extral_matchs(matchid)
            for i in lists:
                sub_match = MatchData.get( i['sub_id'] )
                #logging.jsinfo('****** quit_match 3333, subid:%s', str(i['sub_id']))
                if not sub_match:
                    #logging.jsinfo('****** quit_match 4444')
                    continue
                #logging.jsinfo('****** quit_match 5555')
                sub_match.user_list.remove(userid)
                sub_match.user_conf.pop(userid, None)

        #logging.jsinfo('****** quit_match 6666')
        return 1
        
        
    def kickout_offline_user(self, match_id):
        '''
            ǿ�Ʋ������������
            ��Σ�match_id
            ���Σ�offline_user_list    ��������б�
            ��д��liulk
            ���ڣ�2012.08.08 11:56
        '''        
        #����������ã��Ƿ���Ҫ�߳����������
        ret = MatchDB.kickout_or_not(match_id)
        
        if not ret:
            #��������
            return None
        else:
            #Ҫ����
            #��ʼ�������б�
            offline_user_list = []
            
            #ȡ�����²�����Ա�б�
            userlist = []
            for item in MatchData.get(match_id).user_list:
                userlist.append(item)
            logging.info('apply userlist is----------> : %s'%userlist)
            userlist_len = len(userlist)
            
            for val in range(userlist_len):
                #�����û��Ƿ�����True or False
                online = Player.check_user_online_status( userlist[val] )
                if online:
                    continue
                else:
                    #�����ߣ�Ҫ�ߵ����ˣ���userid���������б�
                    offline_user_list.append(userlist[val])
                    #ͬʱ�����ڴ��е�user_list,  user_conf
                    self.quit_match(match_id, userlist[val])
                    
            #�������б���������񣬽���ǿ������
            msg = {
            P.MATCH_ID : match_id,
            P.PLAYER_LIST : offline_user_list,
            }        
            remotename = AGENT_ADDRESS
            logging.info('remotename is : %s'%str(remotename))

            c_sequence_id = ''    # ȡ�����к�
            data = P.pack().event( P.KICKOUT_OFFLINE_USER ).mid( c_sequence_id ).body( msg ).get()
            Message.send( remotename, data )
            
            logging.info('Inform lobby_misc to kick out the offline users!')
            logging.info('OFFLINE USER_LIST: %s'%offline_user_list)
            
            return offline_user_list
    
    
    
    
    
    
    
    
    
    
    
    
    
