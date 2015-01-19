#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left, right = 0, len(A)
        while left<right:
            mid = (left+right)/2
            if A[mid]==target:
                return mid
            elif A[mid]>target:
                right = mid
            else:
                left = mid+1
        # this is the last item which is equal to target, otherwise first one bigger than it
        return left

if __name__ == '__main__':
    pass
