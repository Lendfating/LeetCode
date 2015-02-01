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
    # @return a boolean
    def isBalanced(self, root):
        balance, depth = self.__isBalanced(root)
        return balance
    
    def __isBalanced(self, root):
        if root is None: return True, 0
        left_balance, left_depth = self.__isBalanced(root.left)
        if not left_balance: return False, 0
        right_balance, right_depth = self.__isBalanced(root.right)
        return right_balance and abs(left_depth-right_depth)<2, max(left_depth, right_depth)+1

if __name__ == '__main__':
    pass
