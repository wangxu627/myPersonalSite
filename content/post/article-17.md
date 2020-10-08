
---
title: Python中用requests上传文件
date: 2019-07-14 03:30:42.001395
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    files = {  
        "file":open(path,"rb")  
    }  
    param = {  
        "enctype":"multipart/form-data",  
        "key": path,  
        "Signature": data["authorization"],  
        "x-cos-security-token":data["token"],  
        "x-cos-meta-fileid":data["cos_file_id"]  
    }  
    reponse = requests.post(data["url"], data=param, files=files)

目前只知道用requests来发送，用python自带的urllib.requests发送multipart/form-data文件是有点问题，后续解决


