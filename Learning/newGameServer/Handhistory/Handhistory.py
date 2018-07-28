#coding=gbk
'''牌谱记录模'''
from Message import dispatcher
import random
import JsonUtil as json
import zlog as logging
import traceback
from Protocol import Command as C
from Protocol import Key     as K
import Version

import XmlConfig
CLIENT_GROUP = XmlConfig.get("/xml/Paipu/client_group")["value"]
CLIENT_NAME  = XmlConfig.get("/xml/Paipu/client_name")["value"]
SERVER_GROUP = XmlConfig.get("/xml/Paipu/server_group")["value"]
SERVER_NAME  = XmlConfig.get("/xml/Paipu/server_name")["value"]
MD_ADDR      =  XmlConfig.get("/xml/Server_addr/md_addr")["value"]
MY_ADDR = 'tcp://'
DELAY = 4
try:
    CLIENT_MD = dispatcher.Dispatcher()
    CLIENT_MD.init([CLIENT_GROUP, CLIENT_NAME], MY_ADDR, MD_ADDR,'write')
except:
    logging.error( traceback.format_exc() )


def send(msg):
    ''' 发送消息 '''
    CLIENT_MD.send((SERVER_GROUP, SERVER_NAME), msg, DELAY)

class Handhistory:
    ''' 牌谱类 '''
    def __init__( self, table_id, hand_id ):
        self.table_id = table_id
        self.hand_id = hand_id
        self.content = []

    def record( self, commond_id, msg ):
        ''' 记录器 '''
        try:
            msg = Version.deformator( msg )            
            commond_id = Version.R_CMD.get(commond_id, commond_id)

            self.content.append( [commond_id, msg] )
            if commond_id == 'PRIZE_MSG':
                msg = json.write([self.table_id, self.hand_id, self.content])
                send( msg )
        except:
            logging.error(traceback.format_exc())  
            


