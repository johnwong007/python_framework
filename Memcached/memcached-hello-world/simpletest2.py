#coding:utf-8

import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

#mc.set('foo', 'bar', 20, 600)
print(mc.get('foo'))

mc.set_multi({'1':'bar1','2':'bar2'}, 20, 'foo', 600)
print(mc.get('foo1'))

mc.add('foo', 'bar', 10, 600)
print(mc.get('foo'))

mc.replace('foo', 'bar1', 10, 100)
print(mc.get('foo'))

print(mc.get_multi(['foo1','foo2']))

mc.delete('foo2', 0)
print(mc.get('foo2'))

mc.add('foo2', '10', 10, 6)
print(mc.incr('foo2', 1))

print(mc.decr('foo2', 2))
