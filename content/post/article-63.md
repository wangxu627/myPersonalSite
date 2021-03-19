
---
title: Navicat连接MySQL8.0亲测有效
date: 2019-11-07 01:44:03.689991
Description: ""
Tags: []
Categories: []
DisableComments: false
---
原文地址:<https://www.cnblogs.com/shiysin/p/shiysin.html>   **  
**

 **今天下了个 MySQL8.0，发现Navicat连接不上，总是报错1251；**

 **原因是MySQL8.0版本的加密方式和MySQL5.0的不一样，连接会报错。**

 **试了很多种方法，终于找到一种可以实现的：**

 **更改加密方式**

_1.先通过命令行进入mysql的root账户：_

    
    
    PS C:\Windows\system32> mysql -uroot -p

_再输入root的密码：_

    
    
    Enter password: ******
    
    
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 18
    Server version: 8.0.11 MySQL Community Server - GPL
    Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.
    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
    mysql>

 _2.更改加密方式：_

    
    
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;
    Query OK, 0 rows affected (0.10 sec)

 _  3.更改密码：_

    
    
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
    Query OK, 0 rows affected (0.35 sec)

 _4.刷新：_

    
    
    mysql> FLUSH PRIVILEGES;
    Query OK, 0 rows affected (0.28 sec)

 _// 如果报错    _ERROR 1396 (HY000): Operation ALTER USER failed for 'root'@'%'
_：_

 _则是远程访问权限不正确，先选择数据库，查看一下再更改：_

    
    
    mysql> use mysql;
    Database changed  
    
    mysql> select user,host from user;
    +------------------+-----------+
    | user             | host      |
    +------------------+-----------+
    | mysql.infoschema | localhost |
    | mysql.session    | localhost |
    | mysql.sys        | localhost |
    | root             | localhost |
    +------------------+-----------+
    5 rows in set (0.00 sec)


