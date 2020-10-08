
---
title: Python的矩阵乘法
date: 2020-03-31 09:12:37.673039
Description: ""
Tags: []
Categories: []
DisableComments: false
---
**Matrix multiplication**

mathutils now uses the [PEP 465](https://www.python.org/dev/peps/pep-0465/)
binary operator for multiplying matrices

<https://www.python.org/dev/peps/pep-0465/>  

  

    
    
    >>> M = Matrix()  
    >>> v = Vector()  
    >>> M @ v  
    Vector((0.0, 0.0, 0.0))  
      
    >>> v @ v  
    0.0  
      
    >>> M @ M  
    Matrix(((1.0, 0.0, 0.0, 0.0),  
            (0.0, 1.0, 0.0, 0.0),  
            (0.0, 0.0, 1.0, 0.0),  
            (0.0, 0.0, 0.0, 1.0)))

  


