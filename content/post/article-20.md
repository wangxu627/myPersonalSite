
---
title: Javascript中的bind,call和apply
date: 2019-07-16 12:59:44.455764
Description: ""
Tags: []
Categories: []
DisableComments: false
---
可以将call()和apply()看作是某个对象的方法，通过调用方法的形式来间接调用函数。其中第一个实参，在call()和apply()是调用上下文，可通过this来获得该引用

比如

    
    
    f.call(o)f.apply(o)等同于
    o.m = f
    o.m()
    delete o.m
    

call()和apply()的区别在于后续参数，call()将参数逐个传递，而apply()需要把后续参数打包成一个数组

    
    
    f.call(o,1,2,3)  
    等同于  
    f.apply(o,[1,2,3])

用途

    
    
    //在对象o的方法m调用前后增加日志，类似修饰器的功能  
    function trace(o, m) {  
        var original = o[m];  
        o[m] = function() {  
            console.log(new Date(), "Entering:", m);  
            var result = original.apply(this, arguments);  
            console.log(new Date(), "Existing:", m);  
            return result;  
        }  
    }

  

bind是es5新增的方法，作用是将函数绑定到某个对象上。当在f（）上调用bind()方法并传入一个对象o作为参数，这个方法将返回一个新函数，比如

    
    
    function f(y) {  
        return this.x + y;  
    }  
    var o = {x: 1}  
    var g = f.bind(2)  
    g(1) //  => 3

除了第一个参数，传入bind()的实参也会绑定至this，这个附带的应用是一种函数式编程技术，叫做“柯里化”

比如

    
    
    var sum = function(x, y) {  
        return x + y;  
    }  
    var succ = sum.bind(null, 1);  
    succ(2) // => 3, x绑定到1，并传入2作为实参  
      
    function f(y, z) {  
        return this.x + y + z;  
    }  
    var g = sum.bind({x:1}, 2);  
    g(3) // => 6, x绑定到1，并传入2作为实参

bind的实现

    
    
    if (!Function.prototype.bind) {  
        Function.prototype.bind = function (o, /* args */) {  
            var self = this, boundArgs = arguments;  
            return function () {  
                var args = [], i;  
                for (i = 1, i < boundArgs.length; i++) args.push(boundArgs[i]);  
                for (i = 0; i < arguments.length; i++) args.push(arguments[i]);  
                return self.apply(o, args);  
            }  
        }  
    }

  


