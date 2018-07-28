#coding=gbk
'''���ݴ洢ģ��'''

import Pickle as Pc
import Redis as Re
import Message.RMonitor as RM
import os
import threading
import Data
import XmlConfig

# ��ֹ�ź�
END_EVENT = threading.Event()

# �������̵ķ�����
global server_name 

# ��Ϸ�����ַ��ǰ׺
SERVER_ADDR_PREFIX   =  XmlConfig.get("/xml/Redis_addr/server_addr_prefix")["value"]

def register_server( appid ):
    ''' �������������ע�� '''
    global server_name
        
    server_name = appid
    
    return True

def start():
    ''' ���������������������� '''
    global server_name
        
    pickle_x = Pickle( server_name )
        
    table_list = pickle_x.start()
    
    return table_list
    return True

def stop():
    ''' ����KeyboardInterrupt��װ���ڴ������ '''
    global server_name
    
    pickle_x = Pickle( server_name )
    pickle_x.stop()
    
    return True
    
def endSignalHandler(signum, frame):
    ''' ��׽��ֹ�źţ�װ���ڴ������ '''
    global server_name
    
    # ж�ؼ��ģ��
    #��ֹ�رռ�ط����RM.stop()ִ�б������ܼ�������ִ��
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
    ''' ���¼���redis������ '''
    Re.set( SERVER_ADDR_PREFIX, server_name, 50 )
    
    return True
    

class Pickle:
    """���л�ģ��"""

    def __init__( self, servername ):
        
        self.servername = servername
        
        self.saveFile = os.environ['_BASIC_PATH_'] + '/var/pickle/' + servername + '.sav'
        
        if not os.path.exists(self.saveFile):            
            f = file( self.saveFile,'w' )           
            f.close()

    def start( self ):
        ''' ����,������������ '''
        obj_list = Pc.load( self.saveFile )
        
        if obj_list != list(): 
        
            Data.table_list, Data.ut2remote, Data.ut2seatid , Data.tableid2match  = obj_list 

        Re.set( SERVER_ADDR_PREFIX, self.servername, 50 )
        
        print Data.table_list
        return Data.table_list
    
    
    def stop( self ):
        ''' ֹͣ������װ���ڴ� '''
        obj_list = [ Data.table_list, Data.ut2remote, Data.ut2seatid, Data.tableid2match ]
         
        Pc.dump( self.saveFile, obj_list )
        
        Re.delete( SERVER_ADDR_PREFIX, self.servername )