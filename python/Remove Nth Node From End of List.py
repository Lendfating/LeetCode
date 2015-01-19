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
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        prev, last = dummy, dummy
        for i in xrange(n+1):
            prev = prev.next
        while prev is not None:
            prev, last = prev.next, last.next
        last.next = last.next.next
        return dummy.next

if __name__ == '__main__':
    pass
