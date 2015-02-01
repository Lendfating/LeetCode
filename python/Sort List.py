#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

归并排序很容易，因此归并过程对链表而言实现很简单。
（由于有空间复杂度要求，所以考虑一下非递归实现）
非递归实现无非是从底向上，控制间距去实现。

快排的话，最坏时间复杂度为O(N^2)，依赖于输入，所以一般要加入随机化过程，而LeetCode不支持random模块，故快排是无法通过oj的。


"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        # use merger sort to sort this list
        if head is None or head.next is None: return head
        # Step 1. use two point to find the middle of the list, and split it into two
        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            fast, slow = fast.next.next, slow.next
        p2 = slow.next      # the start of second half
        slow.next = None    # set the end of the first half
        # Step 2. use merger sort in the first half and second half respectively
        p1 = self.sortList(head)
        p2 = self.sortList(p2)
        # Step 3. merger two half part
        dummy = ListNode(0)
        p = dummy
        while p1 is not None and p2 is not None:
            if p1.val<p2.val:
                p.next = p1
                p, p1 = p.next, p1.next
            else:
                p.next = p2
                p, p2 = p.next, p2.next
        if p1 is not None: p.next = p1
        if p2 is not None: p.next = p2
        return dummy.next
    
    # @param head, a ListNode
    # @return a ListNode
    def sortList1(self, head):
        # use merger sort to sort this list。 Iterative implement
        if head is None or head.next is None: return head
        # Step 1. calculate the length of the list
        length, p = 0, head
        while p is not None: length, p = length+1, p.next
        # Step 2. step from 1->2->4...->length, merger each two close pair in each step
        step, dummy = 1, ListNode(0)
        dummy.next = head
        while step<length:
            # Step 2.0 initialize the start state for <cur2>
            last1, cur1, last2, cur2, next2 = dummy, dummy.next, dummy, dummy.next, dummy.next.next
            for i in xrange(step): last2, cur2, next2 = last2.next, cur2.next, next2.next
            last2.next = None
            # Step 2.1 do merger work for each pair <cur1, cur2>
            while True:
                # insert every node in second list into first list
                for i in xrange(step):
                    # find the position for cur2 to insert into
                    while cur1 is not None and cur1.val<cur2.val: last1, cur1 = last1.next, cur1.next
                    # insert cur2 into first list
                    last1.next, cur2.next = cur2, cur1
                    last1, cur2 = last1.next, next2
                    # goto the end of the list
                    if cur2 is None: break
                    next2 = next2.next
                # goto the end of the list
                if cur2 is None: break
                # get next pair of <cur1, cur2>
                while last1.next is not None: last1 = last1.next
                last1.next, cur1, last2 = cur2, cur2, last1
                for i in xrange(step):
                    last2, cur2 = last2.next, cur2.next
                    if cur2 is None: break
                    next2 = next2.next
                # not enough for a pair
                if cur2 is None: break
                last2.next = None
            # Step 2.2 goto next step
            step = step<<1
        return dummy.next
        
    # @param head, a ListNode
    # @return a ListNode
    def sortList2(self, head):
        # use quick sort to sort this list
        if head is None or head.next is None: return head
        # Step 1. split into two part depend on the value
        small, big = ListNode(0), ListNode(0)
        p1, p2, p, val = small, big, head.next, head.val
        while p is not None:
            if p.val<val:
                p1.next = p
                p1, p = p1.next, p.next
            else:
                p2.next = p
                p2, p = p2.next, p.next
        p1.next, p2.next = None, None
        # Step 2. use quick sort for each part
        small.next = self.sortList2(small.next)
        big.next = self.sortList2(big.next)
        # Step 3. merger there parts
        p1 = small
        while p1.next is not None: p1 = p1.next
        p1.next, head.next = head, big.next
        return small.next
            

def gen_list(list):
    dummy = ListNode(0)
    p = dummy
    for val in list:
        p.next = ListNode(val)
        p = p.next
    return dummy.next

if __name__ == '__main__':
    s = Solution()
    print s.sortList1(gen_list([4,19,14,5,-3,1,8,5,11,15]))
