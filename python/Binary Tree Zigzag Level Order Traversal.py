#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

遍历时仍然从左往右遍历，只是添加结果时根据第几层，决定是正序加入结果还是逆序加入结果。
如果遍历时就分开遍历（从左往右 或 从右往左），那么会遇到一会先左子节点，一会先右子节点的情况，两种情况不统一，不方便统一处理。

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
    def zigzagLevelOrder(self, root):
        result = []
        if root is None: return result
        cur_level_nodes, left_to_right = [root], 1
        while len(cur_level_nodes)>0:
            vals, next_level_nodes = [], []
            for node in cur_level_nodes:
                vals.append(node.val)
                if node.left is not None: next_level_nodes.append(node.left)
                if node.right is not None: next_level_nodes.append(node.right)
            # all values in vals are positive sequence, how to append it into result depend on 'left_to_right'
            result.append(vals if left_to_right else vals[::-1])
            cur_level_nodes = next_level_nodes
            left_to_right ^= 1
        return result

if __name__ == '__main__':
    pass
