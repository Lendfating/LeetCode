#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''

"""
# problem
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, 
only nodes itself can be changed.
Link: https://oj.leetcode.com/problems/swap-nodes-in-pairs/

# soluction

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        hyst = dump = ListNode(0);  # hyst表示滞后一个node
        hyst.next = head;
        p1 = hyst.next;
        while p1 is not None:
            p2 = p1.next;
            if p2 is not None: # swap pairs
                hyst.next = p2;
                p1.next = p2.next;
                p2.next = p1;
                hyst = p1;
                p1 = hyst.next;
            else:
                break;
        return dump.next;
            
def initList(arr):
    p = dump = ListNode(0);
    for item in arr:
        p.next = ListNode(item);
        p = p.next;
    return dump.next;

if __name__ == '__main__':
    list = initList([1,2,3,4])
    s = Solution();
    p = s.swapPairs(list);
    while p is not None:
        print p.val
        p = p.next;
