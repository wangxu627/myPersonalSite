
---
title: redis暴露公网导致被挖矿病毒感染
date: 2019-12-22 14:28:10.479454
Description: ""
Tags: []
Categories: []
DisableComments: false
---
原因：

1.redis暴露公网ip

2.redis没有设置访问密码

3.使用root用户启动redis

现象：

自己部署的服务会定期被取消，且ssh不上去，重启之后能ssh上，不过服务还是会被取消

通过观察现象，发现规律是定时被取消，并且ps -elf后发现了crontab这个进程（是一个定时任务）

crontab -l 发现一堆奇怪的东西，类似这种

![](http://5b0988e595225.cdn.sohucs.com/images/20190904/62c48f0672784ffaac15862e01f0ffd5.jpeg)  

google后发现这很可能是挖矿病毒的定时任务，然后通过观察/.ssh/ authorized_keys 文件，发现里面有一个并不是我主机的公钥

另外，netstat -anp | grep 80也发现连接到了一些奇奇怪怪的主机上

  

解决步骤：

1.删除crontab，使用systemctl stop crontab或 rm -rf /etc/cron.d/*；

2.删除或修改authorized_hosts，在删除他的时候发现我root用户居然也删不掉，lsattr发现有个-i的属性，删除并重装apt-get
install e2fsprogs或者yum install e2fsprogs，后使用chattr -i  authorized_keys 解决

3.关闭crontab的开机启动， systemctl disable crontab

4.重启机器

  

原理：

<https://www.cnblogs.com/evan-blog/p/10707087.html>  

参考：

<http://www.sohu.com/a/338718240_354899>  

<https://blog.csdn.net/lailaiquququ11/article/details/83510406>  

<https://www.jianshu.com/p/93dc6f774b72>  

<https://www.cnblogs.com/Sungeek/p/9084022.html>  

<https://www.cnblogs.com/cpl9412290130/p/11592803.html>  

<https://www.cnblogs.com/linjiqin/p/11720673.html>  


