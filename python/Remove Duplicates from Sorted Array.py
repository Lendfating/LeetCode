#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==0: return 0;
        last = 0;
        for i in xrange(1, len(A)):
            if A[i]!=A[last]:
                A[last+1] =A[i];
                last += 1;
        return last+1;

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,2])
