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
    def minDepth(self, root):
        if root is None: return 0
        level, cur_level_nodes = 0, [root]
        while len(cur_level_nodes)>0:
            level, next_level_nodes = level+1, []
            for node in cur_level_nodes:
                if node.left is None and node.right is None: return level
                if node.left is not None: next_level_nodes.append(node.left)
                if node.right is not None: next_level_nodes.append(node.right)
            cur_level_nodes = next_level_nodes
        return level
    

if __name__ == '__main__':
    pass
