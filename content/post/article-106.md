
---
title: 使用python编码解码html特殊符号
date: 2020-01-27 14:30:43.982586
Description: ""
Tags: []
Categories: []
DisableComments: false
---
比如,+,<,>,=

    
    
    from urllib.parse import quote,unquote  
      
    unquote("%3d")  
    quote("=")

  


