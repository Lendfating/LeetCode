#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left, right = 0, len(A)
        while left<right:
            mid = (left+right)/2
            if A[mid]==target:
                return True
            elif (A[mid]<A[right-1] and A[mid]<target and target<=A[right-1]) or \
                (A[left]<A[mid] and (target>A[mid] or target<A[left])):
                left = mid+1
            elif (A[left]<A[mid] and A[left]<=target and target<A[mid]) or \
                (A[mid]<A[right-1] and (target>A[right-1] or target<A[mid])):
                right = mid
            else:
                return self.search(A[left:mid], target) or self.search(A[mid+1:right], target)
        return False
    
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left, right = 0, len(A)
        while left<right:
            mid = (left+right)/2
            if A[mid]==target: return True
            if A[left]<A[mid]:  # left part is sorted
                if A[left]<=target and target<A[mid]:
                    right = mid
                else:
                    left = mid+1
            elif A[left]>A[mid]:    # right part is sorted
                # note: we not use A[mid]<A[right-1]
                if A[mid]<target and target<=A[right-1]:
                    left = mid+1
                else:
                    right = mid
            else:
                # skip duplicate one
                left += 1
        return False
    

if __name__ == '__main__':
    pass
