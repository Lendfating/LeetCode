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
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        length, p = 0, head
        while p is not None and length<k:
            length, p = length+1, p.next
        if length<k or k<2: return head;
        # reverse the first k nodes from the begining
        last, cur, next = None, head, head.next
        for i in xrange(k):
            next = cur.next
            cur.next = last;
            cur, last = next, cur;
        # reverse the last part of the list
        head.next = self.reverseKGroup(cur, k)
        return last # now 'last' is the new head of the list

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
            
    s = Solution()
    head = init([1,2,3,4,5])
    printList(head)
    head = s.reverseKGroup(head, 2)
    printList(head)
    
