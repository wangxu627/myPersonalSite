
---
title: 快排简单实现
date: 2019-11-05 02:34:47.631532
Description: ""
Tags: []
Categories: []
DisableComments: false
---
版本1：

    
    
    def partition(arr, l, r):  
        pivot = arr[l]  
        while(l < r):  
            while(l < r and arr[r] >= pivot):  
                r -= 1  
            arr[r], arr[l] = arr[l], arr[r]  
            while(l < r and arr[l] <= pivot):  
                l += 1  
            arr[l], arr[r] = arr[r], arr[l]  
          
        return l  
      
    def qsort(arr, l, r):  
        if(l < r):  
            idx = partition(arr, l, r)  
            qsort(arr, l, idx - 1)  
            qsort(arr, idx + 1, r)

版本2：

    
    
    def quicksort(array):  
            less = []  
            greater = []  
            if len(array) <= 1:  
                    return array  
            pivot = array.pop()  
            for x in array:  
                    if x <= pivot:  
                            less.append(x)  
                    else:  
                            greater.append(x)  
            return quicksort(less) + [pivot] + quicksort(greater)

  


