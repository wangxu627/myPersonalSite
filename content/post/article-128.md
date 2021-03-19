
---
title: Redis清空数据库
date: 2020-05-19 00:02:52.403635
Description: ""
Tags: []
Categories: []
DisableComments: false
---
1.flushall，清除所有数据库的所有数据

2.flushdb，清除选中数据库的所有数据

3.redis-cli KEYS "*" | xargs redis-cli del

4.redis-cli -a airflow -n 15 KEYS "*" | xargs redis-cli -a airflow -n 15
del，如果需要密码并选中某个数据库

还可以通过lua脚本：

    
    
    EVAL "return redis.call('del', unpack(redis.call('keys', ARGV[1])))" 0 prefix:[YOUR_PREFIX e.g delete_me_*]

<https://stackoverflow.com/questions/4006324/how-to-atomically-delete-keys-
matching-a-pattern-using-redis>  


