
---
title: Python poll IO多路复用
date: 2019-11-12 18:39:09.137690
Description: ""
Tags: []
Categories: []
DisableComments: false
---
## 一、poll介绍

poll本质上和select没有区别，只是没有了最大连接数(linux上默认1024个)的限制，原因是它基于链表存储的。

## 二、使用poll编写SocketServer（本博客代码需要在linux下运行）

首先我们建立一个服务器端的socket

    
    
    import select
    import socket
    import sys
    import queue
    from queue import Queue
    
    
    # 创建一个socket连接
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)
    
    # 绑定IP地址和端口号
    server_address = ('localhost', 8800)
    server.bind(server_address)
    print("服务器已启动http://localhost:8800/")
    
    # 监听连接数
    server.listen(5)
    
    # 消息队列 用于记录客户端发来的消息
    message_queues = {}

设置轮询的超时时间

如果不设置timeout，方法将会阻塞直到对应的poll对象有一个事件发生。

    
    
    TIMEOUT = 1000 # 设置为1秒

poll的事件类型

    
    
    POLLIN    Input ready                  有数据读取
    POLLPRI    Priority input ready        有紧急数据读取
    POLLOUT    Able to receive output      准备输出
    POLLERR    Error                       某些错误
    POLLHUP    Channel closed              挂起
    POLLNVAL    Channel not open           无效请求，描述符无法打开  
      
    
    
    
    READ_ONLY = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
    READ_WRITE = READ_ONLY | select.POLLOUT

注册要监听文件描述符

首先需要实例化一个poll对象，对要监听的句柄进行注册

    
    
    poller = select.poll()
    # 注册server端socket  要监听的事件类型为 读
    poller.register(server, READ_ONLY)

文件描述符映射具体的套接字对象

    
    
    """
    由于poll()返回包含套接字文件描述符和事件标志的元组列表，因此需要从文件描述符号到对象的映射才能从套接字中读取或写入该套接字。
    """
    fd_to_socket = { server.fileno(): server,}



事件轮询

    
    
    while True:
    
        """
        去检测已经注册的文件描述符，会返回一个(fd,event)元祖列表
        fd:文件描述符
        event:描述符可能会发生的事件
        如果返回为空的列表，则说明超时且没有文件描述符有事件发生
        """
        events = poller.poll(TIMEOUT) # 如果timeout为None，将会阻塞，知道有事件发生
        for fd, flag in events:
            # 从文件描述符中检索实际的套接字
            s = fd_to_socket[fd]

事件类型判断

    
    
            if flag & (select.POLLIN | select.POLLPRI): # 有数据可以读取
    
                if s is server: # 表示有新的连接
                    # 可以读取数据
                    connection, client_address = s.accept()
                    print(sys.stderr, '新的连接来自:', client_address)
                    connection.setblocking(0)
                    fd_to_socket[connection.fileno()] = connection # 往fd字典中添加一个新的 文件描述符
                    poller.register(connection, READ_ONLY)
    
                    message_queues[connection] = Queue() # 为了防止等待客户端发来数据期间发生阻塞，分配一个队列用于保存数据
                else: # 表示客户端传来了消息
    
                    data = s.recv(1024)
                    if data: # 表明数据接受成功
    
                        print(sys.stderr, '接受数据 "%s" 来自 %s' % (data, s.getpeername()))
                        message_queues[s].put(data)
                        # 修改一个已经存在的fd，修改事件为写。这里表示服务器向客户端要发送数据
                        poller.modify(s, READ_WRITE)
                    else:
                        # 如果没有接受到数据，表示要断开连接
                        print(sys.stderr, '关闭', client_address, '并未读取到数据')
                        # 停止监听连接上的输入
                        poller.unregister(s)
                        s.close()
    
                        # 将此链接从队列中删除
                        del message_queues[s]
    
            elif flag & select.POLLHUP:
                print(sys.stderr, '关闭', client_address, '收到HUP后')
                poller.unregister(s)
                s.close()
    
            elif flag & select.POLLOUT:
                try:
                    next_msg = message_queues[s].get_nowait()
                except queue.Empty:
                    print(sys.stderr, '队列', s.getpeername(), '为空')
                    poller.modify(s, READ_ONLY)
                else:
                    print(sys.stderr, '发送 "%s" 到 %s' % (next_msg, s.getpeername()))
                    s.send(next_msg)
    
            elif flag & select.POLLERR:
                print(sys.stderr, '异常信息:', s.getpeername())
                poller.unregister(s)
                s.close()
                del message_queues[s]

  

