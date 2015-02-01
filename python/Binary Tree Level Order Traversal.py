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
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if root is None: return result
        cur_level_nodes = [root]
        while len(cur_level_nodes)>0:
            vals, next_level_nodes = [], []
            for node in cur_level_nodes:
                vals.append(node.val)
                if node.left is not None: next_level_nodes.append(node.left)
                if node.right is not None: next_level_nodes.append(node.right)
            result.append(vals)
            cur_level_nodes = next_level_nodes
        return result
        

if __name__ == '__main__':
    pass
