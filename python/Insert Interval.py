#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

因为涉及到数组的中间值插入和删除等操作，因此时间复杂度不会低于O(n)，所以二分查找的意义不是很大。

"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals)<=0: return [newInterval]
        index = self.binarySearch(intervals, newInterval)
        intervals.insert(index, newInterval)
        if index>0 and intervals[index-1].end>=intervals[index].start:
            index -= 1
        while index<len(intervals)-1 and intervals[index].end>=intervals[index+1].start:
            intervals[index].end = max(intervals[index].end, intervals[index+1].end)
            intervals.pop(index+1)
        return intervals
    
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return the index of newInterval should be in
    def binarySearch(self, intervals, newInterval):
        # find the index of the first elem which is bigger than or equal to newInterval
        l, r = 0, len(intervals)
        while l<r:
            mid = (l+r)/2
            if intervals[mid].start>=newInterval.start:
                r = mid
            else:
                l = mid+1
        return l
    
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert1(self, intervals, newInterval):
        if len(intervals)<=0: return [newInterval]
        i = 0
        while i<len(intervals):
            if intervals[i].end<newInterval.start:
                i += 1
            elif intervals[i].start<=newInterval.end:
                newInterval.start = min(intervals[i].start, newInterval.start)
                newInterval.end = max(intervals[i].end, newInterval.end)
                intervals.pop(i)
            else:
                intervals.insert(i, newInterval)
                return intervals
        intervals.insert(i, newInterval)
        return intervals
    

if __name__ == '__main__':
    pass
