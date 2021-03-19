
---
title: 二叉树遍历的几种递归和非递归方式
date: 2019-11-15 14:05:35.935693
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    from collections import namedtuple  
      
    Node = namedtuple("Node", ["value", "left", "right"])  
      
    def create_tree():  
        p4 = Node(4, None, None)  
        p5 = Node(5, None, None)  
        p2 = Node(2, p4, p5)  
        p6 = Node(6, None, None)  
        p3 = Node(3, None, p6)  
        p1 = Node(1, p2, p3)  
        return p1  
      
    def visit_recursion_pre_order(node):  
        if(node):  
            print(node.value)  
            visit_recursion_pre_order(node.left)  
            visit_recursion_pre_order(node.right)  
      
    def visit_norecursion_pre_order(root):  
        if(not root):  
            return  
        stack = []  
        stack.append(root)  
        while(len(stack) > 0):  
            cur = stack.pop()  
            print(cur.value)  
            if(cur.right):  
                stack.append(cur.right)  
            if(cur.left):  
                stack.append(cur.left)  
      
    def visit_recursion_in_order(node):  
        if(node):  
            visit_recursion_in_order(node.left)  
            print(node.value)  
            visit_recursion_in_order(node.right)  
      
    def visit_norecursion_in_order(root):  
        if(not root):  
            return  
        visited = set()  
        stack = []  
        stack.append(root)  
        while(len(stack) > 0):  
            cur = stack[-1]  
            while(cur.left and cur.left not in visited):  
                visited.add(cur.left)  
                stack.append(cur.left)  
                cur = cur.left  
            print(cur.value)  
            stack.pop()  
            if(cur.right):  
                stack.append(cur.right)  
      
    def visit_recursion_post_order(node):  
        if(node):  
            visit_recursion_post_order(node.left)  
            visit_recursion_post_order(node.right)  
            print(node.value)  
      
    def visit_norecursion_post_order(root):  
        if(not root):  
            return  
        visited = set()  
        stack = []  
        stack.append(root)  
        while(len(stack) > 0):  
            cur = stack[-1]  
            if(cur.right and cur.right not in visited):  
                stack.append(cur.right)  
            if(cur.left and cur.left not in visited):  
                stack.append(cur.left)  
      
            if((cur.left is None or cur.left in visited) and   
               (cur.right is None or cur.right in visited)):  
                print(cur.value)  
                visited.add(cur)  
                stack.pop()  
      
    if __name__ == "__main__":  
        root = create_tree()  
        visit_recursion_pre_order(root)  
        print("=" * 10)  
        visit_norecursion_pre_order(root)  
        print("=" * 10)  
        visit_recursion_in_order(root)  
        print("=" * 10)  
        visit_norecursion_in_order(root)  
        print("=" * 10)  
        visit_recursion_post_order(root)  
        print("=" * 10)  
        visit_norecursion_post_order(root)

  


