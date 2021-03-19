
---
title: Git每次都要求输入密码
date: 2020-05-28 06:43:43.455261
Description: ""
Tags: []
Categories: []
DisableComments: false
---
<https://stackoverflow.com/questions/11403407/git-asks-for-username-every-
time-i-push>  

  

 _Edit (by @dk14 as suggested by moderators and comments)_

 **WARNING: If you use  `credential.helper store` from the answer, your
password is going to be stored completely unencrypted ("as is") at `~/.git-
credentials`. Please consult the comments section below or the answers from
the "Linked" section, especially if your employer has zero tolerance for
security issues.**

Even though accepted, it doesn't answer the actual OP's question about
omitting a username only (not password). For the readers with that exact
problem @grawity's [answer](https://superuser.com/questions/847181/skip-
username-prompt-when-using-git) might come in handy.

* * *

 **Original answer (by @Alexander Zhu):**

You can store your credentials using the following command

    
    
    $ git config credential.helper store
    $ git push http://example.com/repo.git
    Username: <type your username>
    Password: <type your password>
    

Also I suggest you to read  
[`$ git help credentials`](https://git-scm.com/docs/gitcredentials)


