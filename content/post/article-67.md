
---
title: Python select IO多路复用
date: 2019-11-12 18:36:57.887566
Description: ""
Tags: []
Categories: []
DisableComments: false
---
## 一、select介绍

Python的 **select()**
函数是底层操作系统实现的直接接口。它监视套接字，打开文件和管道（任何带有返回有效文件描述符的`fileno（）`方法），直到它们变得可读或可写，或者发生通信错误。
**select()** 使得更容易同时监视多个连接，并且比使用套接字超时在Python中编写轮询循环更有效，因为监视发生在操作系统网络层而不是解释器。



## 二、使用select编写SocketServer

接下来通过socket server例子要以了解select 是如何通过单进程实现同时处理多个非阻塞的socket连接的

#### 首先我们建立一个服务器端socket

    
    
    import select
    import socket
    import sys
    from queue import Queue
    import queue
    
    
    # 创建套接字
    server = socket.socket()
    server.setblocking(False)
    server.bind(('localhost',8800))
    # 监听传入的连接
    server.listen(5)

**select()**
的参数是三个包含要监视的通信通道的列表。第一个是要检查要读取的传入数据的对象列表，第二个包含在缓冲区中有空间时将接收传出数据的对象，第三个包含可能有错误的对象（通常是错误的组合输入和输出通道对象）。服务器的下一步是设置包含要传递给
**select()** 输入源和输出目标的列表。

    
    
    input = [server] 
    output = [] 
    select.select(input,output,input)

所有客户端的进来的连接和数据将会被server的主循环程序放在上面的list中处理，我们现在的server端需要等待连接可写（writable)之后才能过来，然后接收数据并返回(因此不是在接收到数据之后就立刻返回)，因为每个连接要把输入或输出的数据先缓存到queue里，然后再由select取出来再发出去。

    
    
    # 对外发送数据的队列，记录到字典中
    message_queues = {}

服务器程序的主要部分循环，调用 **select** **`()`** 来阻止并等待网络活动。

    
    
    while 1:
        #等待至少一个套接字准备好处理
        print(sys.stderr, '\nwaiting for the next event')
        """
        readable中的socket连接代表有数据可接受，可读取
        writable list中存放着你可以对其进行发送(send)操作
        exceptional 当连接通信出现error时会把error写到exceptional列表中
        """
        readable, writable, exceptional = select.select(input, output, input)

  

    
    
      
    readable列表中的socket可能会有3种可能状态，  
        1. 如果这个socket是server(它负责监听客户端的连接)，那就表示server端已经收到一个新的连接  
        2. 客户端把数据发送过来了  
        3. 客户端和服务器端断开了连接，将客户端对象从 列表和队列中删除

  

    
    
        for s in readable:
            if s is server: # 第1种情况，表示有新的连接进来
                connection,add = s.accept() # 接受新的连接
                connection.setblocking(0)
    
                """
                这个时候，为了不阻塞整个程序的运行，我们先将它放入input列表中。
                下一次loop时，就会被select去监听，如果这个连接的客户端发来了数据
                那么这个连接的fd在server端就会变成就绪的，select就会把这个连接返回到readable列表中
                然后在 for s in readable中取出这个连接，开始接受数据
                """
                input.append(connection)
                message_queue[connection] = Queue()
    
            else: # 第2种情况就是，客户端把数据发送了过来
                data = s.recv(1024) # 通过recv去接受数据
                if data:
                    print(sys.stderr, 'received "%s" from %s' % (data, s.getpeername()))
                    message_queue[s].put(data) # 接受到的数据先放到队列中
                    if s not in output:
                        output.append(s) # 为了不影响处理与其他客户端的连接，这里不立刻返回数据给客户端
                else: # 第3种情况 就是客户端断开了连接，这个时候recv()数据就是空，这个时候就可以跟客户端断开连接
                    if s in output:
                        """
                        既然断开了连接，就没有必要给客户端发送数据了
                        如果客户端连接对象还在output中，就把他删除
                        """
                        output.remove(s)
                    input.remove(s) # 在input列表中也删除掉
                    # 关闭连接，在队列中也删除
                    s.close()
                    del message_queue[s]

  

