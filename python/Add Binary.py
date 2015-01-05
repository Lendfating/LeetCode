#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        length1, length2, carry, result = len(a), len(b), 0, "";
        for i in xrange(1, max(length1, length2)+1):
            operator1 = 1 if i<=length1 and a[-i]=='1' else 0;
            operator2 = 1 if i<=length2 and b[-i]=='1' else 0;
            carry, result = (operator1+operator2+carry)>>1, str((operator1+operator2+carry)&1)+result;
        if carry==1:
            result = '1' + result;
        return result;

if __name__ == '__main__':
    s = Solution()
    print s.addBinary("11", "1")
