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
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None: return ;
        # Step 1. find the mid node using two pointer
        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            # the end point of the loop is important, must stop at the end of first half.
            fast, slow = fast.next.next, slow.next
        # Step 2. reverse the second half of the list
        last, cur, trail_list = None, slow.next, None
        slow.next = None    # make the end of the first half to None
        while cur is not None:
            next = cur.next
            cur.next = last
            last = cur
            trail_list = cur
            cur = next
        # Step 3. insert the last half node into the first half
        cur, head_list = head, head.next
        while trail_list is not None:
            cur.next = trail_list
            cur, trail_list = cur.next, trail_list.next
            cur.next = head_list
            cur = cur.next
            if head_list is not None: head_list = head_list.next
        
        

if __name__ == '__main__':
    pass
