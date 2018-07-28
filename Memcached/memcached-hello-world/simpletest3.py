#coding:utf-8

import memcache
import time

mc = memcache.Client(['127.0.0.1:11211'], debug=0, cache_cas=True)

mc.set('key', 'value', 20, 600)
print(mc.get('key'))
mc.append('key', 'after')
print(mc.get('key'))
mc.prepend('key', 'before')
print(mc.get('key'))

#mc.set('product_count', '900', 20, 600)
v = mc.gets('product_count')
print(mc.cas_ids)
time.sleep(15)
# 类似事物，保证数据的准确性。
# 如果有人在gets之后和cas之前修改了product_count，那么，下面的设置将会执行失败，剖出异常，从而避免非正常数据的产生。
print(mc.cas('product_count', "899"))

print(mc.get('product_count'))
print(mc.cas_ids)
