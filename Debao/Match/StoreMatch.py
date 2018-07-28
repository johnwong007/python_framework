#coding=gbk
import os
import zlog as logging
import inspect
import cPickle
import traceback
import threading
import Object
import Object.Match as OM

INTERVAL = 120
_DB_FILE_ = ''
_DATA_EVENT_ = threading.Event()
_DATA_EVENT_.clear()

##赛事持久化信息模块##
# 使用方法：
# import StoreMatch as SM
# SM.INTERVAL = 120 # 设置每2分钟持久化一次
# SM.init() # 初始化模块
# SM.store() #主动触发持久化
# SM.clear() #清楚历史信息

def init(db_file = None):
    '''初始化定时持久化模块'''
    if not db_file:
        db_file = os.environ['_BASIC_PATH_'] + '/var/data/match.db'
    
    global _DB_FILE_
    _DB_FILE_ = db_file
    
    restore() #恢复以前的赛事信息
    
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

def run():
    '''主运行程序'''
    while not Object.END_EVENT.isSet():
        try:
            _DATA_EVENT_.wait(INTERVAL)
            
            _data = OM.get_all_match()
            _store(_data)
            _DATA_EVENT_.clear() 
        except:
            logging.error('error in StoreMatch.run: %s', traceback.format_exc())

def open_db(db_file, mod = 'r'):
    '''打开db文件'''
    dname = os.path.dirname(db_file)
    if not os.path.isdir(dname):
        os.makedirs(dname, 0755)
    
    f = open(db_file, mod)
    return f
    

def init_all_match(data):
    '''初始化所有赛事'''
    all_ins = OM.get_all_match()
    
    for mid, mins in data.items():
        ins = OM.Match()
        info = dir(ins)
        for i in info:
            #是方法跳过
            if inspect.ismethod(getattr(ins, i)):
                continue
            #设置属性
            if hasattr(mins, i):
                setattr(ins, i, getattr(mins, i))
        all_ins[mid] = ins
    
def get_db_content():
    '''获取db文件中的存储内容'''
    if not os.path.isfile(_DB_FILE_):
        return None
    
    f = open_db(_DB_FILE_)
    pick = cPickle.Unpickler(f)
    _data = pick.load()
    return _data

def restore():
    '''恢复赛事当前状态'''
    _data = get_db_content()
    if _data:
        init_all_match(_data)
    

def _store(data):
    '''存储对象'''
    f = open_db(_DB_FILE_, 'w')
    pick = cPickle.Pickler(f, -1)
    pick.dump(data)
    f.close()
    del(pick)

def store():
    '''存储对象事件'''
    _DATA_EVENT_.set()

def clear():
    '''清除db文件'''
    if not os.path.isfile(_DB_FILE_):
        return False
    
    os.remove(_DB_FILE_)
    return True