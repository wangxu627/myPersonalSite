
---
title: gunicorn导入报错No module named
date: 2019-07-02 15:13:28.590701
Description: ""
Tags: []
Categories: []
DisableComments: false
---
用python -m flask run可以运行，但是用gunicorn的时候报错，参考了这位兄弟的文章

<https://www.cnblogs.com/sudawei/p/3467919.html>  

主要就是在PYTHONPATH中把上层目录加入到环境变量中，这样项目所在的文件夹才会被当做包来处理

    
    
    export PYTHONPATH=..

  


