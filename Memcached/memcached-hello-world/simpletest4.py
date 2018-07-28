#coding:utf-8

import memcache
import time

# time.sleep(4)
mc = memcache.Client(['127.0.0.1:11211'], debug=0, cache_cas=True)
mc.set('product_count', '900', 60)
print(mc.get('product_count'))
