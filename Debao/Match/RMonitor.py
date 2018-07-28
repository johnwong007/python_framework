#coding=gbk
"""
MonitorService的Basic模块

version: 1.1
    1.1 添加 SWITCH OFF 时候的alert处理

"""
import os
import sys
import time
import socket
import zlog as logging
import threading
import traceback


import JsonUtil
import XmlConfig
from . import dispatcher
XmlConfig.loadFile(os.environ['_BASIC_PATH_'] + '/etc/monitor.xml')


############################################################



class Client:
    """监控服务的客户端
    """
    
    monitor_type = 'basic'
    
    def __init__(self, app_id, svc_addr):
        """构造函数
        参数：
            app_id: 被监控的应用的ID
            svc_addr: 监控服务端的地址
        """
        self.app_id = app_id
        self.svc_addr = svc_addr
        self._end_event = threading.Event()
        
    def _call(self, cmd_id, data):
        """发送数据
        参数：
            cmd_id: 执行的命令
            data: 跟命令相关的数据
        没有返回
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.sendto(JsonUtil.write({
                        'app_id': self.app_id,
                        'cmd_id': cmd_id,
                        'data': data,
                     }), self.svc_addr)
        finally:
            s.close()
        
    def _call2(self, cmd_id, data, timeout=2):
        """发送数据并接收回复
        参数：
            cmd_id: 执行的命令
            data: 跟命令相关的数据
            timeout: 超时限制
        返回服务端的回复
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(timeout)
        try:
            s.sendto(JsonUtil.write({
                        'app_id': self.app_id,
                        'cmd_id': cmd_id,
                        'data': data,
                     }), self.svc_addr)
            return JsonUtil.read(s.recv(60000)) # 网络规定数据包最大64K
        finally:
            s.close()

    def register(self, args):
        """register
            args:   注册参数，dict格式，里面mobiles和emails最少提供一个，
                    mobiles是手机号码的list，emails是邮件地址的list，
                    max_idle_time是最大空闲时间，超过这个时间不通知就会告警。
        """
        self._end_event.clear()
        data = {'max_idle_time': 120, 'monitor_type': self.monitor_type}
        data.update(args)
        try:
            ret = self._call2('register', data)
            if ret['code'] < 0:
                raise Exception(ret)
        except:
            logging.error('monitoring register failed: [%s] %s',
                            self.app_id, traceback.format_exc())
            raise
        return ret
        
    def unregister(self):
        """unregister
        """
        self._end_event.set()
        try:
            ret = self._call2('unregister', None)
            if ret['code'] < 0:
                raise Exception(ret)
        except:
            logging.error('monitoring unregister failed: [%s] %s',
                            self.app_id, traceback.format_exc())
            return
        return ret
        
    def alert(self, short_msg, long_msg, encoding='utf-8'):
        """发送告警
        """
        self._call('alert', {
                      'short_msg': short_msg,
                      'long_msg': long_msg,
                      'encoding': encoding,
        })
        logging.info('send alert:%s, %s', short_msg, long_msg)
        
    def inform(self, data=None):
        """单次通知
        """
        try:
            self._call('inform', data)
            logging.debug('monitor inform')
        except:
            pass
        
    def _loop_inform(self, data, interval):
        """自动循环通知
        """
        while True:
            self._end_event.wait(interval)
            if self._end_event.isSet():
                break
            try:
                self.inform(data)
            except:
                logging.error('monitoring inform failed: [%s] %s',
                                self.app_id, traceback.format_exc())
        
    def start_loop(self, data=None, interval=60):
        """启动自动循环通知
        """
        self._end_event.clear()
        th = threading.Thread(target=self._loop_inform, args=(data, interval))
        th.setDaemon(True)
        th.start()
 
    def stop_loop(self):
        """自动循环通知停止
        """
        self._end_event.set()
    
    @staticmethod
    def get_stats(svc_addr, timeout=4):
        """获取所有app状态（super命令）
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(timeout)
        try:
            s.sendto(JsonUtil.write({
                        'cmd_id': Client.monitor_type + '_stats',
                        'data': None,
                     }), svc_addr)
            return JsonUtil.read(s.recv(60000)) # 网络规定数据包最大64K
        finally:
            s.close()


#######################################################################

MBC = None
MONITOR_RBT_WRITE = None
SWITCH = 'ON'
reply_info = {
    'is_reply' : True,
    'ping_time' : time.time(),
}


def start(q_name, my_app_name, mq_addr):
    ''' 
        params  tuple q_name
                string my_app_name   
                      同一台机器 不可有两个相同进程的my_app_name相同 
                string mq_addr  rabbitmq的amqp格式的字符串
    '''
    try :
        init(q_name, my_app_name)
        global MONITOR_RBT_WRITE
        MONITOR_RBT_WRITE = dispatcher.Dispatcher()
        MONITOR_RBT_WRITE.init( q_name, '', mq_addr, 'write')
    except Exception,ex:
        logging.error( "Error: %s" % ex )
        logging.error( traceback.format_exc() )

def init(q_name, my_app_name):
    ''' '''
    swtich = XmlConfig.get('/monitor')
    if swtich.get('switch','OFF').upper() == 'OFF':
        global SWITCH
        logging.info('the monitor is not turing on')
        SWITCH = 'OFF' 
        return
    monitor_serv_info = XmlConfig.get('/monitor/monitor_serv_addr')
    host = monitor_serv_info['host']
    port =int(monitor_serv_info['port'])
    max_idle_time = XmlConfig.get('/monitor/max_idle_time')
    alert_inverval = XmlConfig.get('/monitor/alert_interval')
    keepers_info = XmlConfig.list('/monitor/keepers/')
    emails  = []
    mobiles = []
    for i in keepers_info.values():
        emails.extend(i['emails'].split(','))
        mobiles.extend(i['mobiles'].split(','))
    global MBC 
    MBC = Client(my_app_name, (host, port) )
    res = MBC.register({
        'mobiles': mobiles,
        'emails': emails,
        'max_idle_time': int(max_idle_time),
        'alert_interval': alert_inverval,
    })
    if res['code'] != 201:
        logging.warning('monitor register %s',res)
    MBC._end_event.clear()
    ping_send_thread = threading.Thread(target=ping_send, args=( q_name, float(max_idle_time)/3.0))
    ping_send_thread.setDaemon(True)
    ping_send_thread.start()


def alert(shortmsg, longmsg, charset='utf-8'):
    ''' 告警接口 '''
    try :
        global SWITCH
        if SWITCH == 'OFF':
            logging.error('SWITCH=OFF shortmsg[%s],longmsg[%s]',shortmsg,longmsg)
            return
        global MBC
        MBC.alert(shortmsg, longmsg, charset)
    except Exception,ex:
        logging.error( "Error: %s" % ex )
        logging.error( traceback.format_exc() )


def ping_send(remotename, interval = 100):
    ''' 向给自己发消息
        params tuple remotename   (groupname, servicename)
               int   interval  每隔多久发一次消息
    '''
    try :
        global MONITOR_RBT_WRITE 
        global MBC
        global reply_info
        while True:
            MBC._end_event.wait(interval)
            if MBC._end_event.isSet():
                break
            try:
                data = {  
                         "0003":{"0005":0x00000001},
                         "0004":{},
                       }
                data = JsonUtil.write( data )
                MONITOR_RBT_WRITE.send(remotename, data)
                if True == reply_info['is_reply']:
                    reply_info['is_reply'] = False
                    reply_info['ping_time'] = time.time()
                logging.info('send [ping] to myself through rabbitmq')
            except:
                logging.warning('from ping_send %s',traceback.format_exc())
    except Exception,ex:
        logging.error( "Error: %s" % ex )
        logging.error( traceback.format_exc() )


def stop():
    ''' 向监控中心解除注销'''
    try:
        global MBC
        res = MBC.unregister()
        if res['code'] != 301:
            logging.warning('monitor unregister %s',res)
    except Exception,ex:
        logging.error( "Error: %s" % ex )
        logging.error( traceback.format_exc() )


def ping_reply(*arglist,**arglists):
    ''' 接收到ping消息以后的回复 
        需要接收消息的服务程序指定命令字对应
    '''
    try:
        global MBC
        global reply_info
        reply_info['is_reply'] = True
        MBC.inform()          
    except Exception,ex:
            logging.error( "Error: %s" % ex )
            logging.error( traceback.format_exc() )
