
---
title: PyCharm Community和Vscode配置flask调试
date: 2020-01-20 05:10:25.672015
Description: ""
Tags: []
Categories: []
DisableComments: false
---
# PyCharm Community

1\. Templates用Python

2.Scripts选择到虚拟或全局环境的flask文件，我这里是/home/dnacd/.local/share/virtualenvs/python-
api-template-PGOq6p85/bin/flask

3.Parameters补齐剩下命令，比如 flask run --host XXX.XXX.XXX.XXX --port 22222

4.Environment variables： FLASK_APP=application;FLASK_ENV=development

![](http://image.wxioi.com/0e8108cbb6e23aa4f985767cedc2c4c4.png)  

# VsCode

    
    
    {  
        // Use IntelliSense to learn about possible attributes.  
        // Hover to view descriptions of existing attributes.  
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387  
        "version": "0.2.0",  
        "configurations": [  
            {  
                "name": "Python: Flask",  
                "type": "python",  
                "request": "launch",  
                "module": "flask",  
                "env": {  
                    "FLASK_APP": "application",  
                    "FLASK_ENV": "development",  
                    "FLASK_DEBUG": "1"  
                },  
                "args": [  
                    "run",  
                    "--no-debugger",  
                    "--no-reload"  
                ],  
                "jinja": true  
            }  
        ]  
    }

![](http://image.wxioi.com/cf9f0eb14e4a12585585ddf25850a953.png)  


