
---
title: sql
date: 2020-01-08 15:35:47.538874
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    select fs.code, sum(fs.fx_per) from (select fs.*, row_number() over (partition by fs.code order by fs.date desc) as seq from stocks fs) fs where fs.seq <= 4 group by fs.code;
    
    
    
    
    select fs.code, sum(fs.fx_per) 
    
    from (select fs.*, row_number() over (partition by fs.code order by fs.date desc) as seq 
    
            from stocks fs) fs 
    
    where fs.seq <= 4 
    
    group by fs.code;
    
    
    

  


