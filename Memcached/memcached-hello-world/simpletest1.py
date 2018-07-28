#coding:utf-8
import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# set and get 
'''
	set 命令的基本语法格式如下
	set(key, value, exptime=0, min_compress_len=0) 用于设置zlib压缩

'''
ret = mc.set('foo', 'bar')
print(ret)
value = mc.get('foo')
print(value)

# 清空key
mc.set('foo', None)
print(mc.get('foo'))



