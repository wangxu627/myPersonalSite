
---
title: 使用functools.lru_cache做备忘
date: 2019-10-16 15:14:30.358136
Description: ""
Tags: []
Categories: []
DisableComments: false
---
functools.lru_cache 是非常实用的装饰器，
它实现了备忘（memoization）功能。这是一项优化技术，它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。LRU 三个字母是“Least
Recently Used”的缩写，表明缓存不会无限制增长，一段时间不用的缓存条目会被扔掉。  
生成第 n 个斐波纳契数这种慢速递归函数适合使用 lru_cache  

生成第 n 个斐波纳契数， 递归方式非常耗时 (因为有很多重复计算)  

    
    
    from clockdeco import clock  
    @clock  
    def fibonacci(n):  
        if n < 2:  
            return n  
        return fibonacci(n-2) + fibonacci(n-1)  
    if __name__=='__main__':  
        print(fibonacci(6))

使用缓存实现， 速度更快  

    
    
    import functools  
    from clockdeco import clock  
    @functools.lru_cache()  
    @clock  
    def fibonacci(n):  
        if n < 2:  
            return n  
        return fibonacci(n-2) + fibonacci(n-1)
    
    
    if __name__=='__main__':  
        print(fibonacci(6))

除了优化递归算法之外， lru_cache 在从 Web 中获取信息的应用中也能发挥巨大作用。  
特别要注意， lru_cache 可以使用两个可选的参数来配置。 它的签名是：  

    
    
    functools.lru_cache(maxsize=128, typed=False)

maxsize 参数指定存储多少个调用的结果。 缓存满了之后， 旧的结果会被扔掉， 腾出空间。 为了得到最佳性能， maxsize 应该设为 2 的幂。
typed 参数如果设为 True， 把不同参数类型得到的结果分开保存， 即把通常认为相等的浮点数和整数参数（ 如 1 和 1.0） 区分开。 顺便说一下，
因为 lru_cache 使用字典存储结果， 而且键根据调用时传入的定位参数和关键字参数创建， 所以被 lru_cache 装饰的函数，
它的所有参数都必须是可散列的。  


