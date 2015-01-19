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
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        while cur is not None:
            while cur.next is not None and cur.val==cur.next.val:
                cur = cur.next
            if prev.next==cur:  # use the point of cur! good idea
                # no duplicates for current node
                prev = cur
            else:               # delete current node
                prev.next = cur.next
            cur = cur.next
        return dummy.next
    
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates1(self, head):
        # recursion
        if head is None or head.next is None: return head
        
        if head.val==head.next.val:
            while head.next is not None and head.val==head.next.val:
                head = head.next;
            return self.deleteDuplicates1(head.next)
        else:
            head.next = self.deleteDuplicates1(head.next)
        return head

if __name__ == '__main__':
    pass
