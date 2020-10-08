
---
title: sudo不需要输入密码
date: 2019-12-02 16:19:28.570575
Description: ""
Tags: []
Categories: []
DisableComments: false
---
先进入root：  
chun:su输入密码：root:su输入密码：root: gedit /etc/sudoers  
2.sudoers打开编辑：  
root ALL=(ALL:ALL) ALL  
chun ALL=(ALL:ALL) ALL  
#改为：chun ALL=(ALL:ALL) NOPASSWD:ALL  
%admin ALL=(ALL) ALL  
#改为：%admin ALL=(ALL) NOPASSWD:ALL  
%sudo ALL=(ALL:ALL) ALL  
chun ALL=(ALL) ALL  
#改为： chun ALL=(ALL) NOPASSWD:ALL  
按F2保存修改，按F3退出到终端。


