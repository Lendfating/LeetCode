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
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        p, p1, p2 = dummy, l1, l2
        while p1 is not None and p2 is not None:
            if p1.val<p2.val:
                p.next = p1
                p, p1 = p.next, p1.next
            else:
                p.next = p2
                p, p2 = p.next, p2.next
        p.next = p1 if p1 is not None else p2
        return dummy.next

if __name__ == '__main__':
    pass
