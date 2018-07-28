#coding=utf-8
#Label
import time
import threading

#������
counter=0
#��������
MAX_COUNT=10000
#��������
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






#����ı�ǩ�ļĴ洦
#
#   hang_up_labels = {
#       label : {
#           'c' : ������ӱ�ǩ����Ŀ,
#           'p' : ����ǩid,
#       },
#       ...
#   }
#
labels = dict()



def set( prefix, parent_label=None ):
    '''
        ȡ��ǩ���
        ��� prefix   string  ǰ׺
             parent_rabel   string  ����ǩ����ѡ
        ���� ��ǩ��� = ǰ׺ + ���� + һ��4λ���֣�ͬһ�벻����10000������ɡ�������
              ������ظ����򷵻�False
        
        ����: chende  2011-12-29 23:03:57
        �޸�: 
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
        labels[ parent_label ][ 'c' ] += 1  # �������

    return label

def unset( label ):
    '''
        ȡ��ָ���ı�ǩ
        ��Σ���ǩID
        ���Σ�True ȡ���ɹ� False ȡ��ʧ��
        ����: chende  2011-12-29 23:21:46
        �޸�: 
    '''
    if not labels.has_key( label ):
        return True

    if labels[ label ][ 'c' ] > 0:
        # �ӱ�ǩ��Ϊ0�����޷�ȡ��
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

