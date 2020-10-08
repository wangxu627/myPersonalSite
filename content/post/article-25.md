
---
title: 使用JS的blob对象异步加载图片
date: 2019-07-22 02:02:04.142255
Description: ""
Tags: []
Categories: []
DisableComments: false
---
这个问题是两年前在公司做项目时，角色头像需要从其他服务器异步加载遇到的，当时网上找的解决方案，能用，只是只知其然不知其所以然，最近在看blob对象的文档时，才明白了其中原理

  

    
    
    <html>  
        <head>  
            <title>Hello</title>  
        </head>  
        <body>  
            <img id="imgobj" style="width:300px;height:300px" ></img>  
            <div id="addarea"></div>  
        </body>  
      
        <script>  
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

主要就是URL.createObjectURL和URL.revokeObjectURL两个方法的使用，会在浏览器中创建一个类似mini
server的东西，所以就可以通过一个"虚拟"url来访问图片了

另外如果需要跨域，最好是在服务器用CORS来做，另外这个ajax请求如果用jquery来发送，我这边是不成功的，因为jq对blob的支持有点问题，如果你有解决方案可以请告诉我


