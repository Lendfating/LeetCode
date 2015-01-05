#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''

"""
# problem
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.
Link: https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# soluction
第一个下降点即是
**二分查找会更快 **

"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        for i in xrange(1,len(num)):
            if num[i]<num[i-1]:
                return num[i];
        return num[0];
    
    def findMin1(self, num):
        # 二分查找，会更快。注意拐点一定出现在(left, right]中
        left, right = 0, len(num)-1;
        while left<right:
            mid = (left+right+1)//2;    # 一定要采用向上取整，不然 right 可能无法到达
            if num[mid]<num[mid-1]: # 拐点
                return num[mid];
            elif num[mid]<num[left]:# 拐点出现在左半部分
                right = mid-1;
            else:                   # 拐点出现在右半部分
                left = mid;
        return num[0];
    
    def findMin2(self, num):
        # 递归实现，让思路清晰点。要画画图，分析一下左右边的情况
        return self.findMinBinary(num, 0, len(num)-1);
        
    def findMinBinary(self, num, left, right):
        if num[left]>num[right]:    # 存在拐点, 递归处理
            mid = (left+right)//2;
            if num[left]>num[mid]:  # 拐点在左半部分
                return self.findMinBinary(num, left, mid);
            else:
                return self.findMinBinary(num, mid+1, right);
        else:       # 正常有序数组
            return num[left];
        

if __name__ == '__main__':
    num = [4, 5, 6, 7, 0, 1, 2];
    s = Solution();
    print s.findMin(num)
    print s.findMin1(num)
    print s.findMin1([2,1])
    print s.findMin2(num)
    print s.findMin2([2,1])
