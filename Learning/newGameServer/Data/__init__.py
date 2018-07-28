#coding=gbk
'''数据存储模块'''

import Pickle as Pc
import Redis as Re
import Message.RMonitor as RM
import os
import threading
import Data
import XmlConfig

# 终止信号
END_EVENT = threading.Event()

# 启动进程的服务名
global server_name 

# 游戏服务地址的前缀
SERVER_ADDR_PREFIX   =  XmlConfig.get("/xml/Redis_addr/server_addr_prefix")["value"]

def register_server( appid ):
    ''' 对启动服务进行注册 '''
    global server_name
        
    server_name = appid
    
    return True

def start():
    ''' 进程启动，加载序列内容 '''
    global server_name
        
    pickle_x = Pickle( server_name )
        
    table_list = pickle_x.start()
    
    return table_list
    return True

def stop():
    ''' 进程KeyboardInterrupt，装载内存的内容 '''
    global server_name
    
    pickle_x = Pickle( server_name )
    pickle_x.stop()
    
    return True
    
def endSignalHandler(signum, frame):
    ''' 捕捉终止信号，装载内存的内容 '''
    global server_name
    
    # 卸载监控模块
    #防止关闭监控服务后，RM.stop()执行报错，不能继续往下执行
    try:
        RM.stop()
    except:
        pickle_x = Pickle( server_name )
        pickle_x.stop()        
        END_EVENT.set()        
        return True
        
    pickle_x = Pickle( server_name )
    pickle_x.stop()    
    END_EVENT.set()
    
    return True

def reSet( server_name ):
    ''' 重新加载redis的内容 '''
    Re.set( SERVER_ADDR_PREFIX, server_name, 50 )
    
    return True
    

class Pickle:
    """序列化模块"""

    def __init__( self, servername ):
        
        self.servername = servername
        
        self.saveFile = os.environ['_BASIC_PATH_'] + '/var/pickle/' + servername + '.sav'
        
        if not os.path.exists(self.saveFile):            
            f = file( self.saveFile,'w' )           
            f.close()

    def start( self ):
        ''' 启动,批量加载序列 '''
        obj_list = Pc.load( self.saveFile )
        
        if obj_list != list(): 
        
            Data.table_list, Data.ut2remote, Data.ut2seatid , Data.tableid2match  = obj_list 

        Re.set( SERVER_ADDR_PREFIX, self.servername, 50 )
        
        print Data.table_list
        return Data.table_list
    
    
    def stop( self ):
        ''' 停止，批量装载内存 '''
        obj_list = [ Data.table_list, Data.ut2remote, Data.ut2seatid, Data.tableid2match ]
         
        Pc.dump( self.saveFile, obj_list )
        
        Re.delete( SERVER_ADDR_PREFIX, self.servername )