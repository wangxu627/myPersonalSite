
---
title: Python描述符入门
date: 2020-02-07 06:02:42.231677
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    class Desc(object):  
        def __get__(self, instance, owner):  
            print("get!!!!")  
            print("self=", self, type(self))  
            print("instance=", instance, type(instance))  
            print("owner=", owner, type(owner))  
            print('*'*50, "\n")  
      
        def __set__(self, instance, value):  
            print("set!!!!")  
            print("self=", self, type(self))  
            print("instance=", instance, type(instance))  
            print("value=", value, type(value))  
            print('*'*50, "\n")  
      
      
    class TestDesc(object):  
        x = Desc()  
      
    t = TestDesc()  
    t.x  
    t.x  = 100  
    m = TestDesc()  
    m.x
    
    

输出如下：  

    
    
    get!!!!  
    self= <__main__.Desc object at 0x7f5b58bbc978> <class '__main__.Desc'>  
    instance= <__main__.TestDesc object at 0x7f5b58bbc9b0> <class '__main__.TestDesc'>  
    owner= <class '__main__.TestDesc'> <class 'type'>  
    **************************************************   
      
    set!!!!  
    self= <__main__.Desc object at 0x7f5b58bbc978> <class '__main__.Desc'>  
    instance= <__main__.TestDesc object at 0x7f5b58bbc9b0> <class '__main__.TestDesc'>  
    value= 100 <class 'int'>  
    **************************************************   
      
    get!!!!  
    self= <__main__.Desc object at 0x7f5b58bbc978> <class '__main__.Desc'>  
    instance= <__main__.TestDesc object at 0x7f5b58bbc9e8> <class '__main__.TestDesc'>  
    owner= <class '__main__.TestDesc'> <class 'type'>  
    **************************************************

结论：

描述符只有一个，所有的get和set方法的self是同一个，但instance可能不同  


