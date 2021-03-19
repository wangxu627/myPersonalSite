
---
title: Python包的相对导入时出现错误的解决方法
date: 2019-10-30 04:36:36.966919
Description: ""
Tags: []
Categories: []
DisableComments: false
---
转载地址：https://www.cnblogs.com/ArsenalfanInECNU/p/5346751.html

  

在练习Python中package的相对导入时，即

    
    
    from . import XXX

或者

    
    
    from .. import XXX

时会遇到这样两个错误：

    
    
    SystemError: Parent module '' not loaded, cannot perform relative import

和

    
    
    ValueError: attempted relative import beyond top-level package



其实这两个错误的原因归根结底是一样的：在涉及到相对导入时，package所对应的文件夹必须正确的被python解释器视作package，而不是普通文件夹。否则由于不被视作package，无法利用package之间的嵌套关系实现python中包的相对导入。

文件夹被python解释器视作package需要满足两个条件：

**1、文件夹中必须有__init__.py文件，该文件可以为空，但必须存在该文件。**

**2、不能作为顶层模块来执行该文件夹中的py文件（即不能作为主函数的入口）。**

**补充：在"from YY import
XX"这样的代码中，无论是XX还是YY，只要被python解释器视作package，就会首先调用该package的__init__.py文件。如果都是package，则调用顺序是YY，XX。**

**另外，练习中“from . import XXX”和“from .. import
XXX”中的'.'和'..'，可以等同于linux里的shell中'.'和'..'的作用，表示当前工作目录的package和上一级的package。**

举个例子：

目录树

testIm/

\--__init__.py

\--main.py : from Tom import tom

\--Tom/

\--__init__.py : print("I'm Tom's __init__!")

\--tom.py : from . import tomBrother, from .. import kate,print("I'm Tom!")

\--tomBrother.py print(I'm Tom's Brother!)

\--Kate/

\--__init__.py : print("I'm Kate's __init__!")

\--kate.py

运行文件：main.py

结果：

    
    
    I'm Tom's __init__!
    I'm Tom's Brother!
    Traceback (most recent call last):
    File "D:\PythonLearning\TestIm\main.py", line 3, in <module>
    from Tom import tom
    File "D:\PythonLearning\TestIm\Kate\kate.py", line 4, in <module>
    from .. import kate
    ValueError: attempted relative import beyond top-level package
    >>>

可以看到from . import
tomBrother顺利执行，首先执行了Tom文件夹下的__init__.py文件，后来执行了tomBrother.py文件，但是当执行到“from ..
import
kate”时报错，这是因为我们是在TestIm文件夹下把main.py文件作为主函数的入口执行的，因此尽管TestIm文件夹中有__init__.py文件，但是该文件夹不能被python解释器视作package，即Tom
package不存在上层packge，自然会报错，相对导入时超出了最高层级的package。

修改方法：

目录树

test/

\--main.py : from testIm.Tom import tom

\--testIm/

\--__init__.py

\--Tom/

\--__init__.py : print("I'm Tom's __init__!")

\--tom.py : from . import tomBrother, from .. import Kate,print("I'm Tom!")

\--tomBrother.py print(I'm Tom's Brother!)

\--Kate/

\--__init__.py : print("I'm Kate's __init__!")

\--kate.py

运行文件：main.py

结果：

    
    
    I'm top's __init__!
    I'm Tom's __init__!
    I'm Tom's Brother!!
    I'm Kate's __init__!
    I'm Tom!

即主函数入口不在TestIm中，则TestIm和其同样包含__init__.py文件的子文件夹都被python解释器视作package，形成相应的嵌套关系。可以正常使用from
. import XXX和from .. import XXX。

  

补充:

如果相对层级超过两层，则只需要加一个点来表示相对路径，如

from ... import a # 表示向上2层  

from ....module2 import c # 向上3层  


