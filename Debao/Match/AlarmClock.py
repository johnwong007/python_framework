#coding=utf-8
import time

_ALARM_CLOCK_ = {
    # key : awake time,
}

def set(key):
    _ALARM_CLOCK_[ key ] = time.time()

def sleep(key, tSleep):
    '''
        ���ܣ�˯��
        ���أ���˯���򷵻�True�����򷵻�False
        ��д��chend
        ������2012-1-30 11:32:20
        �޸ģ�
    '''
    if _ALARM_CLOCK_.has_key( key ):
        tNow = time.time()
        tAwake = _ALARM_CLOCK_[ key ]
        if tNow > tAwake:
            # time up
            del _ALARM_CLOCK_[ key ]
            return False

    else:
        _ALARM_CLOCK_[ key ] = time.time() + tSleep

    return True

def awake(key):
    if _ALARM_CLOCK_.has_key( key ):
        del _ALARM_CLOCK_[ key ]

    return True
