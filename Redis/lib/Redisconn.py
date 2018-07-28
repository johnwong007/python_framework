#coding:utf-8
import os
import redis
import logging
#logging.basicConfig(filename='./jsinfo.log', level=logging.DEBUG)
try:
	import xml.etree.cElementTree as ET
except:
	import xml.etree.ElementTree as ET
class Redisconn:
	INS = None
	def __init__(self):
		host = None
		port = None
		password = None
		filepath = os.path.abspath(__file__)
		filepath = filepath[:filepath.rfind('/')]
		tree = ET.ElementTree(file=filepath+'/redis.xml')
		root = tree.getroot()
		for item in root.iterfind('redis/conn'):
			config = item.attrib
			host = str(config['host'])
			port = int(config['port'])
			password = str(config['password'])
		if host and port and password:
			self.conn = redis.Redis(host=host, port=port, password=password)
		else:
			logging.error('get config from redis.xml failed')
	
	@staticmethod
	def getInstance():
		if not Redisconn.INS:
			Redisconn.INS = Redisconn()
		return Redisconn.INS.conn		
