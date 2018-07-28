#coding:utf-8

import binascii
import random
# help(binascii)
print('binascii主要是用来处理进制之间的转换')

a = 'worker'
b = binascii.b2a_hex(a)
print(b)
print(binascii.a2b_hex(b))

irray = random.choice([['ACCT:GOLD:5000', '5000金币'], ['ACCT:GOLD:5000', '5000金币']])
irray1 = ['金', '币']
print('irray = ')  ;print(irray[1])
print('irray1 = ')  ;print(irray1)
str = '金币'
b=binascii.b2a_hex(str)
print(b)
print(binascii.a2b_hex(b))


print('===========>')
print(hex(88))
