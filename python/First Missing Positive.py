#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''

"""
# problem
Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.

# soluction
因为有控件和时间的限制，故先排序的思路是不可以的。要想确保时间为O（n），必须要用空间换时间，而由于空间的限制，故必须充分利用原有控件。

"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # 对原始数组 A 处理，保证 >0 的数在数组的右侧
        left, right, length = 0, len(A)-1, len(A);
        while left<=right:
            A[right], A[left] = A[left], A[right];  # 交换逆序对
            while left<length and A[left]<=0: left += 1;
            while right>=0 and A[right]>0: right -= 1;
        # 清楚左侧的负数，将其变为1（不要取反，万一多个0的话就糟了）
        for i in xrange(left):
            A[i] = 1;
        # 依次处理右侧的正数，将其标记在原始数组A中，负数位表示出现过
        for i in xrange(left, len(A)):
            index = abs(A[i])-1;
            if index<length: # 越界的不用管，最低缺失数据一定在1-len(A)+1之间
                A[index] = -abs(A[index]);
        # 从起始位开始检查，输出第一个非负位（表示第一个缺失的数据）
        for i in xrange(len(A)):
            if A[i]>0:
                return i+1;
        return len(A)+1;
    
    def firstMissingPositive1(self, A):
        # 本质上是同排序。既然时间、空间都有限制，应该想到桶的思想。易知结果在1~len(A)+1之间，故可以考虑排序标记
        length = len(A);
        for i in xrange(length):    # 考虑重复元素，股两层循环
            while A[i]>0 and A[i]<=length and A[i]!=A[A[i]-1]:
                val = A[i]-1;
                A[i], A[val] = A[val], A[i];  # 交换
        # 寻找第一个未标记的桶（A[i]!=i+1）
        for i in xrange(length):
            if A[i]!=i+1:
                return i+1;
        return length+1;

if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive([0])
    print s.firstMissingPositive([3,4,-1,1])
    
    print s.firstMissingPositive1([0])
    print s.firstMissingPositive1([3,4,-1,1])
    
    
