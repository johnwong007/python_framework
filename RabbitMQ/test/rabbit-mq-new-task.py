#coding:utf-8

import sys
import pika

msg = ' '.join(sys.argv[1:]) or 'hello, world'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

queue_name = 'task_queue'
channel.queue_declare(queue_name, durable=True)

channel.basic_publish(
		exchange='',
		routing_key=queue_name,
		body=msg,
		properties=pika.BasicProperties(
		    delivery_mode = 2,
		))

print("[x] Sent %r"%(msg))
connection.close()
