#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        # binary search
        return self.binarySearch(A, 0, len(A)-1, target)

    def binarySearch(self, A, left, right, target):
        if left>right: return -1;
        
        mid = (left+right)/2
        if A[mid]==target: return mid;
        
        if A[left]<A[right]:    # sorted sub-Array
            if A[mid]>target:
                return self.binarySearch(A, left, mid-1, target)
            else:
                return self.binarySearch(A, mid+1, right, target)
        else:
            ret = self.binarySearch(A, left, mid-1, target)
            if ret==-1: ret = self.binarySearch(A, mid+1, right, target)
            return ret;
        
    def search1(self, A, target):
        # non-recursion
        left, right = 0, len(A)-1
        while left<=right:
            mid = (left+right)/2
            if A[mid]==target:
                return mid;
            # there must be a sorted sub-array in left or right part
            if (A[left]<A[mid] and A[left]<=target and target<A[mid]) or \
               (A[left]>A[mid] and (target<A[mid] or target>A[right])):
                # left part is sorted and target in it
                # left part is rotated and target not in right part
                right = mid-1;  # search left part
            else:
                left = mid+1;
        return -1;
                

if __name__ == '__main__':
    pass
