#coding:utf-8

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:] if len(sys.argv)>1 else None 
if not binding_keys:
	print('Usage: %s [binding_key]...'%(sys.argv[0]))
	sys.exit(1)

print(binding_keys)
for binding_key in binding_keys:
	channel.queue_bind(queue=queue_name, exchange='topic_logs', routing_key=binding_key)

print('Waiting for message')
def callback(ch, method, properties, body):
	print('Received %r'%(body))
	
channel.basic_consume(callback,queue=queue_name,no_ack=True)

channel.start_consuming()
