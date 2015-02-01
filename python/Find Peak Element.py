#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        # binary search
        left, right = 0, len(num)
        while left<right:
            mid = (left+right)>>1
            if mid==left or num[mid-1]<num[mid]:
                if mid+1==right or num[mid]>num[mid+1]: return mid
                left = mid+1
            else:
                right = mid
        return left
        

if __name__ == '__main__':
    pass
