#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

第一种方法是很直观的动归。

第二种方案是从当前可匹配前缀的基础上，增加新单词，看看用现有单词词库是否可以匹配到终点。

"""
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s)==0: return True
        if len(dict)==0: return False
        dic = {}
        for key in dict:
            dic[key] = True
        return self.wordTest(s, dic)
            
    def wordTest(self, s, dict):
        tables = [False]*(len(s)+1)
        tables[0] = True
        for i in xrange(1, len(s)+1):
            for j in range(i)[::-1]:
                if tables[j] and dict.has_key(s[j:i]):
                    tables[i] = True
                    break
        return tables[-1]
    
    def wordTest1(self, s, dict):
        to_check, checked, length = [0], [False]*len(s), len(s)
        while len(to_check)>0:
            start = to_check.pop()
            if not checked[start]:
                checked[start] = True
                for end in xrange(start+1, length+1):
                    if dict.has_key(s[start:end]):
                        to_check.append(end)
                        if end==length: return True
        return False

if __name__ == '__main__':
    s = Solution()
    print s.wordBreak("leetcode", ["leet", "code"])
