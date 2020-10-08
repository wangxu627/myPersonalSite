
---
title: Python之for else
date: 2019-08-21 13:33:24.852377
Description: ""
Tags: []
Categories: []
DisableComments: false
---
Effective Python里面有讲到for后面可以接else，不过不建议使用

    
    
    t = 5  
    for i in range(10):  
        if(i == t):  
            break  
    else:  
        print("Executed")  
      
    

如果在for中break了，后面的else不会执行

反之：

    
    
    t = 10  
    for i in range(10):  
        if(i == t):  
            break  
    else:  
        print("Executed")

整个循环完整执行了，则会执行

PS：如果是个空循环，后面的else也会执行

  

Effective Python说这种代码属于奇技淫巧，不推荐使用

不过在看_collections_abc.py代码的时候，发现标准库里还是有使用的

    
    
    def _check_methods(C, *methods):  
        mro = C.__mro__  
        for method in methods:  
            for B in mro:  
                if method in B.__dict__:  
                    if B.__dict__[method] is None:  
                        return NotImplemented  
                    break  
            else:  
                return NotImplemented  
        return True
    
    
    class Sized(metaclass=ABCMeta):  
      
        __slots__ = ()  
      
        @abstractmethod  
        def __len__(self):  
            return 0  
      
        @classmethod  
        def __subclasshook__(cls, C):  
            if cls is Sized:  
                return _check_methods(C, "__len__")  
            return NotImplemented

  

8月23日更新：

今天看了《流畅的python》中对else块的描述之后，发现其实else块还是很有用的，只是else这个关键字在for，while后面不合适，理解成then的话就更恰当一些了


