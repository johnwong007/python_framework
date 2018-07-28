#coding=gbk
''' 消息模块 '''
import dispatcher
import zlog as logging

import XmlConfig

GROUP_NAME    =  XmlConfig.get("/xml/Server_name/group_name")["value"]

LOCAL_ADDR    =  XmlConfig.get("/xml/Server_addr/local_addr")["value"]

MD_ADDR       =  XmlConfig.get("/xml/Server_addr/md_addr")["value"]

message_read  = dispatcher.Dispatcher()
message_write = dispatcher.Dispatcher()



def regist( server_name ):
    #初始化 
    logging.info( '注册地址为：%s'%str( (GROUP_NAME, server_name)) )
    ret = message_read.init( ( GROUP_NAME, server_name ), LOCAL_ADDR, MD_ADDR , 'read')
    if ret == 1:    
        logging.info( 'regist sucess!' )
    else:
        return False
                
    ret = message_write.init( ( GROUP_NAME, server_name ), LOCAL_ADDR, MD_ADDR , 'write')
    
    if ret == 1:
        logging.info( 'regist sucess!' )
    else:
        return False

#发送消息
def sendMessage( remotename, data ):
    
    
    
    if remotename != None:  
        #logging.info( "send to %s, msg is %s, length: %s"%(remotename, data, len( data )) )    
        return message_write.send( remotename, data, 0 )
        
    
    
    return None
    

#接收消息
def receiveMessage():
    
    msg = message_read.receive( 1 )
    
    if msg != ( None, None, None ):
    
        logging.info( "receive msg ,groupname :%s ,servername : %s , msg is %s"% (msg[0],msg[1],msg[2])  )
        
        return msg
        
    return None, None, None

#卸载
def unregist():
    
    logging.info( 'unregist success' )
    return 
    
        


        



