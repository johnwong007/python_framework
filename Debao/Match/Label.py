#coding=utf-8
#Label
import time
import threading

#计数器
counter=0
#最大计数器
MAX_COUNT=10000
#计数器锁
counter_lock = threading.Lock()

def get_cnt():
    LOCK( counter_lock )
    global counter
    counter += 1
    if counter >= MAX_COUNT:
        counter = 0
    return counter

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






#挂起的标签的寄存处
#
#   hang_up_labels = {
#       label : {
#           'c' : 挂起的子标签的数目,
#           'p' : 父标签id,
#       },
#       ...
#   }
#
labels = dict()



def set( prefix, parent_label=None ):
    '''
        取标签编号
        入参 prefix   string  前缀
             parent_rabel   string  父标签，可选
        出参 标签编号 = 前缀 + 日期 + 一个4位数字（同一秒不会有10000次请求吧。。。）
              如果有重复，则返回False
        
        创建: chende  2011-12-29 23:03:57
        修改: 
    '''
    suffix = str( get_cnt() )
    suffix = suffix.zfill( 4 )

    today = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    today = today[-12:]

    label = str(prefix) + today + suffix
    
    if labels.has_key( label ):
        return False

    labels[ label ] = { 'c' : 0, 'p' : None }
    if labels.has_key( parent_label ):
        labels[ label ][ 'p' ] = parent_label
        lol = LOCK( counter_lock )
        labels[ parent_label ][ 'c' ] += 1  # 这里加锁

    return label

def unset( label ):
    '''
        取消指定的标签
        入参：标签ID
        出参：True 取消成功 False 取消失败
        创建: chende  2011-12-29 23:21:46
        修改: 
    '''
    if not labels.has_key( label ):
        return True

    if labels[ label ][ 'c' ] > 0:
        # 子标签不为0，则无法取消
        return False

    parent_label = labels[ label ][ 'p' ]
    desc( parent_label )

    del labels[label]

    return True

def desc( label ):
    if labels.has_key( label ):
        lol = LOCK( counter_lock )
        labels[ label ][ 'c' ] -= 1

def has_key( label ):
    return labels.has_key( label )

