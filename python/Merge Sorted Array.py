#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i, j, k = m-1, n-1, m+n-1
        while j>=0:
            if i>=0 and A[i]>=B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1

if __name__ == '__main__':
    pass
