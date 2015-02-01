#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

非递归版本，两个思路
思路一：利用前序遍历，最终链表的顺序其实是原二叉树的前序遍历结果
思路二：利用Mirror 思想，访问某个结点时查看其前向节点，然后将前向节点（中序）的right指向当前节点的右子节点。

递归的思路还是都是利用了该链化结果是原二叉树的前序遍历这一结论。
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None: return None
        stack = [root]
        while len(stack)>0:
            p = stack.pop()
            if p.right is not None: stack.append(p.right)
            if p.left is not None: stack.append(p.left)
            # visit p here
            p.left = None
            if len(stack)>0: p.right = stack[-1]
        
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten1(self, root):
        while root is not None:
            if root.left is not None:
                # find the prior node of current node, and attach cur.right to prior.right
                prior = root.left
                while prior.right is not None: prior = prior.right
                prior.right = root.right
                # attach current's left to current's right
                root.left, root.right = None, root.left
            # visit next node
            root = root.right
            
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten2(self, root):
        self.__flatten(root, None)
        
    def __flatten(self, root, tail):
        if root is None: return tail
        root.right = self.__flatten(root.left, self.__flatten(root.right, tail))
        root.left = None
        return root

if __name__ == '__main__':
    pass
