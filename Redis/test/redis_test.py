import sys,os
if not os.environ.has_key('_BASIC_PATH_'):
	print('============>11111')
	_BASIC_PATH_ = os.path.abspath(__file__)
	_BASIC_PATH_ = _BASIC_PATH_[:_BASIC_PATH_.rfind('/test/')]
	os.environ['_BASIC_PATH_'] = _BASIC_PATH_

if sys.path.count(os.environ['_BASIC_PATH_']+'/lib') == 0:
	print('=============>22222')
	sys.path.append(os.environ['_BASIC_PATH_']+'/lib')
	sys.path.append(os.environ['_BASIC_PATH_']+'/mod')
	sys.path.append(os.environ['_BASIC_PATH_'])
import Redisconn
rc = Redisconn.Redisconn.getInstance()
print(rc.get('foo'))
