---
title: "Redis批量查询删除KEYS"
date: 2020-10-15T15:59:28+08:00
Description: ""
Tags: []
Categories: []
DisableComments: false
---

对腾讯云的Redis集群不支持很多指令（config get * 、flushdb、flushall、等相关指令）  
redis指令限制：https://www.qcloud.com/document/product/239/4073

没有办法，也需想出办法。。.

---
删除单个：del key

删除多个：redis-cli -h ip -a pass(密码)  keys 关键字 | xargs redis-cli -h ip -a pass(密码) del         #Linux下的管道符批量操作


#在redis的客户端连接处登陆删除

./redis-cli -h 10.111.0.xx  -a xx   keys '*str_ account*' | xargs ./redis-cli -h 10.111.0.xx  -a xx  del

#环境变量直接使用 ln -s  /tmp/redis/src/redis-cli  /usr/bin/
redis-cli -h 10.111.0.xx -a xx  keys '*wxsmrzResult*' | xargs redis-cli -h 10.111.0.xx  -a xx  del 

#在没有，指令限制的情况下，可以使用Redis的flushdb和flushall命令

删除当前数据库中的所有Key flushdb

删除所有数据库中的key       flushall

要访问 Redis 中特定的数据库

指定数据序号为0，即默认数据库 redis-cli -n 0 keys "*" | xargs redis-cli -n 0 del

---

注：keys 指令可以进行模糊匹配，但如果 Key 含空格，就匹配不到了

* h?llo matches hello, hallo and hxllo           #? 匹配任意单个字符
* h*llo matches hllo and heeeello               #* 匹配任意字符
* h[ae]llo matches hello and hallo, but not hillo  # 或者
* h[^e]llo matches hallo, hbllo, ... but not hello   #排除
* h[a-b]llo matches hallo and hbllo             #

Use \ to escape special characters if you want to match them verbatim.
