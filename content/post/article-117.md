
---
title: HTML显示本地或者网络二进制图片方法
date: 2020-02-17 22:36:09.899845
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    <html>  
        <head>  
            <title>Hello</title>  
        </head>  
        <body>  
            <img id="imgobj" style="width:300px;height:300px" ></img>  
            <div id="addarea"></div>  
            <input type="file" onchange="readfile(this.files[0])">  
        </body>  
      
        <script>  
            function readfile(f) {  
                var reader = new FileReader()  
                reader.readAsDataURL(f)  
                reader.onload = function() {  
                    console.log(reader.result)  
                    var url = URL.createObjectURL(f)  
                    console.log(url)  
                    // var imgobj = document.getElementById("imgobj")  
                    imgobj.src = reader.result  
                    imgobj.onload = function() {  
                        URL.revokeObjectURL(imgobj.src)  
                    }  
                }  
            }  
      
            var xhr = new XMLHttpRequest()  
            xhr.open("GET", "http://b-ssl.duitang.com/uploads/item/201808/27/20180827043223_twunu.jpg")  
            xhr.onload = function(e) {  
                var url = URL.createObjectURL(xhr.response)  
                var imgobj = document.getElementById("imgobj")  
                imgobj.src = url  
                imgobj.onload = function() {  
                    URL.revokeObjectURL(imgobj.src)  
                }  
      
                url = URL.createObjectURL(xhr.response)  
                var img = new Image()  
                img.src = url  
                img.onload = function() {  
                    var addarea = document.getElementById("addarea")  
                    addarea.appendChild(img)  
                    URL.revokeObjectURL(img.src)  
                }  
            }  
            xhr.responseType = "blob"  
            xhr.send(null)  
        </script>  
    </html>

  


