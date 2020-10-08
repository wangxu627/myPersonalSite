
---
title: centos 解决python3.7 安装时No module named _ssl
date: 2019-12-25 20:34:19.947659
Description: ""
Tags: []
Categories: []
DisableComments: false
---
centos安装python3.7时遇到如下问题，查阅知需要的openssl版本最低为1.0.2，但是centos
默认的为1.0.1，所以需要重新更新openssl  

    
    
    import _ssl       # if we can't import it, let the error propagate  
    ImportError: No module named _ssl

1、安装依赖库：

    
    
    yum install -y zlib zlib-dev openssl-devel sqlite-devel bzip2-devel libffi libffi-devel gcc gcc-c++
    

2、安装最新版本的openssl  
注意！openssl配置是用config，而不是configure，另外openssl编译安装依赖zlib动态库，所以一定要shared zlib  
自行到官网查阅最新版本~

    
    
    wget http://www.openssl.org/source/openssl-1.1.1.tar.gz
    tar -zxvf openssl-1.1.1.tar.gz
    cd openssl-1.1.1
    ./config --prefix=$HOME/openssl shared zlib
    make && make install
    

3、设置环境变量LD_LIBRARY_PATH

    
    
    echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/openssl/lib" >> $HOME/.bash_profile
    source $HOME/.bash_profile
    

这一步一定要有！！LD_LIBRARY_PATH环境变量主要用于指定查找共享库（动态链接库）时除了默认路径之外的其他路径。当执行函数动态链接.so时，如果此文件不在缺省目录下‘/lib'
and ‘/usr/lib'，那么就需要指定环境变量LD_LIBRARY_PATH  
4、解压python3.7，并安装，一定要指定刚才安装的1.1.1版本的openssl！！！

    
    
    tar -zxvf Python-3.7.0.tgz
    ./configure --prefix=$HOME/Py37 --with-openssl=$HOME/openssl
    make && make install
    echo $HOME
    
    

5、至此python3.7就安装完了，来检验下ssl模块能否被导入吧：

    
    
    [root@izbp12am8wqrn7t6wzgmydz Python-3.7.0]# echo $HOME
    /root
    [root@izbp12am8wqrn7t6wzgmydz Python-3.7.0]# cd /root/Py37/
    [root@izbp12am8wqrn7t6wzgmydz bin]# ./python3
    Python 3.7.0 (default, Sep 16 2018, 14:12:43)
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import ssl
    >>> import _ssl
    >>>
    

6.更新python软链接  
你要知道系统现在的python的位置在哪儿

    
    
    [root@izbp12am8wqrn7t6wzgmydz bin]# whereis python
    python: /usr/bin/python /usr/bin/python2.7 /usr/bin/python.bak /usr/lib/python2.7 /usr/lib64/python2.7 /etc/python /usr/include/python2.7 /usr/local/python /usr/share/man/man1/python.1.gz
    
    
    
    [root@root ~]# cd /usr/bin/
    [root@root bin]# ll python*
    lrwxrwxrwx. 1 root root    7 2月   7 09:30 python -> python2
    lrwxrwxrwx. 1 root root    9 2月   7 09:30 python2 -> python2.7
    -rwxr-xr-x. 1 root root 7136 8月   4 2017 python2.7
    
    

可以看到，python指向的是python2，python2指向的是python2.7，因此我们可以装个python3，然后将python指向python3，然后python2指向python2.7，那么两个版本的python就能共存了。

7.添加软链接

    
    
    将原来的链接备份
    mv /usr/bin/python /usr/bin/python.bak
    
    添加python3的软链接
    ln -s /root/Py37/bin/python3.7 /usr/bin/python
    
    测试是否安装成功了
    python -V
    


