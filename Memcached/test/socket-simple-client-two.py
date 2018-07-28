#coding:utf-8

import socket

s = socket.socket()
port = 12346
s.connect(('127.0.0.1', port))
s.send('hihi i am client')
data = s.recv(512)
print(data)

sock2 = socket.socket()
host = '127.0.0.1'
sock2.connect((host, port))
sock2.send('client send use sock2')
data2 = sock2.recv(512)
print(data2)
sock2.close()

s.close()
