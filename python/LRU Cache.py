#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

题目要求：不强调使用频率，只是按刷新顺序，剔除最近没有使用过得项。因此完全没有必要使用堆统计使用频率了。
（使用堆只能处理好频率，对使用时间无法处理）
题目要求是快速查找和添加与删除，因此，明显用链表比数组更靠谱。因此，此题采用链表与hash结合的方式实现。

"""
class Item:
    def __init__(self, key, value, prev=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = None
        
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Item(0, 0) # dummy one
        self.trail = self.head

    # @return an integer
    def get(self, key):
        if not self.map.has_key(key): return -1
        item = self.map[key]
        if item!=self.trail:    # if item don't at the trail, move it to the trail
            # delete item from the list
            item.prev.next = item.next
            item.next.prev = item.prev
            # add it at the trail of the last
            self.trail.next = item
            item.prev = self.trail
            item.next = None
            self.trail = item
        return item.value


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.map.has_key(key):
            item = self.map[key]
            if item!=self.trail:    # if item don't at the trail, move it to the trail
                # delete item from the list
                item.prev.next = item.next
                item.next.prev = item.prev
                # add it at the trail of the last
                self.trail.next = item
                item.prev = self.trail
                item.next = None
                self.trail = item
            item.value = value
        else:
            if self.capacity==0:  # the list is full now
                # remove one from the head of the list
                item = self.head.next
                self.map.pop(item.key)
                # delete it from the list
                item.prev.next = item.next
                if item.next is not None: item.next.prev = item.prev
                # update the trail pointer
                if self.trail==item: self.trail = item.prev
                self.capacity += 1
            # create new item with given key and value
            item = Item(key, value, self.trail)
            self.map[key] = item
            self.trail.next = item
            self.trail = item
            self.capacity -= 1
        
if __name__ == '__main__':
    pass
