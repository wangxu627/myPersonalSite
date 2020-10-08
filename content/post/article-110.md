
---
title: Python functools之cmp_to_key
date: 2020-02-09 06:51:53.656624
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    from functools import cmp_to_key  
      
    def cmp_new(x,y):  
        sx = str(x)  
        sy = str(y)  
        if(sx + sy > sy + sx):  
            return 1  
        elif(sx + sy < sy + sx):  
            return -1  
        else:  
            return 0  
      
    def print_min_number(arr):  
        arr.sort(key=cmp_to_key(cmp_new))  
        return "".join(str(n) for n in arr)  
      
      
    l = [3,32,321]  
    print(print_min_number(l))

  


