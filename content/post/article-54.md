
---
title: Git Push错误&无法查看push后的git中文件
date: 2019-10-28 17:31:39.966040
Description: ""
Tags: []
Categories: []
DisableComments: false
---
原文链接地址：  
http://blog.csdn.net/wby0322/archive/2010/10/14/5940018.aspx



在使用Git Push代码到数据仓库时，提示如下错误:

[remote rejected] master -> master (branch is currently checked out)

错误原型

remote: error: refusing to update checked out branch: refs/heads/master

remote: error: By default, updating the current branch in a non-bare
repository

remote: error: is denied, because it will make the index and work tree
inconsistent

remote: error: with what you pushed, and will require 'git reset --hard' to
match

remote: error: the work tree to HEAD.

remote: error:

remote: error: You can set 'receive.denyCurrentBranch' configuration variable
to

remote: error: 'ignore' or 'warn' in the remote repository to allow pushing
into

remote: error: its current branch; however, this is not recommended unless you

remote: error: arranged to update its work tree to match what you pushed in
some

remote: error: other way.

remote: error:

remote: error: To squelch this message and still keep the default behaviour,
set

remote: error: 'receive.denyCurrentBranch' configuration variable to 'refuse'.

To git@192.168.1.X:/var/git.server/.../web

 ! [remote rejected] master -> master (branch is currently checked out)

error: failed to push some refs to 'git@192.168.1.X:/var/git.server/.../web'

错误原因以及解决

这是由于git默认拒绝了push操作，需要进行设置，修改.git/config文件后面添加如下代码：

[receive]

denyCurrentBranch = ignore

无法查看push后的git中文件的原因与解决方法

在初始化远程仓库时最好使用 git --bare init   而不要使用：git init

如果使用了git init初始化，则远程仓库的目录下，也包含work tree，当本地仓库向远程仓库push时,
如果远程仓库正在push的分支上（如果当时不在push的分支，就没有问题）, 那么push后的结果不会反应在work tree上,
也即在远程仓库的目录下对应的文件还是之前的内容。

解决方法：

必须得使用命令 git reset --hard 才能看到push后的内容.


