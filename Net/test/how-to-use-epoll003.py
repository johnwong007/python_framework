#coding:utf-8
import socket, select
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)
serversocket.setblocking(0)

epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)
print('serving on 8080')
try:
    connections = {}; requests = {}; responses = {}
    while True:
        event = epoll.poll(1)
        for fileno, event in event:
            if fileno == serversocket.fileno():
                connection, address = serversocket.accept()
                connection.setblocking(0)
                epoll.register(connection.fileno(), select.EPOLLIN)
                connections[connection.fileno()] = connection
                requests[connection.fileno()] = b''
                responses[connection.fileno()] = response
            elif event & select.EPOLLIN:
                requests[fileno] += connections[fileno].recv(1024)
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    epoll.modify(fileno, select.EPOLLOUT)
                    print(requests[fileno].decode())
            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno])==0:
                    epoll.modify(fileno, 0)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()


'''
采用epoll的程序一般这样操作:
建立一个epoll对象
告诉epoll对象, 对于一些socket监控一些事件.
问epoll, 从上次查询以来什么socket产生了什么事件.
针对这些socket做特定操作.
告诉epoll, 修改监控socket和/或监控事件.
重复第3步到第5步, 直到结束.
销毁epoll对象.
采用异步socket的时候第3步重复了第2步的事情. 这里的程序更复杂, 因为一个线程需要和多个客户端交互.
行 1: select模块带有epoll功能
行 13: 因为socket默认是阻塞的, 我们需要设置成非阻塞(异步)模式.
行 15: 建立一个epoll对象.
行 16: 注册服务器socket, 监听读取事件. 服务器socket接收一个连接的时候, 产生一个读取事件.
行 19: connections表映射文件描述符(file descriptors, 整型)到对应的网络连接对象上面.
行 21: epoll对象查询一下是否有感兴趣的事件发生, 参数1说明我们最多等待1秒的时间. 如果有对应事件发生, 立刻会返回一个事件列表.
行 22: 返回的events是一个(fileno, event code)tuple列表. fileno是文件描述符, 是一个整型数.
行 23: 如果是服务器socket的事件, 那么需要针对新的连接建立一个socket.
行 25: 设置socket为非阻塞模式.
行 26: 注册socket的read(EPOLLIN)事件.
行 31: 如果读取事件发生, 从客户端读取新数据.
行 33: 一旦完整的http请求接收到, 取消注册读取事件, 注册写入事件(EPOLLOUT), 写入事件在能够发送数据回客户端的时候产生.
行 34: 打印完整的http请求, 展示即使通讯是交错的, 数据本身是作为一个完整的信息组合和处理的.
行 35: 如果写入事件发生在一个客户端socket上面, 我们就可以发送新数据到客户端了.
行s 36-38: 一次发送一部分返回数据, 直到所有数据都交给操作系统的发送队列.
行 39: 一旦所有的返回数据都发送完, 取消监听读取和写入事件.
行 40: 如果连接被明确关闭掉, 这一步是可选的. 这个例子采用这个方法是为了让客户端首先断开, 告诉客户端没有数据需要发送和接收了, 然后让客户端断开连接.
行 41: HUP(hang-up)事件表示客户端断开了连接(比如 closed), 所以服务器这端也会断开. 不需要注册HUP事件, 因为它们都会标示到注册在epoll的socket.
行 42: 取消注册.
行 43: 断开连接.
行s 18-45: 在这里的异常捕捉的作用是, 我们的例子总是采用键盘中断来停止程序执行.
行s 46-48: 虽然开启的socket不需要手动关闭, 程序退出的时候会自动关闭, 明确写出来这样的代码, 是更好的编码风格.
'''
