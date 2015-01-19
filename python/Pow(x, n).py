#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        # x^7 = x^1 * x^2 * x^4
        result, curPow, i, sign, n = 1, x, 0, True if n>=0 else False, abs(n)
        while (1<<i)<=n:
            if (1<<i)&n > 0: # this bit is "1", so we need curPow in the result
                result *= curPow
            curPow, i = curPow*curPow, i+1
        return result if sign else 1.0/result
    
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow1(self, x, n):
        # from high to low
        x, n = x if n>=0 else 1/x, abs(n)
        result, f = 1, x
        while n>0:
            if n&1==1: result *= f
            n = n>>1
            f = f*f
        return result
    
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow2(self, x, n):
        if n<0: # 尽量少做除法，除法慢
            return 1/self.power(x, -n)
        else:
            return self.power(x, n)
        
    def power(self, x, n):
        if n==0: return 1
        half = self.power(x, n/2)
        if n%2==0:
            return half*half
        else:
            return half*half*x

if __name__ == '__main__':
    pass
