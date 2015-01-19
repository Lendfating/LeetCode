#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

带记录表的深搜可能会好一点，当有障碍时可以不查，直接返回 0， 这样可能会缩短时间

"""
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        # only need O(n) space
        if len(obstacleGrid)<=0: return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[rows-1][cols-1]==1: return 0
        paths = [0] * (cols+1)
        paths[cols-1] = 1-obstacleGrid[rows-1][cols-1]
        for i in range(rows)[::-1]:
            for j in range(cols)[::-1]:
                paths[j] = paths[j]+paths[j+1] if obstacleGrid[i][j]==0 else 0
        return paths[0]
    
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles1(self, obstacleGrid):
        # only need O(n) space
        if len(obstacleGrid)<=0: return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # must use one line space, if not it will be error in getPaths when i<0
        paths = [[-1]*(cols+1) for i in range(rows+1)]
        # note: the path from start to end is also the path from end to start
        return self.dfs(rows, cols, obstacleGrid, paths)
    
    def dfs(self, i, j, obstacleGrid, paths):
        if i<1 or j<1: 
            return 0     # invalid, out of range
        if obstacleGrid[i-1][j-1]==1: 
            return 0  # obstacle 
        if i==1 and j==1: 
            return 1  # start position
        return self.getPaths(i-1, j, obstacleGrid, paths)\
                + self.getPaths(i, j-1, obstacleGrid, paths)
        
    def getPaths(self, i, j, obstacleGrid, paths):
        if paths[i][j]<0: 
            paths[i][j] = self.dfs(i, j, obstacleGrid, paths)
        return paths[i][j]
            

if __name__ == '__main__':
    s = Solution()
    print s.uniquePathsWithObstacles1([[0,0,0],[0,1,0],[0,0,0]])
