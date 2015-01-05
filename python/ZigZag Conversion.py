#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows<=1: return s
        step, groups, len_s, result = 2*nRows-2, len(s)/(2*nRows-2)+1, len(s), ""
        for i in range(nRows):
            for j in xrange(groups):
                if j*step+i<len_s: result += s[j*step+i]
                if (j+1)*step-i<len_s and i>0 and i<nRows-1: result += s[(j+1)*step-i]
        return result

if __name__ == '__main__':
    pass
