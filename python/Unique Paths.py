#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        # just an permutation problem
        # result = A(m+n, m+n)/(A(m,m)*A(n,n)) 
        m, n = (m-1, n-1) if m>n else (n-1, m-1)
        if n==0: return 1;
        def A(x, y):
            return x>y and x*A(x-1, y) or y
        return A(m+n, m+1)/A(n, 1)
    
    # @return an integer
    def uniquePaths1(self, m, n):
        # just an permutation problem
        # result = C(m+n, n)
        result = 1;
        for i in xrange(1, min(m,n)):
            result = result*(max(m,n)+i-1)/i
        return result

if __name__ == '__main__':
    pass
