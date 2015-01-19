#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

注意条件的判断，A[i]!=A[end-1]即可，没必要 A[i]!=A[end] or A[end]!=A[end-1]
注意我们的目标是不要加入两个以上的相同元素，而数组又是按递增顺序的，所以我们完全可以之比较首位元素，
即可知加入A[i]会不会导致有连续的 K 个A[i]

"""
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)<3: return len(A)
        end = 1
        for i in xrange(2, len(A)):
            if A[i]!=A[end-1]:  # A[i]!=A[end] or A[end]!=A[end-1]:
                A[end+1] = A[i]
                end += 1
        return end+1

if __name__ == '__main__':
    pass
