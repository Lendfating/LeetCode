#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
方案一：最直观的方法就是使用最小堆，查找 K 个链中的最小值。

方案二：分而治之。记得合并两个链的时间复杂度是O(n)，因此，利用分治的思想合并每一对串，可以计算时间复杂度依然为O(nlog(k))
for example, 8 ListNode, and the length of every ListNode is x1, x2, x3, x4, x5, x6, x7, x8, total is n.
on level 3: x1+x2, x3+x4, x5+x6, x7+x8 sum: n
on level 2: x1+x2+x3+x4, x5+x6+x7+x8 sum: n
on level 1: x1+x2+x3+x4+x5+x6+x7+x8 sum: n
total 3n, nlog8

注意：顺序合并的话时间复杂度应该在（O(kn）左右，因为这其中会有很多串多次重复访问，从而影响速度。从构件树的角度理解，这样相当于构建了一个单链树
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# define of my mine minHeap
class Heap:
    def __init__(self, list):
        self.list = [item for item in list if item is not None]
        self.length = len(self.list)
        for i in xrange(self.length/2-1, -1, -1):
            self.__down(i)
    
    def getMin(self):
        item, self.list[0] = self.list[0], self.list[self.length-1]
        self.length -= 1
        self.__down(0)
        return item
    
    def addItem(self, item):
        if len(self.list)>self.length:
            self.list[self.length] = item
        else:
            self.list.append(item)
        self.__up(self.length)
        self.length += 1
    
    def __up(self, index):
        while index>0 and self.list[(index-1)/2].val>self.list[index].val:
            self.list[(index-1)/2], self.list[index] = self.list[index], self.list[(index-1)/2]
            index = (index-1)/2
    
    def __down(self, index):
        while 2*index+1<self.length:    # not leaf
            left, right = 2*index+1, 2*index+2
            to_cmp = right if right<self.length and self.list[right].val<self.list[left].val else left
            if self.list[index].val>self.list[to_cmp].val:
                self.list[index], self.list[to_cmp] = self.list[to_cmp], self.list[index]
                index = to_cmp
            else:
                break

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap, dummy = Heap(lists), ListNode(0)
        p = dummy
        while heap.length>0:
            p.next = heap.getMin()
            p = p.next
            if p.next is not None: heap.addItem(p.next)
        return dummy.next
    
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists1(self, lists):
        # cool. divide and conquer. the core if prove time cost is O(n*lg(k))
        if len(lists)==0: return None
        if len(lists)==1: return lists[0]
        mid = len(lists)/2
        p1 = self.mergeKLists1(lists[:mid])
        p2 = self.mergeKLists1(lists[mid:])
        dummy = ListNode(0)
        p = dummy
        while p1 is not None and p2 is not None:
            if p1.val<p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        p.next = p1 if p1 is not None else p2
        return dummy.next
    
    
if __name__ == '__main__':
    pass
