#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''

"""
# problem
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Link: https://oj.leetcode.com/problems/3sum/

# soluction
错误方法： 遍历获得1-2个元素，再利用 hash or 二分查找 找第三个元素，的方法太慢（n^2*log(n) or a*N^2）。
正确方法： 先排序，确定第一个元素，然后再通过左右夹逼的方式得到第2、3个元素。
    另外，重复元素的去除必须融合在查找的过程中，不可最后用别的函数去寻找，太慢。

"""
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num)<3:
            return [];
        ans = [];
        num.sort(); # 递增排序
        for i in xrange(len(num)-2):
            if i>0 and num[i]==num[i-1]:continue;   # 跳过重复项
            left, right = i+1, len(num)-1;
            while left<right:
                sum = num[i]+num[left]+num[right];
                if (sum==0):
                    ans.append([num[i], num[left], num[right]]);
                    while left<right and num[left]==num[left+1]: left+=1;   # 跳过重复项
                    while left<right and num[right]==num[right-1]: right-=1;
                    left += 1;  # 不可直接跳出，中间还有可能存在别的匹配对
                    right -= 1;
                elif sum<0:
                    left += 1;
                else:
                    right -= 1;
        
        return ans;

if __name__ == '__main__':
    list = [-2,0,1,1,2];#[14,4,6,-1,10,9,-8,7,-13,14,-13,-11,-8,-9,11,14,-8,-14,-13,7,-10,-15,-13,-11,-11,11,14,13,2,-14,1,-7,-2,14,-1,-15,9,7,-1,3,6,1,7,5,-1,-5,4,-2,-4,-1,-9,-7,-1,-7,-11,3,12,10,-7,-1,12,1,8,-13,1,14,9,-13,6,-7,-3,-11,2,-11,10,-14,-1,-9,0,2,5,6,3,-11,6,7,0,3,3,0,-12,-8,-13,3,-14,-5,2,10,-11,-14,-12,1,-10,5,5,7,-1,11,14,6,-10,-4,-3,8,-7,10,1,8,-1,-11,-15,-6,-12,-13,12,-11]

    s = Solution();
    print s.threeSum(list);
    
    