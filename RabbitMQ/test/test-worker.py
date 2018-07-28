#coding:utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

queue_test1 = 'queue_test3'
channel.queue_declare(queue=queue_test1, durable=True)

channel.basic_qos(prefetch_count=1)

print('worker2 Waiting for messages')

def callback(ch, method, properties, body):
	print('[x] Received %r'%(body))
	ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,queue=queue_test1)
channel.start_consuming()

