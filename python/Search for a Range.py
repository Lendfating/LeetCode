#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = self.leftSearch(A, target)
        right = self.rightSearch(A, target)
        return [left, right] if left<=right else [-1, -1]
    
    def leftSearch(self, A, target):
        left, right = 0, len(A)
        while left<right:
            mid = (left+right)/2
            if A[mid]>=target:
                right = mid
            else:
                left = mid+1
        return left     # this is the index of first item which is litter than or equal to target
    
    def rightSearch(self, A, target):
        left, right = 0, len(A)
        while left<right:
            mid = (left+right)/2
            if A[mid]>target:   # the difference with leftSearch
                right = mid
            else:
                left = mid+1
        return left-1   # this is the index of last item which is litter than or equal to target
    
        

if __name__ == '__main__':
    pass
