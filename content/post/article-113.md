
---
title: tampermonkey匹配所有网站,自定义按键
date: 2020-02-11 04:16:55.628525
Description: ""
Tags: []
Categories: []
DisableComments: false
---
最重要的一行

// @include /^https?\:\/\/.*.*\\..*\/.*$/

参考：

<https://stackoverflow.com/questions/20462544/greasemonkey-tampermonkey-match-
for-a-page-with-parameters>  

    
    
    // ==UserScript==  
    // @name         Custom Button  
    // @namespace    http://tampermonkey.net/  
    // @version      0.1  
    // @description  try to take over the world!  
    // @author       You  
    // @include      /^https?\:\/\/.*.*\..*\/.*$/  
    // @grant        none  
    // ==/UserScript==  
      
    (function() {  
        'use strict';  
        function clickMeHandler() {  
            alert("Hello");  
        }  
        window.clickMeHandler = clickMeHandler;  
      
        var div = document.createElement("div");  
        var divStr = `<div style="position:fixed; top:20px; left: 20px;">  
            <input type="button" value="Click Me" onclick="clickMeHandler();"></input>  
        </div>`  
        div.innerHTML = divStr;  
        document.body.appendChild(div.firstChild);  
        // Your code here...  
    })();

  