对于writable
list中的socket，也有几种状态，如果这个客户端连接在跟它对应的queue里有数据，就把这个数据取出来再发回给这个客户端，否则就把这个连接从output
list中移除，这样下一次循环select()调用时检测到outputs list中没有这个连接，那就会认为这个连接还处于非活动状态

  

    
    
        for s in writable:
            try:
                next_msg = message_queue[s].get_nowait()
            except queue.Empty as e:
                output.remove(s)
            else:
                s.send(next_msg)

  

最后，exceptional
有异常产生。如果在跟某个socket连接通信过程中出了错误，就把这个连接对象在inputs\outputs\message_queue中都删除，再把连接关闭掉

## 三、完整代码

server端：

    
    
    # 通过非阻塞io实现http请求
    # select + 回调 + 事件循环
    
    # 使用单线程完成高并发
    
    import select
    import socket
    import sys
    from queue import Queue
    import queue
    
    
    # 创建套接字
    server = socket.socket()
    server.setblocking(False)
    server.bind(('localhost',8800))
    # 监听传入的连接
    server.listen(5)
    
    """
    第一个是要检查要读取的传入数据的对象列表，
    第二个包含在缓冲区中有空间时将接收传出数据的对象，
    第三个包含可能有错误的对象（通常是错误的组合输入和输出通道对象）。
    """
    input = [server] # 从中读取数据
    output = [] # 将数据发送出去
    select.select(input,output,input)
    
    message_queue = {} # 消息队列
    
    while input:
        #等待至少一个套接字准备好处理
        print(sys.stderr, '\nwaiting for the next event')
        """
        readable中的socket连接代表有数据可接受，可读取
        writable list中存放着你可以对其进行发送(send)操作
        exceptional 当连接通信出现error时会把error写到exceptional列表中
        """
        readable, writable, exceptional = select.select(input, output, input)
    
    
        """
        readable列表中的socket可能会有3种可能状态，
            1. 如果这个socket是server(它负责监听客户端的连接)，那就表示server端已经收到一个新的连接
            2. 客户端把数据发送过来了
            3. 客户端和服务器端断开了连接，将客户端对象从 列表和队列中删除
        """
        for s in readable:
            if s is server: # 第一种情况，表示有新的连接进来
                connection,add = s.accept() # 接受新的连接
                connection.setblocking(0)
    
                """
                这个时候，为了不阻塞整个程序的运行，我们先将它放入input列表中。
                下一次loop时，就会被select去监听，如果这个连接的客户端发来了数据
                那么这个连接的fd在server端就会变成就绪的，select就会把这个连接返回到readable列表中
                然后在 for s in readable中取出这个连接，开始接受数据
                """
                input.append(connection)
                message_queue[connection] = Queue()
    
            else: # 第2种情况就是，客户端把数据发送了过来
                data = s.recv(1024) # 通过recv去接受数据
                if data:
                    print(sys.stderr, 'received "%s" from %s' % (data, s.getpeername()))
                    message_queue[s].put(data) # 接受到的数据先放到队列中
                    if s not in output:
                        output.append(s) # 为了不影响处理与其他客户端的连接，这里不立刻返回数据给客户端
                else: # 第3种情况 就是客户端断开了连接，这个时候recv()数据就是空，这个时候就可以跟客户端断开连接
                    if s in output:
                        """
                        既然断开了连接，就没有必要给客户端发送数据了
                        如果客户端连接对象还在output中，就把他删除
                        """
                        output.remove(s)
                    input.remove(s) # 在input列表中也删除掉
                    # 关闭连接，在队列中也删除
                    s.close()
                    del message_queue[s]
    
    
        """
        writable list也有几种状态，如果客户端连接在跟它对应的queue里有数据时，就把这个数据取出来再发给用户
        否则就把这个连接从output中移除，这样下一次，select调用时检测到output列表中没有这个连接，就会认为这个连接处于非活动状态
        """
        for s in writable:
            try:
                next_msg = message_queue[s].get_nowait()
            except queue.Empty as e:
                output.remove(s)
            else:
                s.send(next_msg)
    
    
        """
        如果跟某个socket连接通信失败出现错误，就把这个连接对象从 各个列表中删除，再关闭连接
        """
        for s in exceptional:
            input.remove(s)
            for s in output:
                output.remove(s)
            s.close()
            del message_queue[s]

  

client端：

    
    
    import socket
    
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost',8800))
    
    while True:
        msg = bytes(input("<<<"),encoding='utf-8')
        client.sendall(msg)
    
        data = client.recv(1024)
    
        print("{}".format(data))


