
---
title: python和c++关系运算符区别
date: 2019-11-17 07:27:19.083901
Description: ""
Tags: []
Categories: []
DisableComments: false
---
python:

a = 4 > 3 > 2 > 1 等效为

a = 4 > 3 && 3 > 2 && 2 > 1

a == True  

c++:

a = 4 > 3 > 2 > 1 等效为

tmp = 4 > 3 => tmp = 1(TRUE)

tmp = 1 > 3 => tmp = 0(FALSE)

a = 0 > 1 => a = 0(False)

a == 0  


