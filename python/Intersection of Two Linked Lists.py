#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

方案有两种：
方案一：计算两个链表的长度，然后长的先走一段，使两者到终点的距离相同，这样，在两个一起移动，在移动的同时进行判断。
方案二：利用 len_A+len_B == len_B+len_A, p_A先遍历A，再遍历B，p_B先遍历B，再遍历A。这样两个指针一定会在第二轮是相遇。

还有一个很异类，很牛逼的解决方法，把list A里面的所有next指针值的最低位设为 1，然后在list2中判断当前这个node的next指针的低位
是否为1，据此判断交点位置。太牛逼了，利用指针最低位不会出现1这个性质，然后用此来标记那个对象已访问过。（最后当然会恢复一下）

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        # Step 1. calculate the length of each list
        len_A, len_B, p_A, p_B = 0, 0, headA, headB
        while p_A is not None: len_A, p_A = len_A+1, p_A.next
        while p_B is not None: len_B, p_B = len_B+1, p_B.next
        # Step 2. move the start pointer of longer list, so they will have same step to end.
        p_A, p_B = headA, headB
        for i in xrange(len_A-len_B): p_A = p_A.next
        for i in xrange(len_B-len_A): p_B = p_B.next
        # Step 3. move both pointer and compare them, find the intersection node.
        while p_A!=p_B:
            p_A, p_B = p_A.next, p_B.next
        return p_A
    
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode1(self, headA, headB):
        # len_A+len_B == len_B+len_A, take full use of this nature, so, p_A travel list
        # A first then list B, while p_B travel list B first then list A. p_A and p_B will
        # meet at second travel.
        p_A, p_B = headA, headB
        while p_A is not None and p_B is not None:
            if p_A==p_B: return p_A
            # must check p_A==p_B once move pointer to avoid endless loop
            p_A, p_B = p_A.next, p_B.next
            # Any time, p_A and p_B will get to the end together.
            # so, don't worry about it will never stop.
            if p_A==p_B: return p_A
            if p_A is None: p_A = headB
            if p_B is None: p_B = headA
        return None
    
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode2(self, headA, headB):
        # same with previous one
        p_A, p_B, tag = headA, headB, True
        while p_A is not None and p_B is not None:
            if p_A==p_B: return p_A
            p_A, p_B = p_A.next, p_B.next
            if tag and p_A is None: p_A, tag = headB, False
            if p_B is None: p_B = headA
        return None

if __name__ == '__main__':
    pass
