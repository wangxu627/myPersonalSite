
---
title: Scrapy利用多进程启动spider分段处理任务
date: 2019-07-04 01:39:04.414568
Description: ""
Tags: []
Categories: []
DisableComments: false
---
_run.py(launcher)

    
    
    from scrapy.cmdline import execute  
    from multiprocessing import Process  
    import os  
    import time  
      
    def run_proc(part):  
        execute(['scrapy', 'runspider', 'spiders/test.py',"-a","part=" + str(part)])  
        print('Run child process %s (%s)...' % (part, os.getpid()))  
      
    if __name__=='__main__':  
        print('Parent process %s.' % os.getpid())  
        processes = list()  
        for i in range(5):  
            p = Process(target=run_proc, args=(i + 1,))  
            print('Process will start.')  
            p.start()  
            processes.append(p)  
          
        for p in processes:  
            p.join()  
        print('Process end.')

  

test.py(spider)

    
    
    # -*- coding: utf-8 -*-  
    import scrapy  
    import random  
    import math  
      
    # count = math.floor(random.random() * 10000 + random.random() * 500)  
    count = 45243  
      
    class TestSpider(scrapy.Spider):  
        name = 'test'  
        allowed_domains = ['baidu.com']  
        start_urls = ['http://www.baidu.com/']  
      
      
        def __init__(self, part, total = 5, *args, **kwargs):  
            self.part = int(part)  
            self.total = int(total)  
      
            part_cnt = math.ceil(count / self.total)  
            start_index = (self.part - 1) * part_cnt  
            end_index = min(self.part * part_cnt, count) - 1  
      
            print(self.part, start_index, "----------------", end_index, count)  
              
        def parse(self, response):  
            pass

  


