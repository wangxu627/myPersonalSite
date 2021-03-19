
---
title: Python获取ip地址
date: 2020-02-07 06:10:06.322040
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    import socket  
    import fcntl  
    import struct  
        
    def get_ip_address(ifname):  
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        return socket.inet_ntoa(fcntl.ioctl(  
            s.fileno(),  
            0x8915,  # SIOCGIFADDR  
            struct.pack('256s', ifname[:15].encode())  
        )[20:24])  
      
    print(get_ip_address('wlp2s0'))

  
  


