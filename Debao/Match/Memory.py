#coding=utf-8

import traceback
import zlog as logging
import redis
from Config import *

lserv = redis.Redis(COMMON_REDIS_IP, COMMON_REDIS_PORT)
rserv = redis.Redis(USER_ADDR_MEM_IP, USER_ADDR_MEM_PORT)

def getUserConnection(key):
    return rserv.hgetall(key)

def getall(key):
    return lserv.hgetall(key)

def get(key, sub_key):
    return lserv.hget(key, sub_key)
    
def set(key, sub_key, value):
    return lserv.hset(key, sub_key, value)
    
def hdel_key(key):
    '''
        ɾ��ָ��key
    '''
    allkeys = lserv.hkeys(key)
    
    for sub_key in allkeys:                 #��һɾ����key
        ret = lserv.hdel(key, sub_key)
    
    
def get_gaddr_from_tid(table_id):
    '''
        ����table_id����ȡgame��ַ
    '''
    tid = table_id.split('#')
    gameaddr = tid[0]
    return gameaddr
    

    
def record_create_table(table_id, pay_type, big_blind, game_addr):
    '''
        ��¼��ͬäע������������ڵ�game�����ַ
    '''
    logging.debug('record_create_table: table_id = %s, pay_type = %s, big_blind = %s'
                    %(table_id, pay_type, big_blind))
                    
    #game_addr = get_gaddr_from_tid(table_id)            #����table_id �õ�gameaddr
    
    sub_key = pay_type + '_' + str(big_blind)
    
    level_gaddr = get(LEVEL_GADDR_PREFIX, sub_key)      #��ȡ�ȼ�-��ַӳ�����ݽṹ
    
    logging.debug('level_gaddr------> %s'%level_gaddr)
    
    if level_gaddr == None:
        set(LEVEL_GADDR_PREFIX, sub_key, game_addr)
        return
    
    if game_addr not in level_gaddr:                    #redis��û�ж�Ӧ����Ϣ��дһ����ȥ
        set(LEVEL_GADDR_PREFIX, sub_key, game_addr)
    else:
        logging.info('redis has already record the info! %s : %s'%(sub_key, game_addr))
    
    
    
    
    
    
    
    
    
    
    
    
    
