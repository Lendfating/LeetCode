#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

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
    # @return an integer
    def maxPathSum(self, root):
        mps, dummy = self.calculatePathSum(root);
        return mps;
    
    # @param root, a tree node
    # @return two integer, indicating max path sum and max root to leaf path sum
    def calculatePathSum(self, root):
        if root is None: return -1000000000, 0;
        l_tmps, l_omps = self.calculatePathSum(root.left);
        r_tmps, r_omps = self.calculatePathSum(root.right);
        return max(l_tmps, r_tmps, max(l_omps,0) + root.val + max(r_omps,0)), max(l_omps, r_omps, 0)+root.val

if __name__ == '__main__':
    arr = [1,'#',2,3];
    arr, root = initTree(arr);
    s = Solution();
    print s.maxPathSum(root)
