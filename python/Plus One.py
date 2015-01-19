#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
再简单的题多想想，也会有好处，也会有更简洁的思路。

"""
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        for i in xrange(len(digits)-1, -1, -1):
            if digits[i]==9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits

if __name__ == '__main__':
    pass
