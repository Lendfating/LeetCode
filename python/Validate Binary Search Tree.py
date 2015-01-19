#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

思路有两种：直接递归，查找不匹配的子节点。或中序遍历，挨个检查

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
    def isValidBST(self, root):
        result, min_val, max_val = self.__isValidBST(root)
        return result
    
    def __isValidBST(self, root):
        if root is None: return True, None, None
        
        left, l_min, l_max = self.__isValidBST(root.left)
        if not left or (l_max is not None and l_max>=root.val):
            return False, None, None
        right, r_min, r_max = self.__isValidBST(root.right)
        if not right or (r_min is not None and r_min<=root.val):
            return False, None, None
        min_val = l_min if l_min is not None else root.val
        max_val = r_max if r_max is not None else root.val
        return True, min_val, max_val
    
    # @param root, a tree node
    # @return a boolean
    def isValidBST1(self, root):
        prev, stack, p = TreeNode(-100000000000), [], root
        while len(stack)>0 or p is not None:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if prev.val>=p.val: return False
                prev = p
                p = p.right
        return True

if __name__ == '__main__':
    pass
