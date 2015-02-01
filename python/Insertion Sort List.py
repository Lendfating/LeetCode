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
    def insertionSortList(self, head):
        dummy, p = ListNode(0), head
        # do insert operation for each node in the list
        while p is not None:
            # find the position where p should be inserted into
            last, cur = dummy, dummy.next
            while cur is not None and cur.val<p.val:
                last, cur = last.next, cur.next
            # insert p here.
            next = p.next
            last.next, p.next = p, cur
            p = next
        return dummy.next

if __name__ == '__main__':
    pass
