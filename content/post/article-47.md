
---
title: 二叉查找树和堆
date: 2019-10-16 09:04:15.971669
Description: ""
Tags: []
Categories: []
DisableComments: false
---
以前经常弄混淆的两个概念，最近看算法重新复习一下

## 二叉查找树  

二叉查找树（Binary Search
Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的[二叉树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%A0%91/1602879)：

  * 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
  * 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
  * 它的左、右子树也分别为[二叉排序树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%8E%92%E5%BA%8F%E6%A0%91/10905079)。  

![BST](https://img-
blog.csdn.net/20180727201307409?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NzZG4wMTIzemw=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

简单书就是所有左子节点 < 父节点 < 右子节点

在他上面进行查找和二分查找类似

  

##  堆

堆（英语：heap)是计算机科学中一类特殊的数据结构的统称。堆通常是一个可以被看做一棵树的数组对象。堆总是满足下列性质：

  * 堆中某个节点的值总是不大于或不小于其父节点的值；

  * 堆总是一棵完全二叉树。

堆分为两种： _最大堆_ 和 _最小堆_ ，两者的差别在于节点的排序方式。

在最大堆中，父节点的值比每一个子节点的值都要大。在最小堆中，父节点的值比每一个子节点的值都要小。这就是所谓的“堆属性”，并且这个属性对堆中的每一个节点都成立。

![](https://upload-
images.jianshu.io/upload_images/4064751-525f0584ffbdbbed.png?imageMogr2/auto-
orient/strip|imageView2/2/w/219/format/webp)

堆有专门的堆排序

PS：我之前写了个对各种算法的动画图， <https://github.com/wangxu627/canvas-and-sort-anim>  


