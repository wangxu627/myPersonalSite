
---
title: 源码安装python
date: 2019-11-23 19:57:41.871032
Description: ""
Tags: []
Categories: []
DisableComments: false
---
1,安装Python3.6的依赖包  
# yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-
devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

# 如果是CentOS7,还需要安装  

# `yum -y install libffi-devel `

2.下载Python3  
# wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz  
3.安装python3  
创建目录：  
# mkdir -p /usr/local/python3  
解压下载好的Python-3.x.x.tgz包(具体包名因你下载的Python具体版本不不同?而不不同，如：我下载的是Python3.6.1.那我这里就是Python-3.6.1.tgz)  
# tar -zxvf Python-3.6.1.tgz  
4.进入解压后的目录，编译安装。  
# cd Python-3.6.1  
# ./configure --prefix=/usr/local/python3  
# make && make install  
  
5.建立python3的软链  
# ln -s /usr/local/python3/bin/python3 /usr/bin/python3  
6.并将/usr/local/python3/bin加入PATH  
# vim ~/.bash_profile  
# .bash_profile  
# Get the aliases and functions  
if [ -f ~/.bashrc ]; then  
. ~/.bashrc  
fi  
# User specific environment and startup programs  
PATH=$PATH:$HOME/bin:/usr/local/python3/bin  
export PATH  
按ESC，输入:wq回车退出。  
修改完记得执行行下面的命令，让上一步的修改生效：  
# source ~/.bash_profile  
检查Python3及pip3是否正常可用：  
# python3 -V  
Python 3.6.1  
# pip3 -V  
pip 9.0.1 from /usr/local/python3/lib/python3.6/site-packages (python 3.6)


