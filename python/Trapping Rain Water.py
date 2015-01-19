#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        highest = 0
        # find the index of the highest board, and divide it into two parts
        for i in xrange(1, len(A)):
            if A[i]>A[highest]: highest = i
            
        left, right, capacity = 0, 0, 0
        # handle the left part of the highest board
        for i in xrange(0, highest):
            left = max(left, A[i])  # update the high of left board
            capacity += left-A[i]
        # handle the right part of the highest board
        for i in xrange(len(A)-1, highest, -1):
            right = max(right, A[i])    # update the high of right board
            capacity += right-A[i]  # the capacity of this position depends on its fall with right board
        return capacity
    
    # @param A, a list of integers
    # @return an integer
    def trap1(self, A):
        # one pass scan. take full use of the info: the capacity of one position depend on min(left, right)
        # we can only update the low board info.
        l, r, capacity = 0, len(A)-1, 0
        while l<r:
            left, right = A[l], A[r]    # the high of two board
            if left<=right:     # left board is low, so update info from left
                while l<r and A[l]<=left:  # find next position which higher than right 
                    capacity += left-A[l]
                    l += 1
            else:
                while l<r and A[r]<=right:
                    capacity += right-A[r]
                    r -= 1
        return capacity
    
    # @param A, a list of integers
    # @return an integer
    def trap2(self, A):
        # one pass scan. take full use of the info: the capacity of one position depend on min(left, right)
        # we can use subtraction.
        l, r, all, block, curLevel = 0, len(A)-1, 0, 0, 0
        # curLevel response the high of water between current interval
        while l<=r:
            newLevel = max(curLevel, min(A[l], A[r]))
            all += (newLevel-curLevel)*(r-l+1)
            curLevel = newLevel
            if A[l]<A[r]:
                block += A[l]
                l += 1
            else:
                block += A[r]
                r -= 1
        return all-block
                
        

if __name__ == '__main__':
    pass
