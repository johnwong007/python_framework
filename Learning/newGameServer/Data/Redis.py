#coding=gbk
''' redis处理模块 '''
import redis
import os
import sys
proPath = os.path.abspath(__file__)

proPath = proPath[0:proPath.rfind('/')]
proPath = proPath[0:proPath.rfind('/')]
proPath = proPath[0:proPath.rfind('\\')]
proPath = proPath[0:proPath.rfind('\\')]
sys.path.append(proPath)
sys.path.append('F:\develop\python\\')
from Xml import XmlConfig
XmlConfig.loadFile("../poker_game.xml" )



USER_ADDR_MEM_IP   =  XmlConfig.get("/xml/Redis_addr/user_addr_mem_ip")["value"]

USER_ADDR_MEM_PORT =  XmlConfig.get("/xml/Redis_addr/user_addr_mem_port")["value"]

lserv = redis.Redis( USER_ADDR_MEM_IP, int( USER_ADDR_MEM_PORT ) )


def getall( key ):
    return lserv.hgetall( key )

def get( key, sub_key ):
    return lserv.hget( key, sub_key )

def set( key, sub_key, value ):
    
    return lserv.hset( key, sub_key, value )
    
def delete( key, sub_key ):
    return lserv.hdel( key, sub_key )


  
    