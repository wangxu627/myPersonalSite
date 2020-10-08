
---
title: Python中iter的惯用法
date: 2019-11-05 02:27:06.654632
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    # prototype
    # def iter(__function: Callable[[], _T], __sentinel: _T) -> Iterator[_T]: ...  
    
    g = 1  
    def f():  
        global g  
        r = g if g < 10 else 0  
        g += 1  
        return r  
      
    for i in iter(lambda : f(), 0):  
        print(i)

iter第一个参数是callable，会一直调用，直到结果与第二个参数一样，则终止

可以用于读取文件

    
    
    from functools import partial  
    with open('mydata.db', 'rb') as f:  
        for block in iter(partial(f.read, 64), b''):  
        process_block(block)

  


