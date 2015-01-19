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
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None: return head
        p = head
        while p.next is not None:   # p will never be None.
            if p.val==p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

if __name__ == '__main__':
    pass
