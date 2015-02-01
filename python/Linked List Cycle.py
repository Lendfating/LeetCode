#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        p1, p2 = head, head
        # p1 skip one node every step, while p2 skip two nodes
        while p2 is not None and p2.next is not None:
            p1, p2 = p1.next, p2.next.next
            if p1==p2: return True
        return False
            

if __name__ == '__main__':
    pass
