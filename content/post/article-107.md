
---
title: python补码转换
date: 2020-02-03 03:50:59.322049
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    def convert2bin(val, bits):  
        if val < 0:  
            return bin(((1 << bits) - 1) & (val))  
        else:  
            return '0b' + format(val, '0' + str(bits) + 'b')

  
  


