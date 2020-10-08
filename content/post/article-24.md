
---
title: 使用flask或nginx实现动态反向代理
date: 2019-07-21 12:01:10.509701
Description: ""
Tags: []
Categories: []
DisableComments: false
---
之前做小程序有一个需求，在小程序中访问其他网站的图片，会因为防盗链等机制无法访问，简单的解决方案就是通过nginx配置反向代理

    
    
        server {  
            listen       8900;  
            server_name  localhost;  
            location / {  
                proxy_pass http://a.target_host.con/;  
                add_header Access-Control-Allow-Origin *;  
            }  
            error_page   500 502 503 504  /50x.html;  
            location = /50x.html {  
                root   html;  
            }  
        }

但如果需要代理的服务器很多，一个一个配置就不太现实了，一开始想到的方案是用正则修改链接为如下形式

    
    
    http://a.target_host.com/image2019/07/20190719_ls_red_141_1/12small_24_20197191455347.jpg  
    # 把目标主机的地址放到新的链接的get参数里面，然后将链接定向到自己的服务器  
    http://a.my_host.com:8900/image2019/07/20190719_ls_red_141_1/12small_24_20197191455347.jpg?host=http://a.target_host.com/

然后用flask写了一个代理

    
    
    import urllib.request  
    from flask import Flask, request, make_response  
      
    app = Flask(__name__)  
      
    @app.route('/<path:path>')  
    def hello(path):  
        host = request.args.get("host")  
        try:  
            url = host + path  
            response = make_response(urllib.request.urlopen(url).read())  
            response.headers['Content-Type'] = 'image/jpeg'  
            return response  
        except:  
            return ""  
      
    if __name__ == '__main__':  
        app.run(host='0.0.0.0', port=8900)

测试基本可用，不过flask的性能即放到wsgi和nginx上也可能比较慢，另外可以试试sanic，不过目前就这样

最后还是由于性能原因，另外google了一下，发现nginx也是可以做到的，所以决定还是改用nginx直接实现

    
    
    server {  
            listen       8900;  
            server_name  localhost;  
            # 这一行很重要  
            resolver     8.8.8.8;  
            location / {
                proxy_set_header referer "";
                if ($query_string ~* "host=(.+)/$") {  
                    set $replace_host $1;  
                    proxy_pass $replace_host;  
                    add_header Access-Control-Allow-Origin *;  
                }  
            }  
            error_page   500 502 503 504  /50x.html;  
            location = /50x.html {  
                root   html;  
            }  
        }

resolver 8.8.8.8;

这一行是必须要加上的，不然nginx会报no resolver defined to resolve
XXXX的错，至于为啥是8.8.8.8，我也不知啊都啊。。。。

基本流程就是这样

  


