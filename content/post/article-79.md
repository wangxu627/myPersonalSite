
---
title: unix下用signal+python实现setTimeout和setInterval
date: 2019-11-22 17:44:22.899734
Description: ""
Tags: []
Categories: []
DisableComments: false
---
windows下由于信号是个残废，所以可以考虑使用threading模块，不过此方案回调函数是在子线程中执行，threading.get_ident()返回该调用线程的id

    
    
    import threading  
    import os  
    from functools import wraps  
      
    def delay(delay=0.):  
        """  
        Decorator delaying the execution of a function for a while.  
        """  
        def wrap(f):  
            @wraps(f)  
            def delayed(*args, **kwargs):  
                timer = threading.Timer(delay, f, args=args, kwargs=kwargs)  
                timer.start()  
            return delayed  
        return wrap  
      
    @delay(3.0)  
    def my_func(arg1, arg2):  
        print(threading.get_ident())  
        print(arg1, arg2)

linux下可以用signal实现

    
    
    import os  
    import signal  
      
    def setTimeout(handler, time, *args):  
        def signal_handler(signum, stack):  
            handler(*args)  
        signal.signal(signal.SIGALRM, signal_handler)  
        signal.alarm(time)  
      
    def setInterval(handler, time, *args):  
        def signal_handler(signum, stack):  
            handler(*args)  
            signal.alarm(time)  
        signal.signal(signal.SIGALRM, signal_handler)  
        signal.alarm(time)  
      
      
    ''' test code '''  
    import time  
    def call_me(x, y):  
        print(x, y)  
    setTimeout(call_me, 2, 5, 5)  
    setInterval(call_me, 2, 1, 2)  
    while(1):  
        time.sleep(5)

不过此方案有至少2个缺陷没有进行处理

1.如果之前已经设置了alarm，需要在setTimeout和setInterval中进行恢复（如果之前设置的alarm在setTimeout超时时间以内，会提前触发）

2.setTimeout和setInterval无法重叠调用（因问题1引起）

  

另外相对更好的解决方案是结合前面两种方案，在子线程中发送signal.SIGUSR1信号，实验结果说明此方案可行，不过也仅限于unix系统

  


