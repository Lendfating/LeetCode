#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==0: return ""
        arr_len, min_len, stop, j = len(strs), min([len(s) for s in strs]), 0, 0
        while j<min_len:
            for i in xrange(1, arr_len):
                stop |= 0 if strs[0][j]==strs[i][j] else 1
            if stop>0:
                break;
            j += 1;
        return strs[0][:j]

if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(["asdf","as"])
    print s.longestCommonPrefix([])
    print s.longestCommonPrefix(["asd","ba"])
    print s.longestCommonPrefix(["asd"])
    print s.longestCommonPrefix([""])
