
---
title: ubuntu配置samba
date: 2019-12-07 04:53:52.124105
Description: ""
Tags: []
Categories: []
DisableComments: false
---
使用的是正常用户，没有为samba专门新建一个用户

    
    
    1.安装samba  
    apt-get install samba  
    service smbd start  
      
    2.备份并修改配置  
    cp /etc/samba/smb.conf /etc/samba/smb.conf.bak  
    vim /etc/samba/smb.conf   
      
    3.在文件后追加配置内容  
    [username]  
    comment = share folder require password  
    browseable = yes  
    path = /home/username/sharefolder  
    create mask = 0777  
    directory mask = 0777  
    valid users = username  
    force user = username  
    force group = username  
    public = yes  
    writable = yes  
    available = yes  
      
    4.创建共享目录  
    mkdir /home/username/sharefolder  
    chmod 777 /home/username/sharefolder  
      
    5.添加用户(之后会需要设置samba的密码)  
    sudo smbpasswd -a username  
      
    6.重启samba服务器  
    sudo service smbd restart
    
    
    
    7.windows共享  
    运行栏：\\IP

如果windows 10出现: your organization's security policies block unauthenticated
guest access...错误

![](http://image.wxioi.com/9ef6cc0a9d3bb1bf3b19447f096bd8f3.PNG)  

如果windows登录密码一直出错

[global]  
25 ntlm auth = true


