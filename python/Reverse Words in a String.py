#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])
    
    # @param s, a string
    # @return a string
    def reverseWords1(self, s):
        # time O(n) ; memory O(1)
        # 该方法C++可行，python不行，Python中String不支持下标访问
        length = len(s)
        # for the first travel, reverse every char
        for i in xrange(length/2):
            s[i], s[length-1-i] = s[length-1-i], s[i]
        # for the second travel, reverse every char in the word
        begin, end, s = 0, 0, s+' '   # the ends of one word
        for i in xrange(length+1):
            if s[i]!=' ':
                end = i;
                for j in xrange(0, (end-begin)/2):
                    s[begin+j], s[end-1-j] = s[length-1-i], s[i]
                begin = i+1;
        # for the third travel, delete the redundancy spaces 
        index, start = 0, 0;
        while s[start]==' ': start+=1;
        for i in xrange(start, length):
            if s[i]!=' ' or (s[i]==' 'and s[i+1]!=' '):
                s[index] = s[i];
                index += 1;
        return s[:index]

if __name__ == '__main__':
    pass
