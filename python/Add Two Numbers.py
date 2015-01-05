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
    def addTwoNumbers(self, l1, l2):
        if l1 is None: return l2
        dump = ListNode(0)
        p, p1, p2, carry = dump, l1, l2, 0
        while p1 is not None and p2 is not None:
            carry, p.next = (p1.val+p2.val+carry)/10, ListNode((p1.val+p2.val+carry)%10)
            p, p1, p2 = p.next, p1.next, p2.next
        if p1 is not None:
            while p1 is not None and carry != 0:
                carry, p.next = (p1.val+carry)/10, ListNode((p1.val+carry)%10)
                p, p1 = p.next, p1.next
            p.next = p1
        elif p2 is not None:
            while p2 is not None and carry != 0:
                carry, p.next = (p2.val+carry)/10, ListNode((p2.val+carry)%10)
                p, p2 = p.next, p2.next
            p.next = p2
        if carry != 0:
            p.next = ListNode(carry)
        return dump.next

    # @return a ListNode
    def addTwoNumbers1(self, l1, l2):
        dump = ListNode(0)
        p, p1, p2, sum = dump, l1, l2, 0
        while p1 is not None or p2 is not None or sum!=0:
            sum += (p1.val if p1 is not None else 0) + (p2.val if p2 is not None else 0)
            p.next = ListNode(sum%10)
            sum /= 10
            p = p.next
            p1 = p1.next if p1 is not None else None
            p2 = p2.next if p2 is not None else None
        return dump.next

if __name__ == '__main__':
    pass
