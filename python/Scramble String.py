#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1)!=len(s2): return False
        if len(s1)<2: return s1==s2
        if s1==s2: return True
        counts = [0]*128    # we can also sort s1 and s2, and then check whether s1==s2
        for ch in s1: counts[ord(ch)] += 1
        for ch in s2:
            counts[ord(ch)] -= 1
            if counts[ord(ch)]<0:
                return False
        for i in xrange(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False
            
    # @return a boolean
    def isScramble1(self, s1, s2):
        # use memorization. dp store the information
        if len(s1)!=len(s2): return False
        if len(s1)<2: return s1==s2
        if s1==s2: return True
        if sorted(s1)!=sorted(s2): return False
        len_s = len(s1)
        # dp[i][j][l] store whether s1[i:i+l] and s2[j:j+l] is scramble or not
        dp = [[[None]*(len_s+1) for c1 in s1] for c2 in s2]
        
        def helper(i, j, l):
            if dp[i][j][l] is None:
                if l==1:
                    dp[i][j][l] = (s1[i]==s2[j])
                elif s1==s2:
                    dp[i][j][l] = True
                elif sorted(s1)!=sorted(s2):
                    dp[i][j][l] = False
                else:
                    dp[i][j][l] = False
                    for k in xrange(1, l):
                        if (helper(i, j, k) and helper(i+k, j+k, l-k)) or \
                            (helper(i, j+l-k, k) and helper(i+k, j, l-k)):
                            dp[i][j][l] = True
                            break
            return dp[i][j][l]
        return helper(0, 0, len_s)
    
    # @return a boolean
    def isScramble2(self, s1, s2):
        # dynamic programming
        if len(s1)!=len(s2): return False
        len_s = len(s1)
        # dp[i][j][l] store whether s1[i:i+l] and s2[j:j+l] is scramble or not
        dp = [[[False]*(len_s+1) for c1 in s1] for c2 in s2]
        for i in xrange(len_s):
            for j in xrange(len_s):
                dp[i][j][1] = s1[i]==s2[j]
        for l in xrange(2, len_s+1):
            for i in xrange(len_s-l+1):
                for j in xrange(len_s-l+1):
                    for k in xrange(1, l):
                        dp[i][j][l] |= dp[i][j][k] and dp[i+k][j+k][l-k]
                        dp[i][j][l] |= dp[i][j+l-k][k] and dp[i+k][j][l-k]
                        if dp[i][j][l]: break
        return dp[0][0][len_s]
                                           
                    
        
        def helper(i, j, l):
            if dp[i][j][l] is None:
                if l==1:
                    dp[i][j][l] = (s1[i]==s2[j])
                elif s1==s2:
                    dp[i][j][l] = True
                elif sorted(s1)!=sorted(s2):
                    dp[i][j][l] = False
                else:
                    dp[i][j][l] = False
                    for k in xrange(1, l):
                        if (helper(i, j, k) and helper(i+k, j+k, l-k)) or \
                            (helper(i, j+l-k, k) and helper(i+k, j, l-k)):
                            dp[i][j][l] = True
                            break
            return dp[i][j][l]
        return helper(0, 0, len_s)
    

if __name__ == '__main__':
    pass
