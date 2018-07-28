#coding=gbk
'''
version 1.0

use rabbitmq to send topic msg

modify time : 2012-04-11 12:00

    
'''
import sys
import JsonUtil as json
import time
import puka
import JsonUtil as json
import random
import select
import struct
import socket
import zlog as logging
import traceback

import JsonUtil


class Rpublish:


    def __init__(self, mdaddr, exname = 'poker_topic'):
        '''
              string mdaddr rabbitmq-server的地址 需要是amqp的url格式 
                     amqp://192.168.0.252:5673/
                     或者
                     amqp://192.168.0.252:5673/;amqp://192.168.0.252:5674/

        '''
        self.exname = exname
        self.rbt_server_list = [ ]
        amqp_url_list = mdaddr.split(';')
        for i in amqp_url_list:
            if i:
                self.rbt_server_list.append(i)
        random.shuffle(self.rbt_server_list)
        #当前使用节点列表中的哪个index
        self.current_node_index = 0
        self.mdaddr = mdaddr
        #当前使用节点列表中的哪个index
        self.connect_rbt_server()

    
    def send(self, topic, args, res, timeout=None):
        '''
            params string topic
                   dict args
                   res  args
        '''
        for i in range(3):
            res = self._send(topic, args, res, timeout)
            if res:
                return True
            else:
                self.current_node_index = (self.current_node_index + 1)%len(self.rbt_server_list)
                self.connect_rbt_server()
        return False


    def _send(self, topic, args, res, timeout=None):
        '''
            params string topic
                   dict args
                   res  args
        '''
        try:
            if timeout == 0:
                timeout = None
            data = JsonUtil.write( (args,res) )
            promise = self.client.basic_publish(exchange = self.exname,
                                           routing_key = topic,
                                           body = data,
                                           )
            ress = self.client.wait(promise, None)
            if ress == {} :
                return True
            else:
                return False
        except:
            logging.error( 'from send %s',traceback.format_exc() )
            return False

            
    def connect_rbt_server(self):
        ''' 连接rabbitmq-server
            return 1  成功  
                   -1 失败
        '''
        for i in range(3):
            for i in range(3):
                if self._connect_rbt_server() == 1:
                    return 1
            self.current_node_index = (self.current_node_index + 1)%len(self.rbt_server_list)
            logging.warning('now change another rabbitmq-server node,please wait a moment')
        return -1


    def _connect_rbt_server(self):
        ''' connnect to rabbitmq server 
            params string server_url amqp的url
            return 1表示成功
        '''
        server_url = self.rbt_server_list[self.current_node_index]
        try:
            self.client = puka.Client(server_url)
            promise = self.client.connect()
            res = self.client.wait(promise)
            if res and res.has_key('server_properties'):
                logging.info('connect to rabbitmq-server [%s] success',server_url)
            else:
                logging.error('fail to connect or init rabbitmq-server ,amqp url is [%s] error is [%s]',server_url, traceback.format_exc())
                return -1
            if not self.declare_my_exchange():
                #declare exchange
                return -4
            return 1
        except:
            logging.error('fail to connect or init rabbitmq-server ,amqp url is [%s] error is [%s]',server_url, traceback.format_exc())
            time.sleep(0.3)
            return -1
            

    def declare_my_exchange(self):
        ''' 声明exchange estopic'''
        promise_exchange = self.client.exchange_declare(exchange=self.exname,type='topic',durable=True,) 
        res = self.client.wait(promise_exchange)
        return True 

