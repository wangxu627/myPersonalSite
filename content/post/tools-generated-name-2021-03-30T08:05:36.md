---
title: "Linux查看发行版方法汇总"
date: 2021-03-30T08:05:36
Description: ""
Tags: []
Categories: []
DisableComments: false
---
**方法 1： lsb_release 命令**

LSB（Linux 标准库Linux Standard Base）能够打印发行版的具体信息，包括发行版名称、版本号、代号等。
```
# lsb_release -a 
No LSB modules are available. 
Distributor ID: Ubuntu 
Description: Ubuntu 16.04.3 LTS 
Release: 16.04 
Codename: xenial
```

**方法 2： /etc/*-release 文件**

release 文件通常被视为操作系统的标识。在 /etc 目录下放置了很多记录着发行版各种信息的文件，每个发行版都各自有一套这样记录着相关信息的文件。下面是一组在 Ubuntu/Debian 系统上显示出来的文件内容。
```
# cat /etc/issue 
Ubuntu 16.04.3 LTS \n \l 
# cat /etc/issue.net 
Ubuntu 16.04.3 LTS 
# cat /etc/lsb-release 
DISTRIB_ID=Ubuntu 
DISTRIB_RELEASE=16.04 
DISTRIB_CODENAME=xenial 
DISTRIB_DESCRIPTION="Ubuntu 16.04.3 LTS" 
# cat /etc/os-release 
NAME="Ubuntu" 
VERSION="16.04.3 LTS (Xenial Xerus)" 
ID=ubuntu 
ID_LIKE=debian 
PRETTY_NAME="Ubuntu 16.04.3 LTS" 
VERSION_ID="16.04" 
HOME_URL="http://www.ubuntu.com/" 
SUPPORT_URL="http://help.ubuntu.com/" 
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/" 
VERSION_CODENAME=xenial 
UBUNTU_CODENAME=xenial 
# cat /etc/debian_version 
9.3
```
**方法 3： uname 命令**

uname（unix name 的意思） 是一个打印系统信息的工具，包括内核名称、版本号、系统详细信息以及所运行的操作系统等等。

-   建议阅读： 6种查看系统 Linux 内核的方法[1]
```
# uname -a
Linux localhost.localdomain 4.12.14-300.fc26.x86_64 #1 SMP Wed Sep 20 16:28:07 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```
**方法 4： /proc/version 文件**

这个文件记录了 Linux 内核的版本、用于编译内核的 gcc 的版本、内核编译的时间，以及内核编译者的用户名。
```
 # cat /proc/version
 Linux version 4.12.14-300.fc26.x86_64 ([email protected]) (gcc version 7.2.1 20170915 (Red Hat 7.2.1-2) (GCC) ) #1 SMP Wed Sep 20 16:28:07 UTC 2017
```

其他方式参考:
https://os.51cto.com/art/201804/571925.htm

