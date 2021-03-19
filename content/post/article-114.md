
---
title: Python之asyncio并发运行多个task
date: 2020-02-11 15:49:46.835356
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    import asyncio  
      
    async def f1():  
        print("f1 start")  
        await asyncio.sleep(1)  
        print("f1 end")  
          
    async def f2():  
        print("f2 start")  
        await asyncio.sleep(2)  
        print("f2 end")  
          
    loop = asyncio.get_event_loop()  
    t1 = loop.create_task(f1())  
    t2 = loop.create_task(f2())  
    loop.run_until_complete(asyncio.gather(t1, t2))

  


