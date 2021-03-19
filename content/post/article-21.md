
---
title: HTTPS的连接过程
date: 2019-07-16 13:31:07.081440
Description: ""
Tags: []
Categories: []
DisableComments: false
---
![](http://image.wxioi.com/484693311170910ef05d6afb8a0c895a.png)  

1.客户端发送Client Hello报文开始SSL通信，包围中包含客户端支持的SSL版本，加密组件列表

2.SSL可用时，服务器回复Server Hello，和客户端报文一样，包含SSL版本和加密组件，该信息是从Step1中筛选出来的

3.之后发送Certificate报文，该报文包含公开密钥

4.最后发送Server Hello Done报文通知客户端，最初的SSL握手协商结束

5.客户端发送Client Key Exchange报文作为回应，其中包含Pre-master secret作为随机字符串。该报文已用公钥加密

6.客户端继续发送Change Cipher Spec报文，该报文提示服务器，此报文之后的报文会用Pre-master secret加密

7.客户端发送Finished报文。该报文包含至今全部报文的校验值

8.服务器同样发送Change Cipher Spec报文

9.服务器同样发送Finished报文

10.服务器和客户端的Finished报文交换完毕之后，SSL连接就算建立完成

11.应用层HTTP消息

12.断开消息，发送close_notify

  

后续是TCP的四次握手断开


