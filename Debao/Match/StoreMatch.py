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

##���³־û���Ϣģ��##
# ʹ�÷�����
# import StoreMatch as SM
# SM.INTERVAL = 120 # ����ÿ2���ӳ־û�һ��
# SM.init() # ��ʼ��ģ��
# SM.store() #���������־û�
# SM.clear() #�����ʷ��Ϣ

def init(db_file = None):
    '''��ʼ����ʱ�־û�ģ��'''
    if not db_file:
        db_file = os.environ['_BASIC_PATH_'] + '/var/data/match.db'
    
    global _DB_FILE_
    _DB_FILE_ = db_file
    
    restore() #�ָ���ǰ��������Ϣ
    
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

def run():
    '''�����г���'''
    while not Object.END_EVENT.isSet():
        try:
            _DATA_EVENT_.wait(INTERVAL)
            
            _data = OM.get_all_match()
            _store(_data)
            _DATA_EVENT_.clear() 
        except:
            logging.error('error in StoreMatch.run: %s', traceback.format_exc())

def open_db(db_file, mod = 'r'):
    '''��db�ļ�'''
    dname = os.path.dirname(db_file)
    if not os.path.isdir(dname):
        os.makedirs(dname, 0755)
    
    f = open(db_file, mod)
    return f
    

def init_all_match(data):
    '''��ʼ����������'''
    all_ins = OM.get_all_match()
    
    for mid, mins in data.items():
        ins = OM.Match()
        info = dir(ins)
        for i in info:
            #�Ƿ�������
            if inspect.ismethod(getattr(ins, i)):
                continue
            #��������
            if hasattr(mins, i):
                setattr(ins, i, getattr(mins, i))
        all_ins[mid] = ins
    
def get_db_content():
    '''��ȡdb�ļ��еĴ洢����'''
    if not os.path.isfile(_DB_FILE_):
        return None
    
    f = open_db(_DB_FILE_)
    pick = cPickle.Unpickler(f)
    _data = pick.load()
    return _data

def restore():
    '''�ָ����µ�ǰ״̬'''
    _data = get_db_content()
    if _data:
        init_all_match(_data)
    

def _store(data):
    '''�洢����'''
    f = open_db(_DB_FILE_, 'w')
    pick = cPickle.Pickler(f, -1)
    pick.dump(data)
    f.close()
    del(pick)

def store():
    '''�洢�����¼�'''
    _DATA_EVENT_.set()

def clear():
    '''���db�ļ�'''
    if not os.path.isfile(_DB_FILE_):
        return False
    
    os.remove(_DB_FILE_)
    return True