#coding=gbk
"""
MonitorService��Basicģ��

version: 1.1
    1.1 ��� SWITCH OFF ʱ���alert����

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
    """��ط���Ŀͻ���
    """
    
    monitor_type = 'basic'
    
    def __init__(self, app_id, svc_addr):
        """���캯��
        ������
            app_id: ����ص�Ӧ�õ�ID
            svc_addr: ��ط���˵ĵ�ַ
        """
        self.app_id = app_id
        self.svc_addr = svc_addr
        self._end_event = threading.Event()
        
    def _call(self, cmd_id, data):
        """��������
        ������
            cmd_id: ִ�е�����
            data: ��������ص�����
        û�з���
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
        """�������ݲ����ջظ�
        ������
            cmd_id: ִ�е�����
            data: ��������ص�����
            timeout: ��ʱ����
        ���ط���˵Ļظ�
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(timeout)
        try:
            s.sendto(JsonUtil.write({
                        'app_id': self.app_id,
                        'cmd_id': cmd_id,
                        'data': data,
                     }), self.svc_addr)
            return JsonUtil.read(s.recv(60000)) # ����涨���ݰ����64K
        finally:
            s.close()

    def register(self, args):
        """register
            args:   ע�������dict��ʽ������mobiles��emails�����ṩһ����
                    mobiles���ֻ������list��emails���ʼ���ַ��list��
                    max_idle_time��������ʱ�䣬�������ʱ�䲻֪ͨ�ͻ�澯��
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
        """���͸澯
        """
        self._call('alert', {
                      'short_msg': short_msg,
                      'long_msg': long_msg,
                      'encoding': encoding,
        })
        logging.info('send alert:%s, %s', short_msg, long_msg)
        
    def inform(self, data=None):
        """����֪ͨ
        """
        try:
            self._call('inform', data)
            logging.debug('monitor inform')
        except:
            pass
        
    def _loop_inform(self, data, interval):
        """�Զ�ѭ��֪ͨ
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
        """�����Զ�ѭ��֪ͨ
        """
        self._end_event.clear()
        th = threading.Thread(target=self._loop_inform, args=(data, interval))
        th.setDaemon(True)
        th.start()
 
    def stop_loop(self):
        """�Զ�ѭ��ֹ֪ͨͣ
        """
        self._end_event.set()
    
    @staticmethod
    def get_stats(svc_addr, timeout=4):
        """��ȡ����app״̬��super���
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(timeout)
        try:
            s.sendto(JsonUtil.write({
                        'cmd_id': Client.monitor_type + '_stats',
                        'data': None,
                     }), svc_addr)
            return JsonUtil.read(s.recv(60000)) # ����涨���ݰ����64K
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
                      ͬһ̨���� ������������ͬ���̵�my_app_name��ͬ 
                string mq_addr  rabbitmq��amqp��ʽ���ַ���
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
    ''' �澯�ӿ� '''
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
    ''' ����Լ�����Ϣ
        params tuple remotename   (groupname, servicename)
               int   interval  ÿ����÷�һ����Ϣ
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
    ''' �������Ľ��ע��'''
    try:
        global MBC
        res = MBC.unregister()
        if res['code'] != 301:
            logging.warning('monitor unregister %s',res)
    except Exception,ex:
        logging.error( "Error: %s" % ex )
        logging.error( traceback.format_exc() )


def ping_reply(*arglist,**arglists):
    ''' ���յ�ping��Ϣ�Ժ�Ļظ� 
        ��Ҫ������Ϣ�ķ������ָ�������ֶ�Ӧ
    '''
    try:
        global MBC
        global reply_info
        reply_info['is_reply'] = True
        MBC.inform()          
    except Exception,ex:
            logging.error( "Error: %s" % ex )
            logging.error( traceback.format_exc() )
