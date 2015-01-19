#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return an integer
    def reverse(self, x):
        sign, val, res = -1 if x<0 else 1, abs(x), 0
        while val>0:
            res = res*10 + val%10
            val = val/10
        if res>(1<<31):
            return 0
        else:
            return sign*res;
            

if __name__ == '__main__':
    pass
