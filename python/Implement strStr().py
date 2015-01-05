#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        # Brute force
        for i in xrange(len(haystack)-len(needle)+1):
            matched = True
            for j in xrange(len(needle)):
                if haystack[i+j]!=needle[j]:
                    matched = False
                    break
            if matched:
                return i
        return -1
    
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr1(self, haystack, needle):
        #if len(haystack)/len(needle)<10:
        #    return self.strStr(haystack, needle)
        return self.kmp(haystack, needle)
    
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr2(self, haystack, needle):
        len_h, len_n = len(haystack), len(needle)
        if len_n==0: return 0
        nexts, next = [-1] * len_n, -1  # next is the last 'next info' (i-1)
        for i in xrange(1, len_n):
            while next>=0 and needle[i-1]!=needle[next]:
                next = nexts[next]
            nexts[i], next = next+1, next+1
        # take full use of 'nexts' to search needle in haystack
        j = 0;  # index for of needle
        for i in xrange(len_h): # i is the index of haystack
            while j>0 and haystack[i]!=needle[j]:
                j = nexts[j];
            if haystack[i]==needle[j]:
                j += 1
            if j==len_n: # match all
                return i-j+1
        return -1
    
    # @desc： 前两种计算前缀（nexts）的方法目前没找到bug，但是时间复杂度较高
    #        目前 nexts 中记录匹配失败的跳转选择，也可以记录所有相同前缀信息。
    # @param pattern, a string
    # @return a nexts array
    def compute_prefix(self, pattern):
        # compute the prefix match table, that is 'nexts' array
        nexts = [0] * len(pattern)
        for index in xrange(1, len(pattern)):    # calculate the next of every index
            # shift needle to find a prefix match 'target str' which is also needle
            for shift in xrange(1, index+1): # shift needle
                matching = True
                for k in xrange(index-shift):   # verify this case
                    if pattern[shift+k]!=pattern[k]:
                        matching = False;
                        break
                if matching:
                    nexts[index] = index-shift;
                    break
        return nexts;
                
    # @param pattern, a string
    # @return a nexts array
    def compute_prefix1(self, pattern):
        # compute the prefix match table, that is 'nexts' array
        nexts, len_pattern = [0] * len(pattern), len(pattern)
        for shift in range(1, len_pattern)[::-1]:
            for k in xrange(len_pattern-shift):
                if pattern[shift+k]!=pattern[k]:
                    nexts[shift+k] = k
                    break
        return nexts;
    
    # @desc: 按理说本位相同的情况应该舍弃，所以这里是可以优化的
    # @param pattern, a string
    # @return a nexts array
    def compute_prefix2(self, pattern):
        # compute the prefix match table, that is 'nexts' array
        nexts, next = [-1] * len(pattern), -1  # next is the last 'next info' (i-1)
        for i in xrange(1, len(pattern)):
            while next>=0 and pattern[i-1]!=pattern[next]:
                next = nexts[next]
            nexts[i], next = next+1, next+1
        return nexts;
        
    # @param text, a string
    # @param pattern, a string
    # @return an integer
    def kmp(self, text, pattern):
        len_text, len_pattern = len(text), len(pattern)
        if len_pattern==0: return 0
        if len_pattern>len_text: return -1
        nexts = self.compute_prefix(pattern)
        # take full use of 'nexts' to search needle in text
        j = 0;  # index for of pattern
        for i in xrange(len_text): # i is the index of text
            while j>0 and text[i]!=pattern[j]:
                j = nexts[j];
            if text[i]==pattern[j]:
                j += 1
            if j==len_pattern: # match all
                return i-j+1
        return -1

if __name__ == '__main__':
    s = Solution()
    print s.strStr("", "")
    print s.strStr1("", "")
