#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
贪心算法的一道题。用动态规划会计算一些没用的项。

注意，还可以利用 KMP 算法进一步优化，但是考虑到“？”的存在，而且每个patterns中的子串元素并不见得很短，重复性并不见得很高，所以优化的效果并不好说

"""
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        patterns = p.split("*")     # don't pay attention to '' element
        if len(p)==0: return len(s)==0  # must be here. "".split("*") will be ['']
        if len(patterns)==1: return len(s)==len(p) and self.testMatch(s, p) # for case s="aa", p="a"
        if patterns[0]!='' and not self.testMatch(s, patterns[0]): return False
        i, len_s = 0, len(s)
        for k in xrange(len(patterns)):
            pat = patterns[k]
            for i in xrange(i, len_s):
                if self.testMatch(s[i:], pat):
                    i += len(pat)
                    break
            else:
                return "".join(patterns[k:])==""    # for the case s="", p="*"
        return self.testMatch(s[len_s-len(pat):], pat)
            
            
    def testMatch(self, s, p):
        if len(s)<len(p): return False
        for i in xrange(len(p)):
            if p[i]!="?" and p[i]!=s[i]: return False
        return True
    
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch1(self, s, p):
        # with C++, we can take full use of "\0" at the end of one string to avoid the unusual case at the end
        # but in python, we must assert the length
        # pay attention to case s="abacdec", p="ab*c", is also ok
        i, j, start_i, start_j, len_s, len_p = 0, 0, 0, 0, len(s), len(p)
        while i<len_s:
            # match case
            if j<len_p and (p[j]=="?" or (s[i]!="*" and p[j]==s[i])):
                i, j = i+1, j+1
                continue
            # "*" case. new start for next sub-string
            if j<len_p and p[j]=="*":
                start_i, start_j, j = i, j+1, j+1
                continue
            # match failed. we should shift i to re-match
            if start_j>0:
                i, start_i, j = start_i+1, start_i+1, start_j
                continue
            # match failed and there is no "*" in p before j. so we can't shift i
            return False
        # ignore "*" in rest part of p 
        while j<len_p and p[j]=="*": j += 1
        return j==len_p
    
if __name__ == '__main__':
    s = Solution()
    print s.isMatch("aa", "a*")
