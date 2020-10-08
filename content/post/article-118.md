
---
title: Vscode调试python代码时进入library function的设置
date: 2020-02-26 00:43:12.160370
Description: ""
Tags: []
Categories: []
DisableComments: false
---
<https://stackoverflow.com/questions/53594900/visual-studio-code-python-
debugging-step-into-the-code-of-external-functions>  

  

    
    
    {  
        // Use IntelliSense to learn about possible attributes.  
        // Hover to view descriptions of existing attributes.  
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387  
        "version": "0.2.0",  
        "configurations": [  
            {  
                "name": "Python: Current File",  
                "type": "python",  
                "request": "launch",  
                "program": "${file}",  
                "console": "integratedTerminal",  
                "justMyCode": false # IMPORTANT  
            }  
        ]  
    }

  


