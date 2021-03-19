
---
title: 百度云盘分享链接密码获取
date: 2019-11-25 10:23:17.061837
Description: ""
Tags: []
Categories: []
DisableComments: false
---
## 1.安装云盘万能钥匙

<http://ypsuperkey.meek.com.cn/helps/intro>  

<http://ypsuperkey.meek.com.cn/query>  

## 2.使用API

1.API地址  
https://nuexini.gq/bdp.php?url=  
2.使用方法  
url=后面跟百度网盘分享链接，例如我的网盘链接为：https://pan.baidu.com/s/1FOX8GE1qQ0H9VK5M4nZeDQ  
  
组合成为：https://nuexini.gq/bdp.php?url=https://pan.baidu.com/s/1FOX8GE1qQ0H9VK5M4nZeDQ  
  
之后会返回一段json文本  

    
    
    {"_id":"5c59338a4b3f411eac7a6375","type":"BDY","pid":"FOX8GE1qQ0H9VK5M4nZeDQ","invalid_count":0,"state":"VALID","updated_at":"2019-02-05 15:28:28","created_at":"2019-02-05 14:56:10","access_code":"rie7","referrer":{"0363d7f8c949b9b4d516e014d1f03dcf":{"url":"http:\/\/www.gscq.me\/thread-10276.htm","title":"[GSCQ][\u6e56\u5357\u536b\u89c6\u300a\u6b4c\u624b2019\u300b\u7b2c\u56db\u671f\uff1a\u9f50\u8c6b\u6d12\u6cea\u5531\u300a\u4eca\u4e16\u300b\u5fc6\u4e09\u6bdb \u6ce2\u7433\u5a1c\u70b8\u88c2\u9ad8\u97f3\u5f3a\u52bf\u8865\u4f4d][1080I\/TS][720P\/MP4][6.96G+2.03G]-\u97f3\u4e50\/\u7efc\u827a-\u4e50\u8d4f GSCQ.ME"}}}

  

3.查找密码  
找到代码：access_code":"rie7"  
  
rie7 就是我们的百度网盘分享链接提取码  
  
4.完成  


