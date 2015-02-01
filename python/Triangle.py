#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle)==0: return 0
        min_sums = triangle[-1][::]
        for i in range(len(triangle)-1)[::-1]:
            for j in xrange(i+1):
                min_sums[j] = min(min_sums[j], min_sums[j+1])+triangle[i][j]
        return min_sums[0]

if __name__ == '__main__':
    s = Solution()
    print s.minimumTotal([[1],[2,3]])
