
---
title: elasticsearch常见报错
date: 2019-12-07 06:34:23.426878
Description: ""
Tags: []
Categories: []
DisableComments: false
---
[1]: max file descriptors [4096] for elasticsearch process is too low,
increase to at least [65536]  
切换到root用户，编辑limits.conf添加如下内容  
`vi /etc/security/limits.conf`  
`* soft nofile 65536`  
`* hard nofile 65536`

[2]: max number of threads [3818] for user [es] is too low, increase to at
least [4096]  
最大线程个数太低。修改配置文件etc/security/limits.conf，增加配置  
`* soft nproc 4096`  
`* hard nproc 4096`

[3]: max virtual memory areas vm.max_map_count [65530] is too low, increase to
at least [262144]  
修改/etc/sysctl.conf文件，增加配置vm.max_map_count=262144  
`vi /etc/sysctl.conf`  
`sysctl -p`  
执行命令sysctl -p生效

[4]: system call filters failed to install; check the logs and fix your
configuration or disable system call filters at your own risk  
问题原因：因为Centos6不支持SecComp，而ES5.2.1默认bootstrap.system_call_filter为true进行检测，所以导致检测失败，失败后直接导致ES不能启动  
解决方法：在elasticsearch.yml中配置bootstrap.system_call_filter为false，注意要在Memory下面:  
`bootstrap.memory_lock: false`  
`bootstrap.system_call_filter: false`

  
  


