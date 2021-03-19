
---
title: python的os.system函数
date: 2019-07-28 15:31:42.750633
Description: ""
Tags: []
Categories: []
DisableComments: false
---
1.阻塞模式

os.system产生的是新进程，会和父进程有不同的pid

run.py

    
    
    import os  
    print("Parent Id : ", os.getpid())  
    os.system("python start.py")  
    print("End")

start.py

    
    
    import time  
    import os  
      
    for i in range(10):  
        print("Child Pid : ", os.getpid())  
        time.sleep(1)

执行结果：

    
    
    D:\pyToolsCollection\os-system>python run.py  
    Parent Id :  17868  
    Child Pid :  31144  
    Child Pid :  31144  
    Child Pid :  31144  
    Child Pid :  31144  
    Child Pid :  31144  
    Child Pid :  31144  
    Child Pid :  31144  
    Child Pid :  31144  
    Child Pid :  31144  
    Child Pid :  31144  
    End

可以看到两个pid是不同的，但是父进程会阻塞一直到子进程结束，且两个进程公用的同一个控制台输出

2.非阻塞模式

修改后的run.py  

    
    
    import os  
    print("Parent Id : ", os.getpid())  
    os.system("start python start.py")  
    print("End")

在实际命令钱增加了一个start

执行结果：

    
    
    D:\pyToolsCollection\os-system>python run.py  
    Parent Id :  8448  
    End

结果是(父进程?)立即结束，子进程单独新开控制台执行，当然这种情况pid也肯定是不同的

PS：其实在第二种情况中，run.py所在的进程已经不是start.py进程的父进程了，可通过os.getppid()查看，两者并没有关联，这也是第二种情况会有一个新控制台的原因

  

  

  


