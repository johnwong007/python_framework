#coding:utf-8

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severity_list = sys.argv[1:] if len(sys.argv)>1 else ['info']

for severity in severity_list:
	print(severity)
	channel.queue_bind(queue=queue_name,
		exchange='direct_logs',
		routing_key=severity	
	)

print('Waiting for messages')

def callback(ch, method, properties, body):
	print(' Received %r'%(body))

channel.basic_consume(callback,
	queue = queue_name,
	no_ack = False,	
)

channel.start_consuming()


