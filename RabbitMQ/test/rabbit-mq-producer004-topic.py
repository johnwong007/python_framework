#coding:utf-8

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', type='topic')

key = sys.argv[1] if len(sys.argv)>1 else ''
msg = sys.argv[2] if len(sys.argv)>2 else 'hello, world!'

channel.basic_publish(
	exchange='topic_logs',
	routing_key=key,		
	body=msg
)

connection.close()

