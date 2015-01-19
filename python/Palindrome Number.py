#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

10 is not palindrome
"""
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0: return False
        rev_x, copy_x = 0, x
        while x>0:
            rev_x = rev_x*10 + x%10
            x = x/10
        return rev_x==copy_x
    
    # @return a boolean
    def isPalindrome1(self, x):
        if x<0: return False
        acumu, deta = 0, 1
        while x/10>=deta:
            acumu = acumu*10 + x%10
            x, deta = x/10, deta*10
        if x>=deta: x /= 10
        return x==acumu
        

if __name__ == '__main__':
    pass
