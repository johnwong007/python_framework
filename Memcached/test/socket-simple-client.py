#!/usr/bin/python
#coding:utf-8
# 文件名：client.py

import socket				# 导入 socket 模块

s = socket.socket()			# 创建 socket 对象
host = socket.gethostname()		# 获取本机主机名
port = 12346				# 设置端口号

s.connect((host, port))
s.send('你好，菜鸟')
print(s.recv(1024))
s.close()

