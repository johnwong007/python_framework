#coding=utf-8

import traceback
import zlog as logging
import threading

send_lock = threading.Lock()

class LOCK:
    '''
    全自动加解锁
    '''
    def __init__(self, lock):
        self._lock = lock
        self._lock.acquire()
        self._isRelease = False

    def acquire(self):
        # 确保释放了锁才能申请锁
        if self._isRelease :
            self._lock.acquire()
            self._isRelease = False

    def release(self):
        self._lock.release()
        self._isRelease = True

    def __del__(self):
        if not self._isRelease :
            self._lock.release()

import dispatcher

from Config import *

msg_queue_rec = dispatcher.Dispatcher()
msg_queue_send = dispatcher.Dispatcher()
local_address = None

def init(serv_name):
    global local_address
    local_address = (LOCAL_GROUP_NAME, serv_name)
    logging.info( "local_address = %s"%str(local_address) )
    msg_queue_send.init(local_address, LOCAL_IP, MD_ADDRESS, 'write')
    return msg_queue_rec.init(local_address, LOCAL_IP, MD_ADDRESS, 'read')

def receive( timeout=0 ):
    group, name, data = msg_queue_rec.receive(timeout)
    if None != data:
        logging.info( "receive from %s, msg is %s"%( (group, name), data ) )
    return group, name, data

def send(remotename, data, timeout=0):
    lock_you = LOCK( send_lock )
    logging.info( "send to %s, msg is %s"%(remotename, data) )
    ret = msg_queue_send.send(remotename, data, timeout)
    logging.debug( "send over, send_ret=%s"%str(ret) )
    return ret

def unregister():
    msg_queue_rec.unregister()
    msg_queue_send.unregister()



