#coding=gbk
'''
    zlog python扩展
    
    @author:huangjh
    @version:1.3  
    注: 不输出文件名，行号

'''

import os
import sys
import string
import types
import logging as logger
import traceback

import Py_zlog
import LogUtil


_BASIC_PATH_ = os.environ['_BASIC_PATH_']

LogUtil.addTimedRotatingFileHandler(
    '%s/var/log/zlog-Error.log' % ( _BASIC_PATH_, ),
    logLevel = "INFO"
)
    
# --- ################## Zlog 相关 ################### --- #
# zlog配置路径
#logger.info('lllllllllllll %s', sys.argv[1])
ZLOG_CONFIG_PATH = _BASIC_PATH_ + "/etc/"+ sys.argv[1] + "_zlog.conf"
#ZLOG_CONFIG_PATH = _BASIC_PATH_ + "/etc/" + "Level_zlog.conf"
# zlog初始化开关
ZLOG_SWITCH = 1
# zlog规则
ZLOG_RULES = "release"

# 初始化zlog
if ZLOG_SWITCH:
    ZLOG_SWITCH = Py_zlog.init( ZLOG_CONFIG_PATH, ZLOG_RULES )

    
# --- ################## Python zlog封装 ################### --- #
# 日志级别
DEBUG = "DEBUG"
INFO = "INFO" 
NOTICE = "NOTICE"
WARNING = "WARNING"
ERROR = "ERROR"
FATAL = "FATAL"

# 级别API映射
_ZLOG_FUNC_ = {
    "DEBUG"     :   Py_zlog.debug,
    "INFO"      :   Py_zlog.info,
    "NOTICE"    :   Py_zlog.notice,
    "WARNING"   :   Py_zlog.warning,
    "ERROR"     :   Py_zlog.error,
    "FATAL"     :   Py_zlog.fatal
}



        
class Logger():
    def __init__(self):
        pass 
    
    def debug(self, msg, *args):
        self._log(DEBUG, msg, args)
    
    def info(self, msg, *args):
        self._log(INFO, msg, args)
        
    def notice(self, msg, *args):
        self._log(NOTICE, msg, args)
        
    def warning(self, msg, *args):
        self._log(WARNING, msg, args)
        
    def error(self, msg, *args):
        self._log(ERROR, msg, args)
        
    def fatal(self, msg, *args):
        self._log(FATAL, msg, args)
        
        
        
    def _log(self, level, msg, args):
        
        """ 调用zlog API打印信息 """
        
        init_msg = self.combineMsg(msg, args)
        writer = _ZLOG_FUNC_.get(level, None)
        if not writer:
            pass
        writer(init_msg)
        
        
    def combineMsg(self, msg, args):
    
        """ 组装消息 """
        
        if not hasattr(types, "UnicodeType"): #if no unicode support...
            msg_obj = str(msg)
        else:
            msg_obj = msg
            if type(msg) not in (types.UnicodeType, types.StringType):
                try:
                    msg_obj = str(msg)
                except UnicodeError:
                    msg_obj = msg      
        if args:
            msg_obj = msg % args
        return msg_obj
        
        
    

        
root = Logger()

def debug(msg, *args):
    """
    Log a message with severity 'DEBUG' on the root logger.
    """
    if ZLOG_SWITCH:
        logger.error( " ZLOG INIT FAILED!!" )
        return None
    root.debug(*((msg,)+args))
    
def info(msg, *args):
    """
    Log a message with severity 'INFO' on the root logger.
    """
    if ZLOG_SWITCH:
        logger.error( " ZLOG INIT FAILED!!" )
        return None
    root.info(*((msg,)+args))

    
def notice(msg, *args):
    """
    Log a message with severity 'NOTICE' on the root logger.
    """
    if ZLOG_SWITCH:
        logger.error( " ZLOG INIT FAILED!!" )
        return None
    root.notice(*((msg,)+args))
    
    
def warning(msg, *args):
    """
    Log a message with severity 'WARNING' on the root logger.
    """
    if ZLOG_SWITCH:
        logger.error( " ZLOG INIT FAILED!!" )
        return None
    root.warning(*((msg,)+args))
    
    
def error(msg, *args):
    """
    Log a message with severity 'ERROR' on the root logger.
    """
    if ZLOG_SWITCH:
        logger.error( " ZLOG INIT FAILED!!" )
        return None
    root.error(*((msg,)+args))
    
    
def fatal(msg, *args):
    """
    Log a message with severity 'FATAL' on the root logger.
    """
    if ZLOG_SWITCH:
        logger.error( " ZLOG INIT FAILED!!" )
        return None
    root.fatal(*((msg,)+args))

def jsinfo(msg, *args):
    logger.info(*((msg,)+args))
    return
  
  
# zlog内存清除
def fini():
    try:
        Py_zlog.fini()
        logger.info( "Py_zlog finish SUC!!" )
    except:
        logger.error( "error in zlog:fini" )
