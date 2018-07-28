#coding:utf8
'''
编写测试代码，学习服务器代码
'''
import traceback
import logging
logging.basicConfig(filename='./jsinfo.log', level=logging.DEBUG)
import os
import sys
proPath = os.path.abspath(__file__)

proPath = proPath[0:proPath.rfind('/')]
proPath = proPath[0:proPath.rfind('/')]
proPath = proPath[0:proPath.rfind('\\')]
proPath = proPath[0:proPath.rfind('\\')]
sys.path.append(proPath)
sys.path.append('F:\develop\python\\')
from Protocol import Key as K
from Json import JsonUtil as json
import Config
import time
import re
from Data import Data

def divide(msg):
    '''解包'''
    try:
    	pack = json.read(msg)
    	head = pack.get(K.HEADER, None)
    	body = pack.get(K.BODY, None)

    	if head == None or body == None:
    		errMsg = '包头或者包体内容为空，非法的消息'
    		logging.info(errMsg)
    		print(errMsg)
    		return None
        
        command_id = head.get(K.COMMAND_ID, None)
        connect_id = head.get(K.CONNECT_ID, None)

        user_id = body.get(K.USER_ID, None)
        table_id = body.get(K.TABLE_ID, None)

        print("%X"%command_id)
        print("%s"%connect_id)
        print("%s"%user_id)
        print("%s"%table_id)
        if command_id == None or connect_id == None or user_id == None or table_id == None:
            errMsg = "指令或者桌子id或者userid或者connectid为空，非法的消息"
            logging.info(errMsg)
            print(errMsg)

        timestamp = head.get(K.TIMESTAMP, 0)
        print("%s"%timestamp)

        if time.time() > timestamp + Config.MESSAGE_TIME_OUT:
            errMsg = "消息超时,不处理,发送时间:%s,当前时间:%s"%( timestamp,time.time() )
            logging.info(errMsg)
            print(errMsg)
            return None

        msg = body
        msg[K.COMMAND_ID] = command_id
        msg[K.CONNECT_ID] = connect_id
        print(msg)
        return msg
    except:
        logging.info(traceback.format_exc())
        print(traceback.format_exc())
        return dict()

def combine(connid, response, msg):
    try:
        pack = {
            K.HEADER: {
                K.CONNECT_ID: connid,
                K.TIMESTAMP: time.time(),
                K.COMMAND_ID: response,
            },
            K.BODY: msg
        }
        pack = json.write(pack)
        return pack
    except:
        errMsg = traceback.format_exc()
        logging.info(errMsg)
        print(errMsg)
        return json.write(dict())

def _getPlayerUidsByTableid(tableid):
    table = Data.table_list.get(tableid, None)
    if table != None:
        player_uids = table.getPlayersUid()
    else:
        player_uids = list()
    return player_uids

def _getPlayerUidsByTableidNew(tableid, chat_type=Config.CHAT_COMMON):
    table = Data.table_list.get(tableid, None)
    player_uids = []
    
    pattern_android = re.compile(Config.ANDROID)
    pattern_flash = re.compile(Config.FLASH)
    pattern_pc = re.compile(Config.PC)
    pattern_ios = re.compile(Config.IOS)

    if table != None:
        for player in table.seats.values():
            if None != player:
                if pattern_android.match(player.user_agent) != None and pattern_android.match(player.user_agent).group() == Config.ANDROID:
                    user_agent = Config.ANDROID
                    
                elif patton_flash.match(player.user_agent) != None and patton_flash.match(player.user_agent).group() == Config.FLASH:
                    user_agent = Config.FLASH
                
                elif patton_pc.match(player.user_agent) != None and patton_pc.match(player.user_agent).group() == Config.PC:
                    user_agent = Config.PC
                
                elif patton_ios.match(player.user_agent) != None and patton_ios.match(player.user_agent).group() == Config.IOS:
                    user_agent = Config.IOS
                else:
                    logging.info('except_solution  player.user_agent=%s patton_android.match(player.user_agent)=%s patton_flash.match(player.user_agent)=%s patton_pc.match(player.user_agent)=%s  patton_ios.match(player.user_agent)=%s', player.user_agent, patton_android.match(player.user_agent), patton_flash.match(player.user_agent), patton_pc.match(player.user_agent), patton_ios.match(player.user_agent)) 
                    user_agent = Config.FLASH 
                if chat_type == Config.CHAT_ONLY_FLASH:
                    if user_agent in [Config.FLASH, Config.PC]:
                        player_uids.append(player.userid)
                elif chat_type == Config.CHAT_COMMON or chat_type == Config.CHAT_ALL:
                    if user_agent in [ Config.FLASH, Config.PC, Config.ANDROID, Config.IOS]:
                        player_uids.append( player.userid )
                else:
                    logging.info("wrong chat type!!!!!!")   
    else:
        player_uids = list()
    return player_uids

def _getRemotename(userid, tableid):
    if Data.ut2remote.has_key(str(userid)+'_'+str(tableid)):
        group_name, server_name, connid = Data.ut2remote.get(str(userid)+'_'+str(tableid))
        return (group_name, server_name, connid)
    else:
        return None, None

def sendMessage(userids, tableid, msg, response):
    table = Data.table_list.get(tableid, None)
    if table != None:
        msg[K.HAND_ID] = table.hand_id
        if len(msg[K.HAND_ID]) < 4:
            msg[K.HAND_ID] = ''
    if type(userids)==list:
        ZFC = 'ABCDEFGHIJKLMNOPQRST'
        tmp_msg = combine(ZFC, response, msg)


if __name__=='__main__':
  msg='{"0003":{"0005":131096,"0007":11519789965,"0006":"YjkwNGRiZWFlZjk4MDNiOTViNTQ0ZDY4MTRlZGRmYTE=60103252","0008":4634.0},"0004":{"3026":"GOLD","2003":"3300","2004":"ksir","5029":"970144603.8","2009":"20000.0","1002":"GAME001#0000000000000000CASH000","2061":"192.168.23.34","504C":970144604,"2003":"3300","2004":"ksir","0009":"FLASH/2.0"}}'
  divide(msg)
  pack = combine('YjkwNGRiZWFlZjk4MDNiOTViNTQ0ZDY4MTRlZGRmYTE=60103252',0x80020018,{'code':0,'msg':'success!'})
  print(pack)

  sendMessage([4454,4547], "52145245", "test", 131096)








