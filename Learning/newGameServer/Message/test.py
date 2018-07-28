#coding=gbk
''' 消息模块 '''
import dispatcher
import time
import JsonUtil as json

message_write  = dispatcher.Dispatcher()
message_write.init( ( 'FUCK', 'FUCK001' ), '', 'amqp://192.168.0.252:5672/' , 'read')
num = 10000

st_time = time.time()
for i in range(num):
    message_write.send( ('FUCK','FUCK001'), json.write('fuck'), 0 )

en_time = time.time()

print (en_time - st_time)/num 