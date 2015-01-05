#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows<=0: return []
        if numRows==1: return [[1]]
        triangle = self.generate(numRows-1)
        triangle.append([1]*numRows)
        for i in xrange(1, numRows-1):
            triangle[numRows-1][i] = triangle[numRows-2][i-1]+triangle[numRows-2][i]
        return triangle
    
    # @return a list of lists of integers
    def generate1(self, numRows):
        triangle = []
        for i in xrange(numRows):
            triangle.append([1]*(i+1))
            for j in xrange(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle

if __name__ == '__main__':
    pass
