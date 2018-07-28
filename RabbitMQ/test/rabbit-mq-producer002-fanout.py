#coding:utf-8

'''
	exchange有三种类型：direct
			topic
			fanout广播模式
'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare('log', 'fanout')


channel.basic_publish(exchange='log',routing_key='',body='这是来自广播的消息')

print('广播消息已发送')
connection.close()

