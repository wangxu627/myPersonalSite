
---
title: linux私钥id_rsa转换成ppk
date: 2019-12-19 07:46:51.382447
Description: ""
Tags: []
Categories: []
DisableComments: false
---
大家都知道在linux下生成的ssh私钥只有Tera Term这个软件可以使用,但Tera
Term无法上传文件,只能使用winscp来上传,但winscp使用私钥的格式是ppk,所以要把linux下的私钥转换成ppk格式.

   需要的软件:puttygen.exe

1.下载puttygen

大家可以去http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html这个地址单独下载puttygen

  

2.转换成ppk格式

运行puttygen.exe-点击Conversions菜单项中的Import key,选择在linux下生成的id_rsa文件,成下面的图

[![点击查看原图](https://blog.slogra.com/content/plugins/kl_album/upload/201208/2010c394aaf9bfe594bebe9be2e74bff20120828135443645321285.jpg)](https://blog.slogra.com/content/plugins/kl_album/upload/201208/2010c394aaf9bfe594bebe9be2e74bff20120828135443645321285.jpg)  

然后点击Save provate Key按钮就可以转换成ppk格式,如图.

[![点击查看原图](https://blog.slogra.com/content/plugins/kl_album/upload/201208/117df1e0ee1bc0d50bcd0999660ea02b201208281354441634277658.jpg)](https://blog.slogra.com/content/plugins/kl_album/upload/201208/117df1e0ee1bc0d50bcd0999660ea02b201208281354441634277658.jpg)  

[![点击查看原图](https://blog.slogra.com/content/plugins/kl_album/upload/201208/c8e8b891489d204632415ff5385d5bd1201208281354442074591326.jpg)](https://blog.slogra.com/content/plugins/kl_album/upload/201208/c8e8b891489d204632415ff5385d5bd1201208281354442074591326.jpg)  

好了大家可以看到已经把原来rsa格式的私钥转换成ppk的了,可以在winscp中导入使用了.  
[![点击查看原图](https://blog.slogra.com/content/plugins/kl_album/upload/201208/4abba027f6621d09b90824a88555dd23201208281354411825025545.jpg)](https://blog.slogra.com/content/plugins/kl_album/upload/201208/4abba027f6621d09b90824a88555dd23201208281354411825025545.jpg)  
好了,就到这里吧.


