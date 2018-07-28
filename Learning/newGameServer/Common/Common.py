#coding=gbk
''' 德州扑克公用函数 '''

import zlog as logging
import inspect
import os
import sys
import datetime
import time
import zlog as logging
import fcntl
import inspect
import signal
import JsonUtil as json
import Common

__NO_DEFAULT_DATA__ = "<NO_DEFAULT_DATA>"

def invokeAutoMatchArgs(fun, inargs):

    funinfo=inspect.getargspec(fun)

    _name=funinfo[0]    # 参数列表
    if len(_name) == 0:
        # 这是一个不需要入参的函数
        return fun()


    _defval=list(funinfo[-1] or ()) # 默认值列表
    _args=[]

    # 填充默认值列表，没有默认值的以 NO_DEFAULT_DATA 值填充
    _defval = [__NO_DEFAULT_DATA__ for i in range(len(_name)-len(_defval))]+_defval

    # 组织参数列表
    for idx, argname in enumerate(_name):
        # 参数传入
        if 'self' == argname :
            continue

        if inargs.has_key(argname):
            _args.append(inargs[argname])
            
        elif _defval[idx] != __NO_DEFAULT_DATA__: # 参数没有传入,检查有没有默认值
            _args.append(_defval[idx])

        else: # 参数错误
            logging.error( "缺少参数%s"%argname )
            return False

    return fun(*_args)

   
def getNow():
    
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) 
    
class Recorder:
    
    def __init__(self,deskid,suffix='txt'):
        self.filename = '.' + deskid + getNow() + '.' + suffix
        self._f = open(self.filename,'a')
        self.record('--------------------------------------------')
        
    def record(self,record_data):
        self._f.write(getNow()+':'+json.write(record_data)+'\n')
        
    def __del__(self):
        self.record('--------------------------------------------')
        self._f.close()
   
    
class Timer:
    def __init__(self, ID=""):
        self._beginTime = datetime.datetime.now()
        self._ID = ID
        self._addInfo = ""

    def taketimes(self):
        # 返回已经耗时
        _tmp = datetime.datetime.now() - self._beginTime
        _timeDiff =  _tmp.seconds*1000000 + _tmp.microseconds
        return _timeDiff/1000

    def setAddInfo(self, addInfo):
        self._addInfo = self._addInfo + addInfo + " "
        return True

    def __del__(self):
        _tmp = datetime.datetime.now() - self._beginTime
        _timeDiff =  _tmp.seconds*1000000 + _tmp.microseconds
        logging.info( "%s 耗时 %s 毫秒 %s", self._ID, str(_timeDiff/1000), self._addInfo )
        
IS_STOP_SERVER_SIGNAL = False     
SEQ_UP_LIMIT = 1000000
class Sequence:
    def __init__(self):
        self.seq = 0
    
    def get_seq(self):
        #获取最新的sequence
        tmp = self.seq
        self.seq += 1
        if self.seq > SEQ_UP_LIMIT:
            self.seq = 0
        return tmp
sequence = Sequence()    #定义一个共享对象


GROUP_NAME = 'c'
SERVER_NAME = 'c'

special_ip_list = [ '192.168.1.1', '113.89.186.205',   '119.147.113.82','58.253.96.21', '119.145.41.230', '113.89.186.205', '14.153.249.154', '14.153.251.147' ]

#按游戏上面所在的盲注级别，从小到大排好的game
GAME_LIST = [ 'GAME001' ]

