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
    def sumNumbers(self, root):
        return self.__sumNumbers(root, 0)
        
    def __sumNumbers(self, root, numbers):
        if root is None: return 0
        numbers = numbers*10 + root.val
        # leaf node
        if root.left is None and root.right is None:
            return numbers
        return self.__sumNumbers(root.left, numbers) + \
                self.__sumNumbers(root.right, numbers)

if __name__ == '__main__':
    pass
