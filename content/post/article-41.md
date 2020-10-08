
---
title: EAFP and LBYL
date: 2019-08-23 06:36:43.849605
Description: ""
Tags: []
Categories: []
DisableComments: false
---
EAFP  
取得原谅比获得许可容易（ easier to ask for forgiveness than  
permission） 。 这是一种常见的 Python 编程风格， 先假定存在有效  
的键或属性， 如果假定不成立， 那么捕获异常。 这种风格简单明  
快， 特点是代码中有很多 try 和 except 语句。 与其他很多语言一  
样（ 如 C 语言） ， 这种风格的对立面是 LBYL风格。  
接下来， 词汇表定义了 LBYL。  
LBYL  
三思而后行（ look before you leap） 。 这种编程风格在调用函数  
或查找属性或键之前显式测试前提条件。 与 EAFP 风格相反， 这种  
风格的特点是代码中有很多 if 语句。 在多线程环境中， LBYL风  
格可能会在“检查”和“行事”的空当引入条件竞争。 例如， 对 if  
key in mapping: return mapping[key] 这段代码来说， 如果  
在测试之后， 但在查找之前， 另一个线程从映射中删除了那个键，  
那么这段代码就会失败。 这个问题可以使用锁或者 EAFP 风格解  
决  


