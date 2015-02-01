#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s)==0: return [[]]
        result = []
        for i in xrange(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                list = self.partition(s[i:])
                for li in list:
                    li.insert(0, s[:i])
                    result.append(li)
        return result
            
    def isPalindrome(self, s):
        return s==s[::-1]
    
    # @param s, a string
    # @return a list of lists of string
    def partition1(self, s):
        if len(s)==0: return [[]]
        tables = [[[]]]
        for end in xrange(1, len(s)+1):
            tables.append([])
            for start in xrange(end):
                if self.isPalindrome(s[start:end]):
                    for par in tables[start]:
                        new_par = par[::]
                        new_par.append(s[start:end])
                        tables[end].append(new_par)
        return tables[-1]
                
    

if __name__ == '__main__':
    s = Solution()
    print s.partition1("aab")
