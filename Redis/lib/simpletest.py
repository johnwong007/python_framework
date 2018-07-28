import Redisconn

rc = Redisconn.Redisconn.getInstance()

print(rc.get('foo'))
