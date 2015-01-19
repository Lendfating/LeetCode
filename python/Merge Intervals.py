#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

当然也可以复用 N 遍 Insert Interval方法，这里就不说了。

"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # sort intervals by start time.
        intervals = sorted(intervals, key=lambda interval: interval.start)
        i = 1
        while i<len(intervals):
            if intervals[i].start<=intervals[i-1].end:
                # merge two intervals
                intervals[i-1].end = max(intervals[i-1].end, intervals[i].end)
                intervals.pop(i)
            else:
                i += 1
        return intervals
        
        
    

if __name__ == '__main__':
    pass
