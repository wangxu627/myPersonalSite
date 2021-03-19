
---
title: iso c/python中和时间相关的函数
date: 2019-11-18 04:10:06.633707
Description: ""
Tags: []
Categories: []
DisableComments: false
---
![](http://image.wxioi.com/c9ed2cd579f2d415895c7acd2a4cf763.jpg)  

一些计时函数：

time.perf_counter，自动选择最精确的计时器，墙上时间

time.process_time，cpu时间，内核和用户cpu时间之和

time.clock,进程启动或第一次调用clock之后的cpu时间

    
    
    import time  
      
    a1=time.perf_counter()  
    a2=time.process_time()  
    a3 = time.clock()  
    c=1  
    for i in range(1,200000):  
        c*=i  
    time.sleep(10)  
      
    b1=time.perf_counter()  
    b2=time.process_time()  
    b3=time.clock()  
    print(b1-a1,'s')  
    print(b2-a2,'s')  
    print(b3-a3,'s')  
      
    #21.109709750002366 s  
    #11.088861482000002 s  
    #11.088497 s

 格式|  说明| 实例  
---|---|---  
 %a|  缩写的周日名|  Tue  
 %A|  全周日名|  Tuesday  
 %b|  缩写的月名|  Feb  
 %B|  全月名|  February  
 %c|  日期和时间|  Tue Feb 10 18:27:38 2004  
 %C|  年/100：[00-99] |  20  
 %d|  月日:[01-31]|  10  
 %D|  日期[MM/DD/YY]|  02/10/04  
 %e|  月日:[ 1-31]|  10  
 %F|  ISO8601日期格式[YYYY-MM-DD]|  2004-02-10  
 %g|  ISO8601基于周的年的最后2位数[00-99]|  04  
 %G|  ISO8601基于周的年|  2004  
 %h|  于%b相同|  Feb  
 %H|  小时（24小时制）[00-23]|  18  
 %I|  小时（12小时制）[01-12]|  06  
 %j|  年日[001-366]|  041  
 %m|  月[01-12]|  02  
 %M|  分[00-59]|  27  
 %n|  换行符|  
 %p|  AM/PM|  PM  
 %r|  本地时间（12小时制）|  06:27:38 PM  
 %R|  于“%H:%M”相同|  18:27  
 %S|  秒[00-60]|  38  
 %t|  水平制表符|  
 %T|  于“%H:%M:%S”相同|  18:27:38  
 %u|  ISO8601基于周数[Monday=1,1-7]|  2  
 %U|  星期日的周数[00-53]|  06  
 %V|  ISO8601的周数[01-53]|  07  
 %w|  周日[0=Sumday, 06]|  2  
 %W|  星期一的周数[00-53]|  06  
 %x|  日期|  02/10/04  
 %X|  时间|  18:27:38  
 %y|  年的最后两位[00-99]|  04  
 %Y|  年 |  2004  
 %z|  ISO8601格式的UTC偏移量|  -0500  
 %Z|  时区名|  EST  
 %%|  转换位一个%|  %  
  
  


