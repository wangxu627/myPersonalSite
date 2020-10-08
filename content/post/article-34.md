
---
title: Python和JS中yield的一些高级使用
date: 2019-08-14 14:13:27.894340
Description: ""
Tags: []
Categories: []
DisableComments: false
---
常规用法谁都懂，不多说

JS：

    
    
    function* coroutine() {  
        yield 1  
        yield 2  
        yield 3  
    }  
      
    g = coroutine()  
    console.log(g.next().value)  
    console.log(g.next().value)  
    console.log(g.next().value)

Python：

    
    
    def coroutine():  
        yield 1  
        yield 2  
        yield 3  
      
    g = coroutine()  
    print(next(g))  
    print(next(g))  
    print(next(g))

  

如果是有嵌套的：

比较憨憨的写法JS

    
    
    function* coroutineInner() {  
        yield 1  
        yield 2  
        yield 3  
    }  
      
    function* coroutineOuter() {  
        var inner = coroutineInner()  
        for(let ret = inner.next(); ret.done == false;ret = inner.next()) {  
            yield ret.value  
        }  
        yield 11  
        yield 12  
        yield 13  
    }  
      
    g = coroutineOuter()  
    console.log(g.next().value)  
    console.log(g.next().value)  
    console.log(g.next().value)  
    console.log(g.next().value)  
    console.log(g.next().value)  
    console.log(g.next().value)

其实就是里面多了一个循环来自动yield内部的协程

Python2：

    
    
    def coroutineInner():  
        yield 1  
        yield 2  
        yield 3  
      
    def coroutineOuter():  
        for ret in coroutineInner():  
            yield ret  
        yield 11  
        yield 12  
        yield 13  
      
    g = coroutineOuter()  
    print(next(g))  
    print(next(g))  
    print(next(g))  
    print(next(g))  
    print(next(g))  
    print(next(g))

Python2和JS的憨憨写法一样

  

下面是比较高级的用法：

JS

    
    
    
    
    function* coroutineInner() {
    
        yield 1
    
        yield 2
    
        yield 3
    
    }
    
    
    function* coroutineOuter() {  
        yield* coroutineInner()  
        yield 11  
        yield 12  
        yield 13  
    }  
      
    g = coroutineOuter()  
    console.log(g.next().value)  
    console.log(g.next().value)  
    console.log(g.next().value)  
    console.log(g.next().value)  
    console.log(g.next().value)  
    console.log(g.next().value)

Python3

    
    
    def coroutineInner():  
        yield 1  
        yield 2  
        yield 3  
      
    def coroutineOuter():  
        yield from coroutineInner()  
        yield 11  
        yield 12  
        yield 13  
      
    g = coroutineOuter()  
    print(next(g))  
    print(next(g))  
    print(next(g))  
    print(next(g))  
    print(next(g))  
    print(next(g))

  

说白了就是yield*和yield from，一点也不高级


