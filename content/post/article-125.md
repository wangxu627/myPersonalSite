
---
title: pip换源相关操作
date: 2020-03-31 03:33:46.632087
Description: ""
Tags: []
Categories: []
DisableComments: false
---
为pip换个国内源还是很有必要的，这里推荐阿里源，因为东西最全。

  
更换默认源  
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple  
然后可以发现在目录“C:\Users\\{$YOUR NAME$}\AppData\Roaming\pip”中的pip.ini文件下中有修改过的内容  
  
临时改变源  
仅仅在使用pip的时候用参数i  
pip install xxxxx -i https://mirrors.aliyun.com/pypi/simple

  

豆瓣：[http://pypi.douban.com/simple/](https://pypi.douban.com/simple/)

清华：<https://pypi.tuna.tsinghua.edu.cn/simple>

阿里：http://mirrors.aliyun.com/pypi/simple/  
  

另外也可以手动修改：

永久修改，一劳永逸：  
  
linux下，修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url至tuna，内容如下：  
 [global]  
 index-url = https://pypi.tuna.tsinghua.edu.cn/simple  
  
windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下  
 [global]  
 index-url = https://pypi.tuna.tsinghua.edu.cn/simple  
  


