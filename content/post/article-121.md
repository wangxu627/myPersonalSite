
---
title: parseInt, parseFloat 和 +
date: 2020-03-23 06:29:55.360704
Description: ""
Tags: []
Categories: []
DisableComments: false
---
+,parseInt和parseFloat都可以将字符串转换为数字

比如

    
    
    var a = "1545"  
    +a // 1545  
    parseInt(a) // 1545  
    parseFloat(a) // 1545  
      
    var b = "1545.11"  
    +b // 1545.11  
    parseInt(b) // 1545  
    parseFloat(b) // 1545.11

####  

#### // 不过[]和空字符串就是例外

    
    
    +''                // 0  
    +'   '             // 0  
      
    parseInt('')       // NaN  
    parseInt('   ')    // NaN  
      
    +[]                // 0  
    parseInt([])       // NaN

  


