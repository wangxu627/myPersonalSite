
---
title: 讲长数字格式化成带逗号的字符串
date: 2020-03-23 06:59:59.063060
Description: ""
Tags: []
Categories: []
DisableComments: false
---
python:

    
    
    Locale unaware  
    '{:,}'.format(value)  # For Python ≥2.7  
    f'{value:,}'  # For Python ≥3.6
    
    Locale aware  
    import locale  
    locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'  
      
    '{:n}'.format(value)  # For Python ≥2.7  
    f'{value:n}'  # For Python ≥3.6

JS:

    
    
    function numberWithCommas(x) {  
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");  
    }

PS:JS版本用正则来处理,小数点后面的数字也会格式化，一般情况是讲小数点后的数字保留N位并不加逗号


