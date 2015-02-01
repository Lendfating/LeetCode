#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

方案一：利用hash，比较直接

方案二：利用连标间的表示技巧，从而将空间复杂度降维 O(1).

"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dummy = RandomListNode(0)
        maps, p, last = {}, head, dummy
        while p is not None:
            if not maps.has_key(p):
                maps[p] = RandomListNode(p.label)
            last.next = maps[p]
            last = last.next
            if p.random is not None:
                if not maps.has_key(p.random):
                    maps[p.random] = RandomListNode(p.random.label)
                maps[p].random = maps[p.random]
            p = p.next
        return dummy.next
    
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList1(self, head):
        if head is None: return None
        # clone every node
        p = head
        while p is not None:
            next = RandomListNode(p.label)
            next.next = p.next
            p.next = next
            p = next.next
        # add the random information for every node
        p = head
        while p is not None:
            next = p.next
            if p.random is not None: next.random = p.random.next
            p = next.next
        # re-link two links.
        new_head, p = head.next, head
        while p is not None:
            next = p.next
            p.next = next.next
            p = p.next
            if p is not None: next.next = p.next
        return new_head
    
            

if __name__ == '__main__':
    pass
