
---
title: Python中的所有特殊方法
date: 2019-07-11 08:32:28.825104
Description: ""
Tags: []
Categories: []
DisableComments: false
---
方法 | 介绍  
---|---  
   `object.``__new__`( _cls_ [,  _..._ ])|  一个静态方法，主要用来定制不可变的子类类型  
  `object.``__init__`( _self_ [,  _..._ ])|  在对象被创建时调用，类似于C++或Java中的构造函数，
但[`__init__()`](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__init__
"object.__init__")返回的值只能是`None`，否则会在运行时引发
[`TypeError`](https://docs.python.org/zh-
cn/3/library/exceptions.html#TypeError "TypeError")。  
  `object.``__del__`( _self_ )|  在对象被销毁是调用类似于C++中的析构函数（ java则是finalize ）,
[`__del__()`](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__del__ "object.__del__") 方法可以 (但不推荐!)
通过创建一个该实例的新引用来推迟其销毁 。这被称为对象  _重生_  
  
  `object.``__repr__`( _self_ )|  在调用repr(obj)方法时被调用，用于生成对象的调试字符串  
  `object.``__str__`( _self_ )|
在调用str(obj)，format(),print()方法时被调用，用于生成对象的显示字符串，该方法和 `object.``__repr__`(
_self_
)类似，具体区别可以查看[Python中__repr__和__str__区别](http://www.wxioi.com/article/14)  
  `object.``__bytes__`( _self_ )  |   通过 [bytes](https://docs.python.org/zh-
cn/3/library/functions.html#func-bytes) 调用以生成一个对象的字节串表示。这应该返回一个
[`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes "bytes")
对象  
  `object.``__format__`( _self_ ,  _format_spec_ )| 在调用内置函数format()的时候被调用  
 `object.``__lt__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__lt__ "永久链接至目标")

`object.``__le__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__le__ "永久链接至目标")

`object.``__eq__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__eq__ "永久链接至目标")

`object.``__ne__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__ne__ "永久链接至目标")

`object.``__gt__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__gt__ "永久链接至目标")

`object.``__ge__`( _self_ ,  _other_ )

|   这些被称为“富比较”方法。运算符号与方法名称的对应关系如下：`x<y` 调用 `x.__lt__(y)`、`x<=y` 调用
`x.__le__(y)`、`x==y` 调用 `x.__eq__(y)`、`x!=y` 调用 `x.__ne__(y)`、`x>y` 调用
`x.__gt__(y)`、`x>=y` 调用 `x.__ge__(y)`  
  `object.``__hash__`( _self_ )|   内置函数 [`hash()`](https://docs.python.org/zh-
cn/3/library/functions.html#hash "hash") 调用时被调用;应该返回一个整数  
  `object.``__bool__`( _self_ )|   内置的 `bool()` 操作执行时被调用；应该返回 `False` 或 `True`  
  `object.``__getattr__`( _self_ ,  _name_ )|   当默认属性访问因引发
[`AttributeError`](https://docs.python.org/zh-
cn/3/library/exceptions.html#AttributeError "AttributeError") 而失败时被调用，
请注意如果属性是通过正常机制找到的，[`__getattr__()`](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__getattr__ "object.__getattr__") 就不会被调用  
  
  `object.``__getattribute__`( _self_ ,  _name_ )|
此方法会无条件地被调用以实现对类实例属性的访问。如果类还定义了 [`__getattr__()`](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__getattr__
"object.__getattr__")，则后者不会被调用，除非
[`__getattribute__()`](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__getattribute__
"object.__getattribute__") 显式地调用它或是引发了
`[AttributeError](https://docs.python.org/zh-
cn/3/library/exceptions.html#AttributeError
"AttributeError")。简单理解就是`__getattribute__的优先级比 __getattr__高  
  `object.``__setattr__`( _self_ ,  _name_ ,  _value_ )  |   此方法在一个属性被尝试赋值时被调用  
  `object.``__delattr__`( _self_ ,  _name_ )|   此方法应该仅在 `del obj.name`
对于该对象有意义时才被实现  
  `object.``__dir__`( _self_ )|   此方法会在对相应对象调用
[`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir "dir")
时被调用。返回值必须为一个序列。 [`dir()`](https://docs.python.org/zh-
cn/3/library/functions.html#dir "dir") 会把返回的序列转换为列表并对其排序。  
  `object.``__get__`( _self_ ,  _instance_ ,  _owner_ )  |  
  `object.``__set__`( _self_ ,  _instance_ ,  _value_ )|  
  `object.``__delete__`( _self_ ,  _instance_ )|  
  `object.``__set_name__`( _self_ ,  _owner_ ,  _name_ )|  
  `object.``__slots__`|   这个类变量可赋值为字符串、可迭代对象或由实例使用的变量名构成的字符串序列。  ___slots___
会为已声明的变量保留空间，并阻止自动为每个实例创建  ___dict___  和  ___weakref___ 。  
  `object.``__call__`( _self_ [,  _args..._ ])|
此方法会在实例作为一个函数被“调用”时被调用；如果定义了此方法，则 `x(arg1, arg2, ...)` 就相当于 `x.__call__(arg1,
arg2, ...)` 的快捷方式。  
  `object.``__len__`( _self_ )  |   调用此方法以实现内置函数
[`len()`](https://docs.python.org/zh-cn/3/library/functions.html#len "len")  
  
  `object.``__getitem__`( _self_ ,  _key_ )|   调用此方法以实现 `self[key]` 的求值  
  `object.``__setitem__`( _self_ ,  _key_ ,  _value_ )|   调用此方法以实现向
`self[key]` 赋值  
  `object.``__delitem__`( _self_ ,  _key_ )|   调用此方法以实现 `self[key]` 的删除  
  `object.``__missing__`( _self_ ,  _key_ )|   此方法由
[`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict
"dict").[`__getitem__()`](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
在找不到字典中的键时调用以实现 dict 子类的 `self[key]`。  
  `object.``__iter__`( _self_ )|   此方法在需要为容器创建迭代器时被调用  
  `object.``__reversed__`( _self_ )|   此方法（如果存在）会被
[`reversed()`](https://docs.python.org/zh-cn/3/library/functions.html#reversed
"reversed") 内置函数调用以实现逆向迭代。它应当返回一个新的以逆序逐个迭代容器内所有对象的迭代器对象。  
  `object.``__contains__`( _self_ ,  _item_ )|   调用此方法以实现成员检测运算符  
 `object.``__add__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__add__ "永久链接至目标")

`object.``__sub__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__sub__ "永久链接至目标")

`object.``__mul__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__mul__ "永久链接至目标")

`object.``__matmul__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__matmul__ "永久链接至目标")

`object.``__truediv__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__truediv__ "永久链接至目标")

`object.``__floordiv__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__floordiv__ "永久链接至目标")

`object.``__mod__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__mod__ "永久链接至目标")

`object.``__divmod__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__divmod__ "永久链接至目标")

`object.``__pow__`( _self_ ,  _other_ [,  _modulo_
])[](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__pow__
"永久链接至目标")

`object.``__lshift__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__lshift__ "永久链接至目标")

`object.``__rshift__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__rshift__ "永久链接至目标")

`object.``__and__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__and__ "永久链接至目标")

`object.``__xor__`( _self_ ,  _other_ )[](https://docs.python.org/zh-
cn/3/reference/datamodel.html#object.__xor__ "永久链接至目标")

`object.``__or__`( _self_ ,  _other_ )

|   调用这些方法来实现二进制算术运算 (`+`, `-`, `*`, `@`, `/`, `//`, `%`,
[`divmod()`](https://docs.python.org/zh-cn/3/library/functions.html#divmod
"divmod"), [`pow()`](https://docs.python.org/zh-
cn/3/library/functions.html#pow "pow"), `**`, `<<`, `>>`, `&`, `^`, `|`)  
  
  


