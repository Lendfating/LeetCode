#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip()
        for i in range(len(s))[::-1]:
            if s[i]==" ":
                return len(s)-i-1
        return len(s)
    
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        # one pass scan
        length, len_s = 0, len(s)
        for i in xrange(len_s):
            if s[i]!=' ':
                length += 1
            elif i+1<len_s and s[i+1]!=' ':
                length = 0
        return length

if __name__ == '__main__':
    pass
