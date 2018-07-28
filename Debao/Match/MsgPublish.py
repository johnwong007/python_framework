#coding=utf-8

import traceback
import zlog as logging
import threading

send_lock = threading.Lock()

class LOCK:
    '''
    ȫ�Զ��ӽ���
    '''
    def __init__(self, lock):
        self._lock = lock
        self._lock.acquire()
        self._isRelease = False

    def acquire(self):
        # ȷ���ͷ���������������
        if self._isRelease :
            self._lock.acquire()
            self._isRelease = False

    def release(self):
        self._lock.release()
        self._isRelease = True

    def __del__(self):
        if not self._isRelease :
            self._lock.release()

import Rpublish

from Config import *

publisher = None

def init():
    global publisher
    publisher = Rpublish.Rpublish( MD_ADDRESS )
    return True

def send(topic, args, res={}, timeout=None):
    #lock_you = LOCK( send_lock ) # Ŀǰ����Ҫ��
    logging.debug( "publish msg. args=%s, res=%s"%(str(args), str(res)) )
    ret = publisher.send(topic, args, res, timeout)
    logging.debug( "publish over" )
    return ret

