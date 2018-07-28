#!/usr/bin/python
#-*- coding: UTF-8 -*-
#文件名：server.py

import socket			# 导入 socket 模块

s = socket.socket()		# 创建 socket 对象
host = socket.gethostname()	# 获取本地主机名
host = '127.0.0.1'
port = 12346			# 设置端口
s.bind((host, port))		# 绑定端口

s.listen(5)			# 等待客户端连接
while True:
	c, addr = s.accept()	# 建立客户端连接
	print(c.recv(1024))
	res = '''
		HTTP/1.1 200 OK

		<html lang='zh-CN'>
		<head>
		<meta charset="utf-8">
		</head>
		=============>
		欢迎访问菜鸟教程
		hello world!
		=============>
		</html>
	'''
	c.sendall(res)
	# c.send('HTTP/1.1 200 OK 欢迎访问菜鸟教程！')
	c.close()		# 关闭连接
