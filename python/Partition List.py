#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

真丢人，善后工作都忘了做。p2要设为 None！！！

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        small, big = ListNode(0), ListNode(0)
        p0, p1, p = small, big, head
        while p is not None:
            if p.val<x:
                p0.next = p
                p0 = p0.next
            else:
                p1.next = p
                p1 = p1.next
            p = p.next
        p0.next = big.next
        p1.next = None      # important!!! if not, it will generate cycle in the list.
        return small.next
        

if __name__ == '__main__':
    pass
