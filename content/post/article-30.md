
---
title: centos7 安装scrapy的一些问题
date: 2019-07-30 17:04:31.769091
Description: ""
Tags: []
Categories: []
DisableComments: false
---
centos7目前官方源支持的python3版本只支持到python3.4，我没有通过源码安装更新过，所以安装scrapy时有些问题  
  
1\. pip3 install scrapy  
最新版本的scrapy依赖4.4.0的lxml，python3.4不支持  
随便挑了一个之前的lxml来安装  
pip3 install lxml==4.3.0  
安装OK  
  
2.再次pip3 install scrapy  
这次是twisted安装失败，因为twisted需要编译，所以需要安装如下依赖  
1.先安装gcc  
yum -y install gcc  
2.安装python-dev  
centos7需要添加源  
# 安装EPEL源  
yum install epel-release -y  
# 安装python3开发包  
yum install python34-devel -y  
  
3.再次安装scrapy，成功  
  
这里有个问题，scrapy和twisted都是最新版本，lxml是老一点的版本，在使用中可能会有些问题  
  
看来还是得抽空把python升级到3.7最好了  
  
PS:果然有点小问题

在最新版本中给crawl传递是的一个object

process.crawl(VgtimeV2Spider())

在centos我装的那个版本里面，是class

process.crawl(VgtimeV2Spider)

参考资料:

https://www.jianshu.com/p/b6fc687ccfe8  
  
  


