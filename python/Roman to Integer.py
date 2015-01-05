#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return an integer
    def romanToInt(self, s):
        result, length = 0, len(s);
        for i in xrange(length):
            if s[i]=='I':
                result += -1 if i+1<length and s[i+1] in 'VX' else 1;
            elif s[i]=='V':
                result += 5;
            elif s[i]=='X':
                result += -10 if i+1<length and s[i+1] in 'LC' else 10;
            elif s[i]=='L':
                result += 50;
            elif s[i]=='C':
                result += -100 if i+1<length and s[i+1] in 'DM' else 100;
            elif s[i]=='D':
                result += 500;
            elif s[i]=='M':
                result += 1000;
        return result;
    
    # @return an integer
    def romanToInt1(self, s):
        # from right to left, we can identify subtraction case easily
        result, length = 0, len(s);
        for i in range(length)[::-1]:
            if s[i]=='I':
                result += 1 if result<5 else -1;
            elif s[i]=='V':
                result += 5;
            elif s[i]=='X':
                result += 10 if result<50 else -10;
            elif s[i]=='L':
                result += 50;
            elif s[i]=='C':
                result += 100 if result<500 else -100;
            elif s[i]=='D':
                result += 500;
            elif s[i]=='M':
                result += 1000;
        return result;

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt('MDCCCXCIX') # 1899
    print s.romanToInt('MCMLXXVI')  # 1976
    print s.romanToInt1('MCMLXXVI')  # 1976
