#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return an integer
    def atoi(self, str):
        str, res = str.strip(), 0
        if len(str)<=0: return res
        sig = -1 if str[0]=='-' else 1
        str = str[1:] if str[0]=='-' or str[0]=='+' else str
        for item in str:
            bit = ord(item)-ord('0')
            if bit<0 or bit>9: break
            res = res*10 + bit
        res = sig*res
        if res>(1<<31)-1: return (1<<31)-1
        if res<-(1<<31): return -(1<<31)
        return res
            

if __name__ == '__main__':
    pass
