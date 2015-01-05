#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
广度优先遍历, 利用循环的思想去遍历即可。基于以构建的上层连接关系，去遍历链接下一层节点

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
        if root is None: return;
        start = root;
        while start.left is not None:    # travel for the depth of the tree
            p = start;
            while p is not None:   # for each node in same leval
                p.left.next = p.right;
                if p.next is not None:
                    p.right.next = p.next.left;
                p = p.next;
            start = start.left;
        
    # @param root, a tree node
    # @return nothing
    def connect1(self, root):
        self.connectNodes(root, None);
    
    def connectNodes(self, root, sibling):
        if root is None: return;
        root.next = sibling;
        self.connectNodes(root.left, root.right);
        if sibling is not None:
            self.connectNodes(root.right, sibling.left);
        else:
            self.connectNodes(root.right, None);    # must exist
        

if __name__ == '__main__':
    pass
