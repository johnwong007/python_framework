#coding=utf-8
import time

_ALARM_CLOCK_ = {
    # key : awake time,
}

def set(key):
    _ALARM_CLOCK_[ key ] = time.time()

def sleep(key, tSleep):
    '''
        功能：睡眠
        返回：在睡眠则返回True，否则返回False
        编写：chend
        创建：2012-1-30 11:32:20
        修改：
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
