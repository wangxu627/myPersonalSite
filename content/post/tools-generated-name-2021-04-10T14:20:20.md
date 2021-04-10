---
title: "Use netsh to forward port to WSL"
date: 2021-04-10T14:20:20
Description: ""
Tags: []
Categories: []
DisableComments: false
---
It's not a bug with WSL 2, WSL 2 is running as a hyper-v virtual machine. The hyper-v adapter can be found in network adapters. You can use port forwarding to forward the port with netsh as below.  
Example command below will forward tcp from port 3000 of the WSL 2 client to port 3000 of the host OS.  
## IMPORTANT
`netsh interface portproxy add v4tov4 listenport=3000 listenaddress=0.0.0.0 connectport=3000 connectaddress=172.18.28.x`  

Next allow incoming and outgoing ports on port 3000 in firewall.

