#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if len(grid)==0: return 0
        for j in xrange(1, len(grid[0])): grid[0][j] += grid[0][j-1]
        for i in xrange(1, len(grid)):
            grid[i][0] += grid[i-1][0]
            for j in xrange(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[len(grid)-1][len(grid[0])-1]
    
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        # 滚动数组方法
        if len(grid)==0: return 0
        SYS_MAX = 100000
        sums = [SYS_MAX]*(len(grid[0])+1)
        sums[1] = 0     # important for start
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                sums[j+1] = grid[i][j] + min(sums[j], sums[j+1])
        return sums.pop()
        

if __name__ == '__main__':
    s = Solution()
    print s.minPathSum([[1,2],[1,1]])
