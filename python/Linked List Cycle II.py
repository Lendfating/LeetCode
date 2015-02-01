#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

fast 速度是 slow的2倍，假设到交点时slow走了 s 步，则fast 走了2s步。也就是fast在环上又走了s步。
此时，我们新定义一个指针 entry从head开始，走slow走过的路，让slow继续走fast多走的那部分路，则这两个指针最终
还会在s步之后相交于这个交点。而且，这两个指针第一次相遇的点即为环的入口。（倒推即可推出）

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        faster, slower = head, head
        # slower move one node each step, while faster move two
        while faster is not None and faster.next is not None:
            slower, faster = slower.next, faster.next.next
            if faster==slower: break
        else:
            return None     # no cycle in this list
        # the distance from join node to join node = the distance from start to join node
        # because the speed of faster is twice of slower.
        p1, p2 = head, slower
        # from head and join node to move, the first same node is the cycle begin.
        while p1!=p2:
            p1, p2 = p1.next, p2.next
        return p1
    
    # @param head, a ListNode
    # @return a list node
    def detectCycle1(self, head):
        fast, slow = head, head
        # slow move one node each step, while fast move two
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next
            if fast==slow:      # there is a cycle
                entry = head
                while entry!=slow: entry, slow = entry.next, slow.next
                return entry
        return None # there is no cycle

if __name__ == '__main__':
    pass
