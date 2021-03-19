
---
title: Python动态规划计算背包问题
date: 2019-11-05 02:51:12.986998
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    '''假设你去伦敦度假，假期2天，但你想去浏览的地方很多。你没法前往每个地方浏览，因此你列了个单子  
    |名胜               |时间       |评分  
    威斯敏斯特教堂       0.5天       7  
    环球剧场             0.5天       6  
    英国国家美术馆       1天         9  
    大英博物馆           2天         9  
    圣保罗大教堂         0.5天       8  
      
    如何让评分最高？  
    '''  
      
    from functools import namedtuple  
      
    TravelItem = namedtuple('TravelItem', ["name", "time", "value"])  
    # TableItem = namedtuple('TableItem', ['path', 'total'])  
      
    class TableItem:  
        def __init__(self, path, total):  
            self.path = path  
            self.total = total  
      
        def __repr__(self):  
            return "({}):{}".format("".join(str(n) for n in self.path), self.total)  
      
    items = [  
        TravelItem('W', 0.5, 7),  
        TravelItem('G', 0.5, 6),   
        TravelItem('N', 1, 9),   
        TravelItem('B', 2, 9),   
        TravelItem('S', 0.5, 8),   
    ]  
      
    days = 2  
      
    rows = 5  
    columns = 4  
    table = [[TableItem([], 0) for i in range(4)] for i in range(5)]  
      
    def get_value(table, i, j):  
        if(i < 0 or i >= len(table)):  
            return 0  
        if(j < 0 or j >= len(table[0])):  
            return 0  
        return table[int(i)][int(j)].total  
      
      
    for i in range(rows):  
        for j in range(columns):  
            if(j - int(items[i].time * 2 - 1) < 0):  
                table[i][j].total = get_value(table, i - 1, j)  
                table[i][j].path = table[i - 1][j].path[:]  
            else:  
                table[i][j].total = max(get_value(table, i - 1, j - items[i].time * 2) + items[i].value, get_value(table, i - 1, j))  
                if((get_value(table, i - 1, j - items[i].time * 2) + items[i].value) > get_value(table, i - 1, j)):  
                    if(j - 1 >= 0):  
                        table[i][j].path = table[i - 1][int(j - items[i].time * 2)].path[:]  
                    table[i][j].path.append(items[i].name)  
                      
                else:  
                    table[i][j].path = table[i - 1][j].path[:]  
      
    print(table)

  


