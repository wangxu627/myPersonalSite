
---
title: Python 描述符 (descriptor) 详解
date: 2019-10-10 11:12:28.664369
Description: ""
Tags: []
Categories: []
DisableComments: false
---
## 什么是描述符

python描述符是一个“绑定行为”的对象属性，在描述符协议中，它可以通过方法重写属性的访问。这些方法有  **get** (),  **set** (),
和 **delete** ()。如果这些方法中的任何一个被定义在一个对象中，这个对象就是一个描述符。

## 讲解描述符前，先看一下属性： **dict**  （每个对象均具备该属性）

作用：字典类型，存放本对象的属性，key(键)即为属性名，value(值)即为属性的值，形式为{attr_key : attr_value}。

对象属性的访问顺序：  
1\. 实例属性  
2\. 类属性  
3\. 父类属性  
4\. __getattr__()方法

  

    
    
    class Test(object):  
        cls_val = 1  
        def __init__(self):  
            self.ins_val = 10  
      
    t = Test()  
      
    print(Test.__dict__)  
    print('*'*100)  
    print(t.__dict__)  
    ""  
    {'__dict__': <attribute '__dict__' of 'Test' objects>, '__doc__': None, '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__init__': <function Test.__init__ at 0x7fa91afb0ea0>, 'cls_val': 1}  
    ****************************************************************************************************  
    {'ins_val': 10}  
    ""

从以上代码可以看出，实例t的属性并不包含cls_val，cls_val是属于类Test的。

## 魔法方法：__get__(), __set__(), __delete__()

方法的原型为：  
1\. __get__(self, instance, owner)  
2\. __set__(self, instance, value)  
3\. __delete__(self, instance)

首先我们先看一段代码：

    
    
    class Desc(object):  
      
        def __get__(self, instance, owner):  
            print("get!!!!")  
            print("self=", self)  
            print("instance=", instance)  
            print("owner=", owner)  
            print('*'*50, "\n")  
      
        def __set__(self, instance, value):  
            print("set!!!!")  
            print("self=", self)  
            print("instance=", instance)  
            print("value=", value)  
            print('*'*50, "\n")  
      
      
    class TestDesc(object):  
        x = Desc()  
      
    t = TestDesc()  
    t.x  
      
    print(t.__dict__)  
    print(TestDesc.__dict__)  
    ""  
    get!!!!  
    self= <__main__.Desc object at 0x7fa91a756978>  
    instance= <__main__.TestDesc object at 0x7fa91a756a20>  
    owner= <class '__main__.TestDesc'>  
    **************************************************   
      
    {}  
    {'__dict__': <attribute '__dict__' of 'TestDesc' objects>, '__doc__': None, '__module__': '__main__', 'x': <__main__.Desc object at 0x7fa91a756e80>, '__weakref__': <attribute '__weakref__' of 'TestDesc' objects>}  
    ""

可以看到，实例化类TestDesc后，调用对象t访问其属性x，会自动调用类Desc的 __get__方法，由输出信息可以看出：  
1\. self: 是Desc的实例对象，也是TestDesc的属性x  
2\. instance: 是TestDesc的实例对象，在上面的例子是实例化后的变量t  
3\. owner: 是TestDesc这个类，因为Desc是包含在它的内部，所以TestDesc拥有所属权

其实Desc类就是是一个描述符（描述符是一个类），因为类Desc定义了方法 __get__, __set__。所以，只要是内部定义了方法
__get__(), __set__(), __delete__()中的一个或多个，就可以称为描述符。

## 访问t.x的时候，为什么会直接去调用描述符的 __get__() 方法

t为实例，访问t.x时，顺序如下：  
1\. 先访问实例属性；其次访问类属性  
2\. 判断属性 x 为一个描述符，则将 TestDesc.x 转化为TestDesc.__dict__[‘x’].__get__(t, TestDesc)
来访问  
3\. 进入类Desc的 __get__()方法，进行相应的操作

## 描述符的对象 x 其实是类 TestDesc 的类属性，那么可不可以把它变成实例属性呢

    
    
    class Desc(object):  
        def __init__(self, name):  
            self.name = name  
      
        def __get__(self, instance, owner):  
            print("get")  
            print('name=',self.name)   
            print('*'*50, "\n")  
      
    class TestDesc(object):  
        x = Desc('x')  
      
        def __init__(self):  
            self.y = Desc('y')  
      
    #以下为测试代码  
    t = TestDesc()  
    t.x  
    t.y  
      
    print(t.__dict__)  
    print(TestDesc.__dict__)  
      
    ""  
    get  
    name= x  
    **************************************************   
      
    {'y': <__main__.Desc object at 0x7fa91a6ee7b8>}  
    {'__dict__': <attribute '__dict__' of 'TestDesc' objects>, '__doc__': None, '__module__': '__main__', 'x': <__main__.Desc object at 0x7fa91a6ee6d8>, '__weakref__': <attribute '__weakref__' of 'TestDesc' objects>, '__init__': <function TestDesc.__init__ at 0x7fa91a732620>}  
    ""

从上面可以看到如果是实例属性，则没有调用__get__()方法，这是因为调用 t.y 时，首先会去调用TestDesc的
__getattribute__() 方法。而y是一个描述符类，所以解释器将该方法转化为TestDesc.__dict__[‘y’].__get__(t,
TestDesc)， 但是TestDesc 并没有 y这个属性，y 是属于实例对象的，所以，只能忽略了。

## 如果 类属性的描述符对象 和 实例属性描述符的对象 同名时

    
    
    class Desc(object):  
        def __init__(self, name):  
            self.name = name  
            print("__init__(): name = ",self.name)  
      
        def __get__(self, instance, owner):  
            print("__get__() ...")  
            return self.name  
      
        def __set__(self, instance, value):  
            self.value = value  
      
    class TestDesc(object):  
        _x = Desc('x')  
        def __init__(self, x):  
            self._x = x  
      
      
    #以下为测试代码  
    t = TestDesc(10)  
    t._x  
      
    ""  
    __init__(): name =  x  
    __get__() ...  
    'x'  
    ""

上面结果表明有与描述符同名的属性时，描述符优先，会覆盖掉实例属性。如果去掉 **set** 方法呢？

    
    
    class Desc(object):  
        def __init__(self, name):  
            self.name = name  
            print("__init__(): name = ",self.name)  
      
        def __get__(self, instance, owner):  
            print("__get__() ...")  
            return self.name  
      
      
    class TestDesc(object):  
        _x = Desc('x')  
        def __init__(self, x):  
            self._x = x  
      
      
    #以下为测试代码  
    t = TestDesc(10)  
    t._x  
    ""  
    __init__(): name =  x  
    10  
    ""

 可以看到并没有覆盖掉实例属性，这个原因如下：  

只要是内部定义了方法 **get** ， **set** ， **delete** 中的一个或多个，就可以称为描述符。如果实现了 **set** 和
**get** ，则称为数据描述符；如果只实现了 **get** ，则称为非数据描述符。

每次属性查找，这个协议的方法实际上是由对象的特殊方法 **getattribute**
()调用。每次通过点号（ins.attribute）或者getattr(ins, ‘attribute’)函数调用都会隐式的调用
**getattribute** ()，它的属性查找的顺序如下：  
1\. 验证属性是否为实例的类对象的数据描述符  
2\. 查看该属性是否能在实例对象的 **dict** 中找到  
3\. 查看该属性是否为实例的类对象的非数据描述符

换句话说：数据描述符优先于 **dict** ，而 **dict** 查找优先于非数据描述符。


