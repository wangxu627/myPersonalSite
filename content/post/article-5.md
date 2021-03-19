
---
title: SourceTree跳过注册安装使用
date: 2019-06-19 10:32:08.180067
Description: ""
Tags: []
Categories: []
DisableComments: false
---
下载链接 <https://www.sourcetreeapp.com/>  

![](https://img-
blog.csdn.net/20180618013031557?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NodXl1ZWEz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

![](https://img-
blog.csdn.net/20180618013057594?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NodXl1ZWEz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

这个时候会要求注册账号,这个时候关掉就可以了

我们进入`%LocalAppData%\Atlassian\SourceTree\`目录

![](https://img-
blog.csdn.net/20180618013116433?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NodXl1ZWEz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
创建一个`accounts.json`文件,写入以下内容

    
    
    [  
      {  
        "$id": "1",  
        "$type": "SourceTree.Api.Host.Identity.Model.IdentityAccount, SourceTree.Api.Host.Identity",  
        "Authenticate": true,  
        "HostInstance": {  
          "$id": "2",  
          "$type": "SourceTree.Host.Atlassianaccount.AtlassianAccountInstance, SourceTree.Host.AtlassianAccount",  
          "Host": {  
            "$id": "3",  
            "$type": "SourceTree.Host.Atlassianaccount.AtlassianAccountHost, SourceTree.Host.AtlassianAccount",  
            "Id": "atlassian account"  
          },  
          "BaseUrl": "https://id.atlassian.com/"  
        },  
        "Credentials": {  
          "$id": "4",  
          "$type": "SourceTree.Model.BasicAuthCredentials, SourceTree.Api.Account",  
          "Username": "",  
          "Email": null  
        },  
        "IsDefault": false  
      }  
    ]

然后打开安装好的`Sourcetree`软件

会重新进入到界面

![](https://img-
blog.csdn.net/20180618013137762?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NodXl1ZWEz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

我们直接下一步,会提示我们注册完成了.  

![](https://img-
blog.csdn.net/20180618013151876?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NodXl1ZWEz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

继续下一步,会让你选择用什么`git`  

![](https://img-
blog.csdn.net/20180618013204786?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NodXl1ZWEz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

如果使用git客户端,选择`我不想使用Mercurial即可`.  

![](https://img-
blog.csdn.net/20180618013217355?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NodXl1ZWEz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
这样就直接安装完成了.  