## 三、完整代码示例

server端：

    
    
    import select
    import socket
    import sys
    import queue
    from queue import Queue
    
    
    # 创建一个socket连接
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)
    
    # 绑定IP地址和端口号
    server_address = ('localhost', 8800)
    server.bind(server_address)
    print("服务器已启动http://localhost:8800/")
    
    # 监听连接数
    server.listen(5)
    
    # 消息队列
    message_queues = {}
    
    """
    POLLIN    Input ready      有数据读取
    POLLPRI    Priority input ready   有紧急数据读取
    POLLOUT    Able to receive output  准备输出
    POLLERR    Error   某些错误
    POLLHUP    Channel closed   挂起
    POLLNVAL    Channel not open  无效请求，描述符无法打开
    """
    # 常用的标识  代表你想检查的事件类型
    READ_ONLY = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
    READ_WRITE = READ_ONLY | select.POLLOUT
    
    TIMEOUT = 1000
    poller = select.poll() # 创建一个poll对象，该对象可以注册或注销文件描述符
    
    # 注册一个文件描述符，可以通过poll()方法来检查是否有对应的IO事件发生
    # 接受两个参数， fd  和  eventmask
    poller.register(server,READ_ONLY)
    fd_to_socket = { server.fileno(): server,}
    # 服务器的循环调用poll()，然后通过查找套接字并根据事件中的标志采取行动来处理返回的“事件”。
    while True:
    
        """
        去检测已经注册的文件描述符，会返回一个(fd,event)元祖列表
        fd:文件描述符
        event:描述符可能会发生的事件
        如果返回为空的列表，则说明超时且没有文件描述符有事件发生
        """
        events = poller.poll(TIMEOUT) # 如果timeout为None，将会阻塞，知道有事件发生
        for fd, flag in events:
            # 从文件描述符中检索实际的套接字
            s = fd_to_socket[fd]
    
            if flag & (select.POLLIN | select.POLLPRI): # 有数据可以读取
    
                if s is server: # 表示有新的连接
                    # 可以读取数据
                    connection, client_address = s.accept()
                    print(sys.stderr, '新的连接来自:', client_address)
                    connection.setblocking(0)
                    fd_to_socket[connection.fileno()] = connection # 往fd字典中添加一个新的 文件描述符
                    poller.register(connection, READ_ONLY)
    
                    message_queues[connection] = Queue() # 为了防止等待客户端发来数据期间发生阻塞，分配一个队列用于保存数据
                else: # 表示客户端传来了消息
    
                    data = s.recv(1024)
                    if data: # 表明数据接受成功
    
                        print(sys.stderr, '接受数据 "%s" 来自 %s' % (data, s.getpeername()))
                        message_queues[s].put(data)
                        # 修改一个已经存在的fd，修改事件为写。这里表示服务器向客户端要发送数据
                        poller.modify(s, READ_WRITE)
                    else:
                        # 如果没有接受到数据，表示要断开连接
                        print(sys.stderr, '关闭', client_address, '并未读取到数据')
                        # 停止监听连接上的输入
                        poller.unregister(s)
                        s.close()
    
                        # 将此链接从队列中删除
                        del message_queues[s]
    
            elif flag & select.POLLHUP:
                print(sys.stderr, '关闭', client_address, '收到HUP后')
                poller.unregister(s)
                s.close()
    
            elif flag & select.POLLOUT:
                try:
                    next_msg = message_queues[s].get_nowait()
                except queue.Empty:
                    print(sys.stderr, '队列', s.getpeername(), '为空')
                    poller.modify(s, READ_ONLY)
                else:
                    print(sys.stderr, '发送 "%s" 到 %s' % (next_msg, s.getpeername()))
                    s.send(next_msg)
    
            elif flag & select.POLLERR:
                print(sys.stderr, '异常信息:', s.getpeername())
                poller.unregister(s)
                s.close()
                del message_queues[s]

  

client端：

    
    
    import socket
    
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost',8800))
    
    while True:
        msg = bytes(input("<<<"),encoding='utf-8')
        client.sendall(msg)
    
        data = client.recv(1024)
    
        print("{}".format(data))

  


