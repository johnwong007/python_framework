#coding=utf-8
'''
赛事管理 

报名 退赛 等等 
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
        ''' 赛事报名 
            params int id 赛事id
        '''
        #加入赛事的用户列表
        #logging.info('**** MatcherServer bg, mathid:%s, uid:%s', str(matchid), str(userid))
        match = MatchData.get(matchid)
        if not match:
            #logging.info('**** MatcherServer, apply_match, unknow match, id:%s', str(matchid))
            return False
            
        #重复报名的要退款
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
        match.user_conf[ str(userid) ][ 'is_trustee' ]      = False #是否是托管状态
        
        match.user_conf[ str(userid) ][ 'rebuy_times' ]     = 0     #玩家已经rebuy的次数
        match.user_conf[ str(userid) ][ 'rebuy_money' ]     = 0     #玩家已经rebuy到的筹码
        match.user_conf[ str(userid) ][ 'pro_rebuy_money' ] = 0     #预买筹码，还没到帐的筹码 
        match.user_conf[ str(userid) ][ 'rebuy_orderid' ]   = []    #订单id：(lobby_orderid, acct_orderid)

        # 电竞赛额外处理  added by WangJian
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
                sub_match.user_conf[ str(userid) ][ 'is_trustee' ]      = False #是否是托管状态
                sub_match.user_conf[ str(userid) ][ 'rebuy_times' ]     = 0     #玩家已经rebuy的次数
                sub_match.user_conf[ str(userid) ][ 'rebuy_money' ]     = 0     #玩家已经rebuy到的筹码
                sub_match.user_conf[ str(userid) ][ 'pro_rebuy_money' ] = 0     #预买筹码，还没到帐的筹码 
                sub_match.user_conf[ str(userid) ][ 'rebuy_orderid' ]   = []    #订单id：(lobby_orderid, acct_orderid)                
        
    def delay_apply_match(self, match_obj, userid, username):
        '''延迟报名比赛的玩家信息，成功录入到内存中'''
        #加入赛事的用户列表
            
        if not str(userid) in match_obj.user_list:
            match_obj.user_list.append( str(userid) )
        if not match_obj.user_conf.has_key(str(userid)):
            match_obj.user_conf[ str(userid) ]                      = {}
            match_obj.user_conf[ str(userid) ][ 'username' ]        = username
            match_obj.user_conf[ str(userid) ][ 'user_agent' ]      = ''
            match_obj.user_conf[ str(userid) ][ 'is_trustee' ]      = False #是否是托管状态
            
            match_obj.user_conf[ str(userid) ][ 'rebuy_times' ]     = 0     #玩家已经rebuy的次数
            match_obj.user_conf[ str(userid) ][ 'rebuy_money' ]     = 0     #玩家已经rebuy到的筹码
            match_obj.user_conf[ str(userid) ][ 'pro_rebuy_money' ] = 0     #预买筹码，还没到帐的筹码 
            match_obj.user_conf[ str(userid) ][ 'rebuy_orderid' ]   = []    #订单id：(lobby_orderid, acct_orderid)

        #reEnter
        if match_obj.player_lose_list.has_key(str(userid)):
            match_obj.player_lose_list.pop(str(userid))


        # 电竞赛额外处理  added by WangJian
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
                    sub_match.user_conf[ str(userid) ][ 'is_trustee' ]      = False #是否是托管状态
                    sub_match.user_conf[ str(userid) ][ 'rebuy_times' ]     = 0     #玩家已经rebuy的次数
                    sub_match.user_conf[ str(userid) ][ 'rebuy_money' ]     = 0     #玩家已经rebuy到的筹码
                    sub_match.user_conf[ str(userid) ][ 'pro_rebuy_money' ] = 0     #预买筹码，还没到帐的筹码 
                    sub_match.user_conf[ str(userid) ][ 'rebuy_orderid' ]   = []    #订单id：(lobby_orderid, acct_orderid) 
                #reEnter
                if sub_match.player_lose_list.has_key(str(userid)):
                    sub_match.player_lose_list.pop(str(userid))                    


    def clear_apply(self, matchid):
        '''
            清空报名
        '''
        match = MatchData.get(matchid)
        if not match:
            return False
        match.user_list = []
        match.user_conf = {}

        # 电竞赛额外处理  added by WangJian
        if (match.level == 'E_SPORTS'):
            lists = MatchDB.get_e_sport_extral_matchs(matchid)
            for i in lists:
                sub_match = MatchData.get( i['sub_id'] )
                if not sub_match:
                    continue
                sub_match.user_list = []
                sub_match.user_conf = {}                                    
        

    def quit_match(self, matchid, userid):
        ''' 退赛
            params int matchid 赛事id
                   int userid  用户id
        '''
        #logging.jsinfo('****** quit_match bg....')
        #这个赛事的参赛用户列表
        MatchData.get(matchid).user_list.remove(userid)
        #这里也用到了pop方法哦！
        MatchData.get(matchid).user_conf.pop(userid, None)

        match = MatchData.get(matchid)
        if not match:
            logging.jsinfo('****** quit_match 1111')
            return 1

        # 电竞赛额外处理  added by WangJian
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
            强制不在线玩家退赛
            入参：match_id
            出参：offline_user_list    被踢玩家列表
            编写：liulk
            日期：2012.08.08 11:56
        '''        
        #检查赛事配置，是否需要踢出不在线玩家
        ret = MatchDB.kickout_or_not(match_id)
        
        if not ret:
            #不用踢人
            return None
        else:
            #要踢人
            #初始化踢人列表
            offline_user_list = []
            
            #取该赛事参赛人员列表
            userlist = []
            for item in MatchData.get(match_id).user_list:
                userlist.append(item)
            logging.info('apply userlist is----------> : %s'%userlist)
            userlist_len = len(userlist)
            
            for val in range(userlist_len):
                #检查该用户是否在线True or False
                online = Player.check_user_online_status( userlist[val] )
                if online:
                    continue
                else:
                    #不在线，要踢掉他了，将userid加入踢人列表
                    offline_user_list.append(userlist[val])
                    #同时更新内存中的user_list,  user_conf
                    self.quit_match(match_id, userlist[val])
                    
            #将踢人列表发给代理服务，进行强制退赛
            msg = {
            P.MATCH_ID : match_id,
            P.PLAYER_LIST : offline_user_list,
            }        
            remotename = AGENT_ADDRESS
            logging.info('remotename is : %s'%str(remotename))

            c_sequence_id = ''    # 取子序列号
            data = P.pack().event( P.KICKOUT_OFFLINE_USER ).mid( c_sequence_id ).body( msg ).get()
            Message.send( remotename, data )
            
            logging.info('Inform lobby_misc to kick out the offline users!')
            logging.info('OFFLINE USER_LIST: %s'%offline_user_list)
            
            return offline_user_list
    
    
    
    
    
    
    
    
    
    
    
    
    
