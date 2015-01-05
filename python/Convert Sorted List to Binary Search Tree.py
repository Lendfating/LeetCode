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
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        length, p = 0, head
        while p is not None:
            length, p = length+1, p.next
        return self.buildTree(head, length)
    
    # @param head, a list node
    # @param length, a integer response the length of the list
    # return a tree node
    def buildTree(self, head, length):
        if length==0: return None
        mid, p = (length+1)/2, head
        for i in xrange(1,length+1):
            if i==mid: break;
            p = p.next
        node = TreeNode(p.val)
        node.left = self.buildTree(head, mid-1)
        node.right = self.buildTree(p.next, length-mid)
        return node
    
    # @param head, a list node
    # @return a tree node
    def sortedListToBST1(self, head):
        length, p = 0, head
        while p is not None:
            length, p = length+1, p.next
        node, dump = self.listToBST(head, length)
        return node
    
    # @param head, a list node
    # @param length, a integer response the length of the list
    # return a tree node & next node of list
    def listToBST(self, head, length):
        # take full use of the order to avoid calculate the pointer of mid
        if length==0: return None, head
        node = TreeNode(0)
        node.left, head = self.listToBST(head, length/2)
        node.val = head.val
        node.right, head = self.listToBST(head.next, (length-1)/2)
        return node, head
        
        
if __name__ == '__main__':
    pass
