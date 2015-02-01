#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i, j, length = 0, len(s)-1, len(s)
        while i<j:
            while i<j and not s[i].isalnum(): i += 1
            while i<j and not s[j].isalnum(): j -= 1
            if s[i].lower()!=s[j].lower(): return False
            i, j = i+1, j-1
        return True
    
if __name__ == '__main__':
    pass
