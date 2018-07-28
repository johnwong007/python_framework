#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket

class UdpServer(object):
	def tcpServer(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.bind(('127.0.0.1', 54321))
		
		while True:
			recvData, (remoteHost, remotePort) = sock.recvfrom(1024)
			print("%s:%s connect"%(remoteHost, remotePort))			# 接收客户端的ip，port

			sendDataLen = sock.sendto('this is send data from server.', (remoteHost, remotePort))
			print('recvData:', recvData)
			print('sendDataLen:', sendDataLen)
		sock.close()

if __name__ == '__main__':
	udpServer = UdpServer()
	udpServer.tcpServer()






