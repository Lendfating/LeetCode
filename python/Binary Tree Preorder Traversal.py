#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''

"""
# problem
Given a binary tree, return the preorder traversal of its nodes' values.
Note: Recursive solution is trivial, could you do it iteratively?
Link: https://oj.leetcode.com/problems/binary-tree-preorder-traversal/

# soluction
分递归和非递归两种方法

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
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return [];
        else:
            ret = [root.val];
            ret.extend(self.preorderTraversal(root.left));
            ret.extend(self.preorderTraversal(root.right));
            return ret;
        
    def preorderTraversal1(self, root):
        # 借助栈的非递归实现
        if root is None:
            return [];
        else:
            ret, stack = [root.val], [];
            stack.append(root);
            p = root.left;
            while len(stack)>0 or p is not None:
                while p is not None:
                    ret.append(p.val);
                    stack.append(p);
                    p = p.left;
                if len(stack)>0:
                    p = stack.pop().right;
            return ret;
        
    def preorderTraversal2(self, root):
        # 一个更简单的非递归实现
        ret, stack = [], [];
        if root is not None:
            stack.append(root);
        while len(stack)>0:
            p = stack.pop();
            ret.append(p.val);
            if p.right is not None:
                stack.append(p.right);
            if p.left is not None:
                stack.append(p.left);
        return ret;

if __name__ == '__main__':
    arr = [1,'#',2,3];
    arr, root = initTree(arr);
    s = Solution();
    print s.preorderTraversal(root)
    print s.preorderTraversal1(root)
    print s.preorderTraversal2(root)
