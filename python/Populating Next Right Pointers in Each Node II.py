#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
注意缺失子树的情况

"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        start = root;
        while start is not None:   # travel the depth
            p, start, end = start, None, None;
            while p is not None:    # for each node in the same leval
                if p.left is not None:
                    if start is None:
                        start = p.left;
                    else:
                        end.next = p.left;
                    end = p.left;       # 连续赋值有问题
                if p.right is not None:
                    if start is None:
                        start = p.right;
                    else:
                        end.next = p.right;
                    end = p.right;
                p = p.next;
                

if __name__ == '__main__':
    root = TreeNode(1);
    root.left = TreeNode(2);
    root.right = TreeNode(3);
    s = Solution();
    s.connect(root)
