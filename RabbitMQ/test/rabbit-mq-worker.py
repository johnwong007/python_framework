#coding:utf-8

import pika
import time

def callback(ch, method, properties, body):
	print(' [x] Received %r'%(body,))
	#time.sleep(5)
	print(' [x] Done')
	ch.basic_ack(delivery_tag = method.delivery_tag)
	
connection = pika.BlockingConnection(pika.ConnectionParameters('30.30.32.115'))
#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

queue_name = 'TOPIC_TEST'
#queue_name = 'task_queue'
channel.queue_declare(queue=queue_name, durable=True)
# channel.queue_declare(queue_name)
print(' [*] Waiting for messages!')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,queue=queue_name)

channel.start_consuming()
