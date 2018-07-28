#coding:utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

exchange_test = 'exchange_test'
queue_test1 = 'queue_test3'
queue_test2 = 'queue_test2'

#channel.queue_declare(queue=queue_test1, durable=True)
#channel.queue_declare(queue=queue_test2, durable=True)

channel.basic_publish(exchange='', routing_key=queue_test1, body='hello, world!',properties=pika.BasicProperties(delivery_mode=2))
channel.basic_publish(exchange='', routing_key=queue_test2, body='hello, world!',properties=pika.BasicProperties(delivery_mode=2))
print('[x] Sent hello world!')



