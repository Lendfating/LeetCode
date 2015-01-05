#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        max_len, cur_len, indexs = 0, 0, [-1]*128    # the index of last char
        for i in xrange(0, len(s)):
            cur_len = min(cur_len+1, i - indexs[ord(s[i])])
            indexs[ord(s[i])] = i
            max_len = max(max_len, cur_len)
        return max_len

if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring("qopubjguxhxdipfzwswybgfylqvjzhar")
