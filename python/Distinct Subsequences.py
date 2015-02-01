#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

典型的动态规划题目，自然可以用滑动数组来降低空间消耗。
参见：https://oj.leetcode.com/discuss/19735/a-dp-solution-with-clarification-and-explanation
第一种方法，固定S，匹配T的前缀
第二种方法，固定T，用S的前缀去匹配。此时，重点是保证第一行是正确的。
    重点是理解，当T长度比S的前缀还长时，递推公式仍然成立。
"""
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        len_S, len_T = len(S), len(T)
        tables = [[0]*(len_S+1) for i in T]
        tables.insert(0, [1]*(len_S+1))
        for i in xrange(len_T):
            for j in xrange(i, len_S):
                tables[i+1][j+1] = tables[i+1][j]
                if T[i]==S[j]:
                    tables[i+1][j+1] += tables[i][j]
        return tables[len_T][len_S]
    
    # @return an integer
    def numDistinct1(self, S, T):
        # implement with sliding array
        len_S, len_T = len(S), len(T)
        tables = [0]*(len_T+1)
        tables[0] = 1
        for i in xrange(len_S):
            for j in range(len_T)[::-1]:
                if S[i]==T[j]:
                    tables[j+1] += tables[j]
        return tables[len_T]

if __name__ == '__main__':
    pass
