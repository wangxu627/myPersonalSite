
---
title: 正则表达式匹配所有字符包括换行符\n -正则表达式(1)
date: 2019-12-16 06:37:38.894574
Description: ""
Tags: []
Categories: []
DisableComments: false
---
<https://blog.csdn.net/babybabyup/article/details/81078742>  

# 前言

遇到问题记录下来，免得再次遇到时的尴尬

### 问题描述

今天在做python正则表达式时，要匹配全部内容，包括换行符。无法得到正确答案，已解决。

### 解决方案

`.` 是匹配除过`\n` 之外的全部自符

用`[\d\D]` 匹配所有字符。或者是`[\s\S]` ,


