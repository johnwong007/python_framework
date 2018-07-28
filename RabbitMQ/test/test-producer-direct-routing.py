#coding:utf-8

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

logtype = sys.argv[1] if len(sys.argv)>1 else 'info'

channel.exchange_declare(exchange='direct_logs', type='direct')

channel.basic_publish(exchange='direct_logs',routing_key=logtype,body='message type is '+logtype)

print('message type is '+logtype)

connection.close()






