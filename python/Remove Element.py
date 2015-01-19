#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        l, n = 0, len(A)
        while l<n:
            if A[l]==elem:
                A[l] = A[n-1]
                n -= 1
            else:
                l += 1
        return r

if __name__ == '__main__':
    pass
