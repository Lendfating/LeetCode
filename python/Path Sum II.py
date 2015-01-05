#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''

"""
# problem
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Link: https://oj.leetcode.com/problems/path-sum-ii/

# soluction
深度优先遍历. 可以递归实现，如果用非递归的话，因为需要维护路径和信息，涉及到和的恢复，故应该采用后续遍历。

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
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None:    # 空白结点
            return [];
        if root.left is None and root.right is None:    # 叶子结点
            return [[sum]] if root.val == sum else [];
        ret = [];
        ret.extend(self.pathSum(root.left, sum-root.val));  # 左子树递归
        ret.extend(self.pathSum(root.right, sum-root.val)); # 右子树递归
        for i in xrange(len(ret)):  # 插入当前结点信息
            ret[i].insert(0, root.val);
        return ret;           
        

if __name__ == '__main__':
    list = [5,4,11,7,'#','#',2,'#','#','#',8,13,'#','#',4,5,'#','#',1];
    list, root = initTree(list);
    s = Solution();
    print s.pathSum(root, 22);
