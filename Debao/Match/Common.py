#coding=utf-8

import time
import datetime
import zlog as logging

# ʱ��������ڵ�ת��
def timestamp2date( stamp ):
    ltime=time.localtime( stamp )
    timeStr=time.strftime("%Y-%m-%d %H:%M:%S", ltime)

    return timeStr

# ���ڵ�ʱ�����ת��
def date2timestamp( date ):
    tTmp = time.strptime(date,"%Y-%m-%d %H:%M:%S")
    dateC = datetime.datetime( *tTmp[:6] )
    timestamp=time.mktime(dateC.timetuple())

    return  timestamp
	
def count_days(date):
	'''
			���㵱ǰʱ��������ṩʱ��֮�������
		��Σ�date �磬'2012-02-06 16:10:16'
		���Σ�days �������
		��д��liulk
		ʱ�䣺2012-06-21 15:33:42
	'''
	seconds_in_oneday = 86400  #24 * 60 * 60
	oldstamp = date2timestamp(date)
	newstamp = time.time()
	days = int( (newstamp - oldstamp) / seconds_in_oneday )
	return days
	
class Timer:
    def __init__(self, ID=""):
        self._beginTime = datetime.datetime.now()
        self._ID = ID

    def taketimes(self):
        # �����Ѿ���ʱ
        _tmp = datetime.datetime.now() - self._beginTime
        _timeDiff =  _tmp.seconds*1000000 + _tmp.microseconds
        return _timeDiff/1000


    def __del__(self):
        _tmp = datetime.datetime.now() - self._beginTime
        _timeDiff =  _tmp.seconds*1000000 + _tmp.microseconds
        logging.info( "event:[%s] cost:[%fs]", self._ID, float(_timeDiff)/1000000 )
