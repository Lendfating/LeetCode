#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        index = self.binaryFindMinIndex(num, 0, len(num)-1)
        return num[index] if index>=0 else num[0]
    
    def binaryFindMinIndex(self, num, left, right):
        if left>=right:
            return -1;
        
        mid = (left+right+1)//2;
        if num[mid-1]>num[mid]:
            return mid;
        ret = -1;
        if num[left]>=num[mid-1]:
            ret = self.binaryFindMinIndex(num, left, mid-1)
        if ret<0 and num[mid]>=num[right]:
            ret = self.binaryFindMinIndex(num, mid, right)
        return ret;
    
    # @param num, a list of integer
    # @return an integer
    def findMin1(self, num):
        return self.binaryFindMin(num, 0, len(num)-1)
    
    def binaryFindMin(self, num, left, right):
        if left>=right or num[left]<num[right]:
            return num[left];
        else:
            mid = (left+right+1)//2;
            min_left = self.binaryFindMin(num, left, mid-1)
            min_right = self.binaryFindMin(num, mid, right)
            return min(min_left, min_right);

if __name__ == '__main__':
    s=Solution()
    print s.findMin([4, 5, 6, 7, 0, 1, 2])
    print s.findMin1([4, 5, 6, 7, 0, 1, 2])
