#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

除了常规的递归和利用栈迭代的方式，还有一个Morris的遍历方法。时间复杂度为O(n)空间复杂度O(1).

证明时间复杂度时，考虑每条边最多走两遍。

http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result, stack, p = [], [], root
        while len(stack)>0 or p is not None:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                result.append(p.val)
                p = p.right
        return result
         
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal1(self, root):
        # use morris method. use Successor link to make tree linked
        result, p = [], root
        while p is not None:
            if p.left is None:
                result.append(p.val)
                p = p.right
            else:   # find the prior node of p
                prior = p.left
                while prior.right is not None and prior.right!=p:
                    prior = prior.right
                if prior.right is None:
                    # have not link it, so it's the first time visit its left sub-tree
                    prior.right = p # link it
                    p = p.left      # start to visit its left sub-tree
                else:
                    # we have linked it, so we have visited its left sub-tree.
                    prior.right = None
                    result.append(p.val)    # visit it
                    p = p.right     # start to visit its right sub-tree
        return result
                    
              
        

if __name__ == '__main__':
    pass
