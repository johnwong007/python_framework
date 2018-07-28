#coding:utf-8

import pika
import sys

class RpcClient:
	num = 0
	wait_msg = True
	def __init__(self):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		self.channel = self.connection.channel()
		queue_name = 'rpc_callback_queue'
		self.channel.queue_declare(queue=queue_name)		
		self.channel.basic_consume(self.response,queue=queue_name,no_ack=True)

	def response(self, ch, method, properties, body):
		print(properties.correlation_id)
		print('Fibonacci %d result is %r'%(self.num, body))
		#sys.exit(0)
		self.wait_msg = False
	
	def call(self, num):
		self.num = num
		self.corr_id = 'rpc_callback_queue'
		conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		channel = conn.channel()
		queue_name = 'rpc_queue'
		channel.basic_publish(
			exchange='',
			routing_key=queue_name,
			body=str(num),
			properties=pika.BasicProperties(
				reply_to = 'rpc_callback_queue',					correlation_id = self.corr_id
			)
		)
		print('Sending %d'%(num))
		conn.close()
		
		while self.wait_msg:
			self.connection.process_data_events()		
		#self.channel.start_consuming()

if __name__=='__main__':
	if len(sys.argv)!=2:
		print('Usage:python %s [number]'%(sys.argv[0]))
		sys.exit(1)
	try:
		num = int(sys.argv[1])
	except:	
		print('Usage:python %s [number]'%(sys.argv[0]))
	
	rpc_client = RpcClient()
	rpc_client.call(num)
	
	sys.exit(0)




