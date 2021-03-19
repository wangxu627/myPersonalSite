
---
title: multiprocessing模块之Process
date: 2019-08-28 01:11:35.690301
Description: ""
Tags: []
Categories: []
DisableComments: false
---
用法很简单，和threading模块的Thread差不多

    
    
    from multiprocessing import Process  
    from time import sleep  
      
    def _worker():  
        print("Worker Process")  
        sleep(1)  
        print("End")  
      
    def start():  
        p = Process(target = _worker)  
        p.start()  
        p.join()  
      
    if __name__ == "__main__":  
        start()

但和Thread相比，有一些限制

1.Process的相关代码必须写在if __name__ == "__main__":中

2.不能把_worker函数定义在start内部，否则会报错


