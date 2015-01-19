#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num = sorted(num)   # avoid the duplicate Permutations due to duplicate num
        return self.__permuteUnique([], num)
    
    def __permuteUnique(self, path, num):
        if len(num)==0: return [path]
        result = []
        for i in xrange(len(num)):
            # avoid the duplicate Permutations due to duplicate num
            if i>0 and num[i]==num[i-1]: continue
            # we can use a bool mark or one pass shift and back to avoid clone of num
            # but I just clone it here.
            result.extend(self.__permuteUnique(path+num[i:i+1], num[:i]+num[i+1:]))
        return result
    
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique1(self, num):
        # take full use of next permutation: https://oj.leetcode.com/problems/next-permutation/
        num = sorted(num)
        result = [num[:]]
        while self.nextPermutation(num) is not None:
            result.append(num[:])
        return result
        
    def nextPermutation(self, num):
        for i in range(len(num))[::-1]:
            if i>0 and num[i]>num[i-1]:
                break
        else:
            return None # all in non-increasing, end
        # swap num[i-1] with the last elem bigger than num[i-1]
        for j in range(i, len(num))[::-1]:
            if num[j]>num[i-1]:
                num[i-1], num[j] = num[j], num[i-1]
                break
        # sort the right part begin i
        l, r = i, len(num)-1
        while l<r:
            num[l], num[r] = num[r], num[l]
            l, r = l+1, r-1
        return num

if __name__ == '__main__':
    pass
