#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        h = ListNode(0)
        h.next = head
        p, last, p_m, p_n = head, h, None, None
        for index in range(1, n+1):
            if index==m: p_m = p
            if index==n: p_n = p
            if index>=m:    # reverse
                next = p.next
                p.next = last
                p, last = next, p
            else:
                p, last = p.next, p
        p_m.next.next = p_n
        p_m.next = p
        return h.next

if __name__ == '__main__':
    def init(list):
        if len(list)==0: return None;
        head = p = ListNode(list[0])
        for i in xrange(1, len(list)):
            p.next = ListNode(list[i])
            p = p.next;
        return head
    
    def printList(p):
        while p is not None:
            print p.val
            p = p.next
    
    s= Solution()
    head = init([1,2,3,4,5])
    printList(head)
    head = s.reverseBetween(head, 2, 4)
    printList(head)
