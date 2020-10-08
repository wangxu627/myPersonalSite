
---
title: 使用python检测命令是否存在
date: 2019-12-02 16:35:13.764047
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    import os  
    def check_cmd_avail(cmd):  
        f = os.popen("command -v " + cmd)  
        return f.read() != ""  
      
    print("git:", check_cmd_avail("git"))  
    print("git2:", check_cmd_avail("git2"))  
    print("python:", check_cmd_avail("python"))  
    print("py3:", check_cmd_avail("py3"))  
    print("py4:", check_cmd_avail("py4"))  
    print("flake8", check_cmd_avail("flake8"))

posix下使用command

windows下使用where  


