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
        删除指定key
    '''
    allkeys = lserv.hkeys(key)
    
    for sub_key in allkeys:                 #逐一删除子key
        ret = lserv.hdel(key, sub_key)
    
    
def get_gaddr_from_tid(table_id):
    '''
        解析table_id，获取game地址
    '''
    tid = table_id.split('#')
    gameaddr = tid[0]
    return gameaddr
    

    
def record_create_table(table_id, pay_type, big_blind, game_addr):
    '''
        记录不同盲注级别的桌子所在的game服务地址
    '''
    logging.debug('record_create_table: table_id = %s, pay_type = %s, big_blind = %s'
                    %(table_id, pay_type, big_blind))
                    
    #game_addr = get_gaddr_from_tid(table_id)            #解析table_id 得到gameaddr
    
    sub_key = pay_type + '_' + str(big_blind)
    
    level_gaddr = get(LEVEL_GADDR_PREFIX, sub_key)      #获取等级-地址映射数据结构
    
    logging.debug('level_gaddr------> %s'%level_gaddr)
    
    if level_gaddr == None:
        set(LEVEL_GADDR_PREFIX, sub_key, game_addr)
        return
    
    if game_addr not in level_gaddr:                    #redis中没有对应的信息，写一条进去
        set(LEVEL_GADDR_PREFIX, sub_key, game_addr)
    else:
        logging.info('redis has already record the info! %s : %s'%(sub_key, game_addr))
    
    
    
    
    
    
    
    
    
    
    
    
    
