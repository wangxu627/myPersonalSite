
---
title: scrapy中向spider传入一个到多个参数
date: 2019-07-03 23:39:28.278810
Description: ""
Tags: []
Categories: []
DisableComments: false
---
如果希望spider定向爬取，就需要给spider传入参数  
  
首先在spider类中定义初始化函数  
  

    
    
    def __init__(self, start_urls=None, number=5, *args, **kwargs):  
        super(DouBanMovieSituationSpider, self).__init__(*args, **kwargs)  
        self.start_urls = start_urls  
        self.number = int(commentNum)
    

  

调用时使用  
  

    
    
    scrapy crawl xxxSpider -a start_urls=xxxxxx -a number=number

  
想传多少个参数，就在参数前加多少个 -a……  
  
有同学是使用pycharm里面的调用python语句来模拟执行cmd的，则将python语句改为“  
  

    
    
    from scrapy.cmdline import execute  
    execute(['scrapy', 'crawl', 'xxxSpider',"-a","start_urls=xxxx","-a","number=666"])

  

\---------------------  
原文：https://blog.csdn.net/c0411034/article/details/81750028  
版权声明：本文为博主原创文章，转载请附上博文链接！


