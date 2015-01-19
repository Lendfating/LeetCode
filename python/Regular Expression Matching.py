#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        j = 2
        while j<len(p)-1:
            if p[j+1]=='*' and p[j-1]=='*' and p[j]==p[j-2]:
                p = p[:j]+p[j+2:]
            else:
                j += 1
        return self.testMatch(s, p)
        
    # @return a boolean
    def testMatch(self, s, p):
        if len(p)==0: return len(s)==0
        if len(p)>1 and p[1]=='*':  # '*' case
            if self.isMatch(s, p[2:]): return True
            if len(s)>0 and (p[0]=='.' or s[0]==p[0]):
                return self.isMatch(s[1:], p)
            return False
        else:
            if len(s)>0 and (p[0]=='.' or s[0]==p[0]):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
            
    # @return a boolean
    def testMatch1(self, s, p):
        i, j, len_s, len_p = 0, 0, len(s), len(p)
        while j<len_p:
            if j+1<len_p and p[j+1]=='*':   # '*' case
                while i<len_s and (p[j]=='.' or s[i]==p[j]):
                    if self.testMatch1(s[i:], p[j+2:]): return True
                    i += 1
                return self.testMatch1(s[i:], p[j+2:])
            else:                           # common case
                if i<len_s and (p[j]=='.' or s[i]==p[j]):
                    i, j = i+1, j+1
                else:
                    return False
        return i==len_s
           

if __name__ == '__main__':
    pass
