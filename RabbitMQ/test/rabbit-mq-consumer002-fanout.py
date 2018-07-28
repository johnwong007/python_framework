#coding:utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare('log', 'fanout')

result = channel.queue_declare(exclusive=True)
queue_name=result.method.queue

channel.queue_bind(queue=queue_name,exchange='log',routing_key='')
#channel.queue_bind(queue=queue_name,exchange='log',routing_key=queue_name)

print('Waiting for messages')

def callback(ch, method, properties, body):
	print('Received %r'%(body))

channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()
