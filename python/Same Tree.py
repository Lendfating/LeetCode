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

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None: return True;
        return p is not None and q is not None and p.val==q.val \
            and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right);

    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree1(self, p, q):
        if p is None or q is None: return p==q;
        return p.val==q.val and self.isSameTree1(p.left, q.left) and self.isSameTree1(p.right, q.right)

if __name__ == '__main__':
    pass
