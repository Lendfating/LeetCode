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
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or head.next is None: return head
        length, p = 1, head
        while p.next is not None:
            length, p = length+1, p.next
        p.next = head   # attach head after trail
        for i in xrange((-k)%length):   # (a*length-k)%length
            p = p.next
        head = p.next
        p.next = None
        return head

if __name__ == '__main__':
    pass
