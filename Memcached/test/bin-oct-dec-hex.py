#coding:utf-8
'''
	十进制:decimal 八进制:octonary 十六进制:hexadecimal 二进制:binary.
'''
CONFIG = {
	'0'		:		'dec2bin',
	'1'		:		'dec2oct',
	'2'		:		'dec2hex',
	'3'		:		'bin2oct',
	'4'		:		'bin2dec',
	'5'		:		'bin2hex',
	'6'		:		'oct2bin',
	'7'		:		'oct2dec',
	'8'		:		'oct2hex',
	'9'		:		'hex2bin',
	'10'		:		'hex2oct',
	'11'		:		'hex2dec',
}

print('0)十进制转2进制')
print('1)十进制转8进制')
print('2)十进制转16进制')
print('3)2进制转8进制')
print('4)2进制转10进制')
print('5)2进制转16进制')

print('6)8进制转2进制')
print('7)8进制转10进制')
print('8)8进制转16进制')
print('9)16进制转2进制')
print('10)16进制转8进制')
print('11)16进制转10进制')
num = input('选择想要转换的函数:')

hex_letter = ['A', 'B', 'C', 'D', 'E', 'F']

def defaultfunc(origin_num):
	print('this is the default func!')

def _other2dec(origin_num, digit, rmflag):
	origin_num = str(origin_num)
	start = 0
	for i in range(0,len(rmflag)):
		flag = rmflag[i]
		tmp = origin_num.find(flag)
		if tmp!=-1:
			start = tmp+len(flag)
	origin_num = origin_num[start:]
	res = 0
	for i in range(0, len(origin_num)):
		tmp = origin_num[i]
		if tmp in hex_letter:
			res = (res<<digit)+ord(tmp)-ord(hex_letter[0])+10
		else:	
			res = (res<<digit)+int(origin_num[i])	
	return str(res)

def _dec2other(origin_num, digit, preflag):
	origin_num = int(origin_num)
	res = ''
	while(True):
		tmp = origin_num%(1<<digit)
		if tmp<10:
			res = str(tmp) + res
		else:
			res = str(hex_letter[tmp-10]) + res
		origin_num = origin_num>>digit
		if origin_num<=(1<<digit)-1:
			if origin_num<10:
				res = preflag + str(origin_num) + res
			else:
				res = preflag + str(hex_letter[(origin_num-10)]) + res
			break
	return res
		

def dec2bin(origin_num):
	return _dec2other(origin_num, 1, '0B')

def dec2oct(origin_num):
	return _dec2other(origin_num, 3, '0O')

def dec2hex(origin_num):
	return _dec2other(origin_num, 4, '0X')

def _bin2oct_hex(origin_num, digit, preflag):	
	origin_num = str(origin_num)
	start = 0
	tmp = origin_num.find('0b')
	if tmp!=-1:
		start = tmp+2
	tmp = origin_num.find('0B')
	if tmp!=-1:
		start = tmp+2
	origin_num = origin_num[start:]
	res = ''
	forend = len(origin_num)%digit
	for i in range(len(origin_num)-1,forend,-digit):
		value = 0
		for j in range(0,digit):
			value = value+(int(origin_num[i-j])<<j)
		if value<10:
			res = str(value)+res
		else:
			res = str(hex_letter[value-10])+res
	
	value = 0	
	for i in range(1,digit+1):
		if forend-i>=0:
			value = value+(int(origin_num[forend-i])<<(i-1))
	if value>0:
		if value<10:
			res = preflag+str(value)+res
		else:
			res = preflag+str(hex_letter[value-10])+res
	else:
		res = preflag+res
	return res

def bin2oct(origin_num):
	return _bin2oct_hex(origin_num, 3, '0O')

def bin2dec(origin_num):
	return _other2dec(origin_num, 1, ('0b','0B',))

def bin2hex(origin_num):
	return _bin2oct_hex(origin_num, 4, '0x')

def oct2bin(origin_num):
	origin_num = str(origin_num)
	start = 0
	tmp = origin_num.find('0O')
	if tmp!=-1:	
		start = tmp+2
	tmp = origin_num.find('0o')
	if tmp!=1:
		start = tmp+2
	origin_num = origin_num[start:]
	res = ''
	for i in range(0, len(origin_num)):
		tmp = _dec2other(int(origin_num[i]), 1, '')
		tmp = int(tmp)
		res = '%s%03d'%(res, tmp)
	return '0B'+res

def oct2dec(origin_num):
	return _other2dec(origin_num, 3, ('0o','0O',))

def oct2hex(origin_num):
	#origin_num = oct2bin(origin_num)
	#return bin2hex(origin_num)	
	origin_num = oct2dec(origin_num)	
	return dec2hex(origin_num)
	
def hex2bin(origin_num):
	origin_num = str(origin_num)
	start = 0
	tmp = origin_num.find('0x')
	if tmp!=-1:
		start = tmp+2
	tmp = origin_num.find('0X')
	if tmp!=-1:
		start = tmp+2
	origin_num = origin_num[start:]
	res = ''
	for i in range(0, len(origin_num)):
		tmp = origin_num[i]
		if tmp in hex_letter:
			tmp = ord(tmp)-ord(hex_letter[0])+10
		tmp = int(_dec2other(str(tmp), 1, ''))
		res = '%s%04d'%(res, tmp)
	return '0B'+res

def hex2dec(origin_num):
	return _other2dec(origin_num, 4, ('0x','0X',))

def hex2oct(origin_num):
	#origin_num = hex2bin(origin_num)
	#return bin2oct(origin_num)
	origin_num = hex2dec(origin_num)
	return _dec2other(origin_num, 3, '0O')
RUN_MAP = {
	'dec2bin'		:		dec2bin,
	'dec2oct'		:		dec2oct,
	'dec2hex'		:		dec2hex,
	'bin2oct'		:		bin2oct,
	'bin2dec'		:		bin2dec,
	'bin2hex'		:		bin2hex,
	'oct2bin'		:		oct2bin,
	'oct2dec'		:		oct2dec,
	'oct2hex'		:		oct2hex,
	'hex2bin'		:		hex2bin,
	'hex2oct'		:		hex2oct,
	'hex2dec'		:		hex2dec,
	'defaultfunc'		:		defaultfunc,
}

try:
	funckey = CONFIG.get(str(num), 'defaultfunc')
	if not funckey:
		funckey = 'defaultfunc'
	func = RUN_MAP.get(funckey, defaultfunc)
	if not func:
		func = defaultfunc
	origin_num = raw_input('输入你想转换的原数据：')
	retval = func(origin_num)
	print(retval)
except:
	print('except!!!!!')

print('==============> end')
