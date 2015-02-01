#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        
    # @param root, a tree node
    # @return an integer
    def maxDepth1(self, root):
        if root is None: return 0
        level, cur_level_nodes = 0, [root]
        while len(cur_level_nodes)>0:
            next_level_nodes = []
            for node in cur_level_nodes:
                if node.left is not None: next_level_nodes.append(node.left)
                if node.right is not None: next_level_nodes.append(node.right)
            level, cur_level_nodes = level+1, next_level_nodes
        return level

if __name__ == '__main__':
    pass
