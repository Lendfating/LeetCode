#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

二叉搜索树，中序遍历即为最小到最大的排列，即原题要求按中序遍历的结果依次输出每一个值。

将遍历的过程拆分开来放到 hasNext()和next()里面即可。

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        # use in-order traversal, and stay at any state where next node will be output
        self.stack = []
        self.cur = root

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.cur is not None or len(self.stack)>0

    # @return an integer, the next smallest number
    def next(self):
        while self.cur is not None:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        node = self.stack.pop()
        self.cur = node.right
        return node.val
        
        
class BSTIterator1:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        # use in-order traversal, and stay at any state where next node will be output
        self.cur = root

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.cur is not None

    # @return an integer, the next smallest number
    def next(self):
        val = -1
        while self.cur is not None:
            if self.cur.left is None:
                val = self.cur.val
                self.cur = self.cur.right
                break
            else:
                prior = self.cur.left
                while prior.right is not None and prior.right!=self.cur:
                    prior = prior.right
                if prior.right is None:
                    prior.right = self.cur
                    self.cur = self.cur.left
                else:
                    prior.right = None
                    val = self.cur.val
                    self.cur = self.cur.right
                    break
        return val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    pass
