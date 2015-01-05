#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        max_len, max_axis, len_s = -1, 0, 2*len(s)-1
        for axis in xrange(len_s):
            cur_len = axis%2
            while axis-cur_len>=0 and axis+cur_len<len_s and s[(axis-cur_len)/2]==s[(axis+cur_len)/2]:
                cur_len +=2
            cur_len -= 2
            if cur_len>max_len:
                max_len, max_axis = cur_len, axis
        return s[(max_axis-max_len)/2:(max_axis+max_len)/2+1]

    # @return a string
    def longestPalindrome1(self, s):
        # more detail see: http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
        T, P, len_T = ["^", "#"], [0]*(2*len(s)+2), 2*len(s)+2
        for item in s:
            T.extend([item, "#"])
        T.append("$")
        C, R, opt_i = 0, 0, 0
        for i in xrange(1, len_T):
            P[i] = min(P[C-(i-C)], R-i) if i<=R else 0
            while T[i-P[i]-1]==T[i+P[i]+1]: P[i] += 1
            if i+P[i]>R:
                C, R = i, i+P[i]
            opt_i = i if P[i]>P[opt_i] else opt_i
        return s[(opt_i-P[opt_i]-1)/2:(opt_i+P[opt_i])/2]
        
        
if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome1("a")
