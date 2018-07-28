#coding:utf-8

import pika

# 建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 创建channel
channel = connection.channel()

# 创建名字为MATCH001的queue
channel.queue_declare(queue = 'hello')

channel.basic_publish(exchange='',routing_key = 'hello', body = 'hello, world!')
print("[x]Sent 'hello, world!'")
connection.close()
