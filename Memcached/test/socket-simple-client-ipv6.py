#coding:utf-8
import socket
import sys

HOST = '127.0.0.1'
PORT = 50007
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
	af, socktype, proto, canonname, sa = res
	try:
		s = socket.socket(af, socktype, proto)
	except socket.error as msg:
		s = None
		continue
	try:
		s.connect(sa)
	except socket.error as msg:
		s.close()
		s = None
		continue
	break
if s is None:
	print('could not open socket')
	sys.exit(1)
s.sendall('hello, world!')
data = s.recv(1024)
s.close()
print('received:', repr(data))




