#coding=utf-8

import time
import datetime
import zlog as logging

# 时间戳到日期的转换
def timestamp2date( stamp ):
    ltime=time.localtime( stamp )
    timeStr=time.strftime("%Y-%m-%d %H:%M:%S", ltime)

    return timeStr

# 日期到时间戳的转换
def date2timestamp( date ):
    tTmp = time.strptime(date,"%Y-%m-%d %H:%M:%S")
    dateC = datetime.datetime( *tTmp[:6] )
    timestamp=time.mktime(dateC.timetuple())

    return  timestamp
	
def count_days(date):
	'''
			计算当前时间与参数提供时间之间的天数
		入参：date 如，'2012-02-06 16:10:16'
		出参：days 相隔天数
		编写：liulk
		时间：2012-06-21 15:33:42
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
        # 返回已经耗时
        _tmp = datetime.datetime.now() - self._beginTime
        _timeDiff =  _tmp.seconds*1000000 + _tmp.microseconds
        return _timeDiff/1000


    def __del__(self):
        _tmp = datetime.datetime.now() - self._beginTime
        _timeDiff =  _tmp.seconds*1000000 + _tmp.microseconds
        logging.info( "event:[%s] cost:[%fs]", self._ID, float(_timeDiff)/1000000 )
