
---
title: python解决排列组合
date: 2019-11-01 03:39:24.931884
Description: ""
Tags: []
Categories: []
DisableComments: false
---
  1. 笛卡尔积：itertools.product(*iterables[, repeat])  

  2. 排列：itertools.permutations(iterable[, r])  

  3. 组合：itertools.combinations(iterable, r)  

  4. 组合（包含自身重复）：itertools.combinations_with_replacement(iterable, r)  

  5. 举例  

### 笛卡尔积：itertools.product(*iterables[, repeat])  
    
    
    import itertools  
    for i in itertools.product('BCDEF', repeat = 2):  
        print(''.join(i),end=",")  
    print('\n')  
       
    # 输出 BB BC BD BE BF CB CC CD CE CF DB DC DD DE DF EB EC ED EE EF FB FC FD FE FF  
    

两个元组进行笛卡尔积：  

    
    
    import itertools  
    a = (1, 2)  
    b = ('A', 'B', 'C')  
    c = itertools.product(a,b)  
    for i in c:  
    print(i,end=",")  
      
    # 输出(1, 'A') (1, 'B') (1, 'C') (2, 'A') (2, 'B') (2, 'C')

### 排列：itertools.permutations(iterable[, r])

    
    
    import itertools  
    for i in itertools.permutations('BCD', 2):  
        print(''.join(i),end=",")  
    # 输出 BC BD CB CD DB DC  
    print('\n')

### 组合：itertools.combinations(iterable, r)

    
    
    import itertools  
    for i in itertools.combinations('BCDEF', 2):  
        print(''.join(i),end=" ")  
    # 输出 BC BD BE BF CD CE CF DE DF EF  
    print('\n')

### 组合（包含自身重复）：itertools.combinations_with_replacement(iterable, r)

    
    
    import itertools  
    for i in itertools.combinations_with_replacement('ABC', 3):  
        print (''.join(i),end=' ')  
       
    # 输出 AAA AAB AAC ABB ABC ACC BBB BBC BCC CCC  
    print('\n')

### 举例

    
    
    'BCDEF五个字母组合问题'  
    import itertools  
       
    print("1个组合：")  
    for i, val in enumerate(list(itertools.combinations('BCDEF', 1))):  
        print("序号：%s   值：%s" % (i + 1, ''.join(val)))  
    print("2个组合：")  
    for i, val in enumerate(list(itertools.combinations('BCDEF', 2))):  
        print("序号：%s   值：%s" % (i + 1, ''.join(val)))  
    print("3个组合：")  
    for i, val in enumerate(list(itertools.combinations('BCDEF', 3))):  
        print("序号：%s   值：%s" % (i + 1, ''.join(val)))  
    print("4个组合：")  
    for i, val in enumerate(list(itertools.combinations('BCDEF', 4))):  
        print("序号：%s   值：%s" % (i + 1, ''.join(val)))  
    print("5个组合：")  
    for i, val in enumerate(list(itertools.combinations('BCDEF', 5))):  
        print("序号：%s   值：%s" % (i + 1, ''.join(val)))

  


