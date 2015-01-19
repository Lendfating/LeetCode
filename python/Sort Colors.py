#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

虽然我觉得统计0、1、2的个数，再分别设置A中多少个0、1、2的方法很不好（实际应用价值太小，把原值抹掉了），
但是第二种滑动窗口的方式还是有可鉴之处的。

"""
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        # p0 and p1 is the end of 0/1, p2 is the start of 2
        p0, p1, p2 = 0, 0, len(A)-1
        while p1<=p2:
            if A[p1]==0: # red color
                A[p1], A[p0] = A[p0], A[p1]
                p0 += 1     # p1>=p0 forever, so we have checked p0.
            elif A[p1]==2:  # blue color
                A[p1], A[p2] = A[p2], A[p1]
                p2 -= 1
            p1 += 1
            
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors1(self, A):
        # we can use switch for this method in C++
        i, j = 0, 0 # this is the gap between red and white, white and blue
        for k in xrange(len(A)):
            if A[k]==0:
                A[k], A[j], A[i] = 2, 1, 0
                k, j, i = k+1, j+1, i+1
            elif A[k]==1:
                A[k], A[j] = 2, 1
                k, j = k+1, j+1
            else:   # A[k]==2
                A[k] = 2
                k = k+1
        
        
                
if __name__ == '__main__':
    pass
