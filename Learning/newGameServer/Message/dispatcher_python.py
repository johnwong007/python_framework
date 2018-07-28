#coding=gbk
'''
version 1.31
rabbitmq client 

         支持发到指定的某一台远程服务
         支持发到指定的远程服务组中的任意一台 
         支持广播发到指定远程服务组下的所有服务

example:
    
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


class Dispatcher:


    def init(self, myname, myaddr, mdaddr, type):
        '''
            params tuple myname (groupname,servicename) groupname为组的名字
                                                        servicename为自己的名字 
                         mydaddr 目前无用
                  string mdaddr rabbitmq-server的地址 需要是amqp的url格式 
                         amqp://192.168.0.252:5673/
                         或者
                         amqp://192.168.0.252:5673/;amqp://192.168.0.252:5674/
                  string type 'read' 或者 'write'
            return  -1 表示 连接rabbit-server 失败
                    -2 表示 声明自己的queue失败
                    -3 表示 声明组的queue失败

        '''
        if type not in ['read','write']:
            logging.error('from init type error')
            return -4
        self.type = type
        self.rbt_server_list = [ ]
        amqp_url_list = mdaddr.split(';')
        for i in amqp_url_list:
            if i:
                self.rbt_server_list.append(i)
        random.shuffle(self.rbt_server_list)
        #当前使用节点列表中的哪个index
        self.current_node_index = 0
        #我的组名字
        self.my_grp_qname =  myname[0]
        #我的service名字 
        self.my_q_name = myname[1] 
        self.mdaddr = mdaddr
        #当前使用节点列表中的哪个index
        return self.connect_rbt_server()

    
    def join_send_info(self, remotename, data):
        ''' 拼接 发送者信息 我的信息 和 发送的实际数据'''
        remote_info = '%s%s'%(str_to_bytes(remotename[0], 8),
                                str_to_bytes(remotename[1], 8))
        my_info = '%s%s'%(str_to_bytes(self.my_grp_qname, 8),str_to_bytes(self.my_q_name, 8))
        return '%s%s%s'%(remote_info,my_info,data)

    
    def send(self, remotename, data, timeout=None):
        '''
             params  tuple remotename  远程服务名 (group, name) (group或name 超过8个字符会报错)
                     data        数据 "hello world"
                     timeout  超时时间 单位 秒   为0则表示阻塞发送 
             return  True or False timeout秒钟之内 发送成功或者失败

        '''
        for i in range(3):
            res = self._send(remotename, data, timeout)
            if res:
                return True
            else:
                self.current_node_index = (self.current_node_index + 1)%len(self.rbt_server_list)
                self.connect_rbt_server()
        return False


    def _send(self, remotename, data, timeout=None):
        '''
             params  tuple remotename  远程服务名 (group, name) (group或name 超过8个字符会报错)
                     data        数据 "hello world"
                     timeout  超时时间 单位 秒   为0则表示阻塞发送 
             return  True or False timeout秒钟之内 发送成功或者失败

        '''
        try:
            if timeout == 0:
                timeout = None
            data = self.join_send_info(remotename,data)
            promise = self.client.basic_publish(exchange = 'poker',
                                           routing_key = remotename[1],
                                           body = data,
                                           )
            #return True
            ress = self.client.wait(promise, None)            
            if ress == {} :
                return True
            else:
                return False
        except:
            logging.error( 'from send %s',traceback.format_exc() )
            return False

            
    def send_group(self, remotename, data, timeout=None):
        '''
             params  tuple remotename  远程服务名 (group, name) (group或name 超过8个字符会报错)
                     data        数据 "hello world"
                     timeout  超时时间 单位 秒   为0则表示阻塞发送 
             return  True or False timeout秒钟之内 发送成功或者失败

        '''
        for i in range(3):
            res = self._send_group(remotename, data, timeout)
            if res:
                return True
            else:
                self.current_node_index = (self.current_node_index + 1)%len(self.rbt_server_list)
                self.connect_rbt_server()
        return False


    def _send_group(self, remotename, data, timeout=None):
        '''
             params  tuple remotename  远程服务名 (group, name) 
                                       (group或name 超过8个字符会报错)

                     data        数据 "hello world"

                     timeout  超时时间 单位 秒   为0则表示阻塞发送 
             return  True or False timeout秒钟之内 发送成功或者失败

        '''
        try:
            if timeout == 0:
                timeout = None
            data = self.join_send_info(remotename,data)
            promise = self.client.basic_publish(exchange = 'poker',
                                           routing_key = remotename[0],
                                           body = data,
                                           )
            ress = self.client.wait(promise, None)
            if ress == {}:
                return True
            else:
                return False
        except:
            logging.error( 'from send_group %s',traceback.format_exc() )
            return False


    def send_broad(self, remotename, data, timeout=None):
        '''
             发送广播消息
             params  tuple remotename  远程服务名 (group, name) (group或name 超过8个字符会报错)
                     data        数据 "hello world"
                     timeout  超时时间 单位 秒   为0则表示阻塞发送 
             return  True or False timeout秒钟之内 发送成功或者失败

        '''
        for i in range(3):
            res = self._send_broad(remotename, data, timeout)
            if res:
                return True
            else:
                self.current_node_index = (self.current_node_index + 1)%len(self.rbt_server_list)
                self.connect_rbt_server()
        return False


    def _send_broad(self, remotename, data, timeout=None):
        '''
             发送广播消息
             params  tuple remotename  远程服务名 (group, name) 
                                       (group或name 超过8个字符会报错)

                     data        数据 "hello world"

                     timeout  超时时间 单位 秒   为0则表示阻塞发送 
             return  True or False timeout秒钟之内 发送成功或者失败

        '''
        try:
            if timeout == 0:
                timeout = None
            data = self.join_send_info(remotename,data)
            promise = self.client.basic_publish(exchange = remotename[0],
                                           body = data,
                                           )
            ress = self.client.wait(promise, None)
            if ress == {}:
                return True
            else:
                return False
        except:
            logging.error( 'from send_group %s',traceback.format_exc() )
            return False


    def receive(self, timeout=1):
        ''' 
             param  float timeout     >=0 阻塞N毫秒
                          timeout如果大于0,最小只能为0.01
             return tuple (group,servicename,data)

                    group 为远程组名
                    servicename 为远程服务名
                    data  为实际数据
        '''
        for i in range(3):
            try:
                return self._receive(timeout)
            except:
                logging.error('from receive error is %s',traceback.format_exc())
                self.current_node_index = (self.current_node_index + 1)%len(self.rbt_server_list)
                self.connect_rbt_server()
        logging.error('from receive unknown dangerous error')
        return None,None,None
                

    def _receive(self, timeout=1):
        ''' 
             param  float timeout     >=0 阻塞N毫秒
                          timeout如果大于0,最小只能为0.01
             return tuple (group,servicename,data)

                    group 为远程组名
                    servicename 为远程服务名
                    data  为实际数据
        '''
        try:
            msg_result = ''
            if timeout == -1:
                msg_result = self.client.wait(self.consume_promise)
            else:
                if timeout <= 0.01:
                    timeout = 0.01
                msg_result = self.client.wait(self.consume_promise,timeout/1000.0)
            if msg_result:
                #给rabbitmq-server一个回应 对应声明consume的时候 no_ack参数 需要为false
                self.client.basic_ack(msg_result)
                body_data = msg_result['body']
                fromgroup = body_data[16:24].replace('\x00', '').strip()
                fromname  = body_data[24:32].replace('\x00', '').strip()
                json_data = body_data[32:]
                return fromgroup,fromname,json_data
            return None,None,None
        except puka.PreconditionFailed:
            logging.warning('from receive %s',traceback.format_exc())
            return None,None,None
        except select.error,e:
            if e[0] == 4:
                logging.warning('from receive select error %s',traceback.format_exc())
            return None,None,None


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
            if not self.declare_my_queue(self.my_q_name):
                #declare myself queue error 
                return -2
            if not self.declare_group_queue(self.my_grp_qname):
                #declare my group queue error 
                return -3
            if self.type == 'read': 
                self.get_consume_promise( [self.my_q_name, self.my_grp_qname])
            logging.info('success init to rabbitmq-server [%s] success',server_url)
            return 1
        except:
            logging.error('fail to connect or init rabbitmq-server ,amqp url is [%s] error is [%s]',server_url, traceback.format_exc())
            time.sleep(0.3)
            return -1
            


    def declare_my_exchange(self):
        ''' 声明exchange poker'''
        promise_exchange = self.client.exchange_declare(exchange='poker',type='direct',durable=True,) 
        res = self.client.wait(promise_exchange)
        #接收广播消息的exchange 名字和组的名字一样
        promise_exchange2 = self.client.exchange_declare(exchange=self.my_grp_qname,type='fanout',durable=True,) 
        res2 = self.client.wait(promise_exchange2)
        return True 


    def declare_my_queue(self, queue_name):
        ''' 声明我自己queuename

            params  string  my_q_name 我自己的queue name
            return True or False
        '''
        promise_queue = self.client.queue_declare(queue=queue_name,
                                                  durable=True,
                                                  arguments={'x-ha-policy':'all',
                                                  }
                                                )
        res = self.client.wait(promise_queue)
        #myqueue和专用的poker的exchange绑定起来
        promise_queue2 = self.client.queue_bind(queue=queue_name,exchange='poker',routing_key=queue_name)
        self.client.wait(promise_queue2)
        return True


    def declare_group_queue(self, group_queue_name):
        ''' 声明我的组的queuename

            params  string  group_queue_name 我的组的queue name
            return True or False
        '''
        promise_queue = self.client.queue_declare(queue=group_queue_name,
                                                 durable=True,
                                                 arguments={'x-ha-policy':'all'}
                                                 )
        res = self.client.wait(promise_queue)
        #myqueue和专用的poker的exchange绑定起来
        promise_queue2 = self.client.queue_bind(queue=group_queue_name,exchange='poker',routing_key=group_queue_name)
        self.client.wait(promise_queue2)
        #组的queue和广播的exchange绑定到一起来
        promise_queue3 = self.client.queue_bind(queue=self.my_q_name,exchange=group_queue_name,)
        self.client.wait(promise_queue3)
        return True


    def get_consume_promise(self,queue_name_list ):
        ''' get consume 
            params list queue_name_list   ['queue1','queue2']
        '''
        self.consume_promise = self.client.basic_consume_multi(
                                                queues = queue_name_list, 
                                                prefetch_count=1,
                                                #no_ack=True,
                                                )

    def unregister(self):
        return True


def str_to_bytes(string, len):
    return struct.pack('%ds' % len, string)
