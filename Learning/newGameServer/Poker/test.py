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

if __name__=='__main__':
	print('__main__')
	msg = '{"0003":{"0005":131096,"0007":1519723115,"0006":"YjkwNGRiZWFlZjk4MDNiOTViNTQ0ZDY4MTRlZGRmYTE=60103252","0008":4634.0},"0004":{"3026":"GOLD","2003":"3300","2004":"ksir","5029":"970144603.8","2009":"20000.0","1002":"GAME001#0000000000000000CASH000","2061":"192.168.23.34","504C":970144604,"2003":"3300","2004":"ksir","0009":"FLASH/2.0"}}'
    divide(msg)



