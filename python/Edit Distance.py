#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        len_1, len_2 = len(word1), len(word2)
        dis = [range(i, i+len_2+1) for i in xrange(len_1+1)]
        for i in xrange(len_1):
            for j in xrange(len_2):
                if word1[i]==word2[j]:
                    dis[i+1][j+1] = dis[i][j]
                else:
                    dis[i+1][j+1] = 1 + min(dis[i][j], dis[i][j+1], dis[i+1][j])
        return dis[len_1][len_2]
    
    # @return an integer
    def minDistance1(self, word1, word2):
        # use scrollable array to reduce the memory to O(n)
        if len(word1)<len(word2): return self.minDistance1(word2, word1)
        len_1, len_2 = len(word1), len(word2)
        dis = range(len_2+1)
        for i in xrange(len_1):
            dis[0], left_upper = i+1, dis[0]
            for j in xrange(len_2):
                upper, left = dis[j+1], dis[j]
                if word1[i]==word2[j]:
                    dis[j+1] = left_upper
                else:
                    dis[j+1] = 1 + min(left_upper, upper, left)
                left_upper = upper
        return dis[len_2]
                    
        

if __name__ == '__main__':
    s = Solution()
    print s.minDistance1("sea", "eat")
