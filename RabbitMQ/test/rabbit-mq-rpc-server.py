#coding:utf-8

import pika

class RpcServer:

	def __init__(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		channel = connection.channel()
		queue_name = 'rpc_queue'
		channel.queue_declare(queue=queue_name)
		print('RpcServer waiting for messages!')
		channel.basic_consume(self.response, queue=queue_name, no_ack=True)
		channel.start_consuming()	

	def fabonacci(self, num):
		num = int(num)
		if num==0:
			return 1
		if num==1:
			return 1
		return self.fabonacci(num-1)+self.fabonacci(num-2)	

	def response(self, ch, method, properties, body):
		num = int(body)
		print(num)
		result = self.fabonacci(num)
		print(result)

		conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		channel = conn.channel()
		#channel = ch
		channel.basic_publish(exchange='',routing_key='rpc_callback_queue',body=str(result),properties=pika.BasicProperties(
	correlation_id = properties.correlation_id
))		
		conn.close()

if __name__=='__main__':
	rpc_server = RpcServer()
	
