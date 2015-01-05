#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''

"""
# problem
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# soluction
深度遍历
有负数，不要乱剪枝

"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def initTree(arr):
    if len(arr)==0 or arr[0]=='#':
        return arr[1:], None;
    else:
        root = TreeNode(arr[0]);
        arr, root.left = initTree(arr[1:]);
        arr, root.right = initTree(arr);
        return arr, root;

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None: return False;  # 空节点
        if root.left is None and root.right is None:    # 叶子节点
            return True if root.val==sum else False;
        # 依次递归左右子树
        return self.hasPathSum(root.left, sum-root.val) or\
            self.hasPathSum(root.right, sum-root.val)

if __name__ == '__main__':
    list = [5,4,11,7,'#','#',2,'#','#','#',8,13,'#','#',4,5,'#','#',1];
    list, root = initTree(list);
    s = Solution();
    print s.hasPathSum(root, 22);
    print s.hasPathSum(root, 15);
