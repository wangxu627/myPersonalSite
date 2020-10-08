
---
title: JS代码给element发送事件
date: 2020-03-23 07:04:49.355329
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    var elem = document.getElementById("add_tag");  
    var event = new MouseEvent("mousedown", {view: window, bubbles: true, cancelable: true});  
    elem.dispatchEvent(event)

感觉不好用，代码可以检查event的isTrusted字段，从而做到完全忽略代码发送的事件

  

    
    
    var event = new FocusEvent("focus", {  
            view: window,  
            bubbles: false,  
            cancelable: false  
          });  
          this.searchInputElement.nativeElement.dispatchEvent(event);

  


