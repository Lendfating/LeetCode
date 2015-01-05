#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dic = {}
        for key in dict:
            dic[key] = True
        return self.wordTest(s, dic)
            
    def wordTest(self, s, dict):
        if len(s)==0: return True
        for i in xrange(1, len(s)+1):
            if dict.has_key(s[:i]) and self.wordBreak(s[i:], dict):
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print s.wordBreak("leetcode", ["leet", "code"])
