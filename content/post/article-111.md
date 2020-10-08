
---
title: img标签src引用网络图片，响应403的解决方法
date: 2020-02-09 11:39:33.084305
Description: ""
Tags: []
Categories: []
DisableComments: false
---
在html页面加入<meta name="referrer" content="no-referrer">标签，就可以解决页面加载网络图片的问题，  
  
原因大概是网络安全的问题，别人的页面做了安全防护的问题。  
  
在html的head标签中加上：  
  
<meta name="referrer" content="no-referrer" /> <!--可以让img标签预加载网络图片-->  
  
  
Referer简介  
  
简单来说，Referer是HTTP协议中的一个请求报头，用于告知服务器用户的来源页面。比如说你从Google搜索结果中点击进入了某个页面，那么该次HTTP请求中的Referer就是Google搜索结果页面的地址。如果你的某篇博客中引用了其他地方的一张图片，那么对该图片的HTTP请求中的Referer就是你那篇博客的地址。  
一般Referer主要用于统计，像CNZZ、百度统计等可以通过Referer统计访问流量的来源和搜索的关键词（包含在URL中）等等，方便站长们有针性对的进行推广和SEO什么的  
当然Referer另一个用处就是防盗链了，主要是图片和网盘服务器使用的较多。盗链的危害不言而喻，侵犯了版权不说，增加了服务器的负荷，却没有给真正的服务提供者带来实际利益（广告点击什么的）  
  
  
另外要注意的是，Referer是由浏览器自动为我们加上的  
  
原文链接：https://blog.csdn.net/lidongliangzhicai/article/details/94961428


