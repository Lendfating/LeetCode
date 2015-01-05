#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix, k = [range(n) for i in range(n)], 1;
        for layer in range(n/2):
            for j in range(layer, n-layer-1):
                matrix[layer][j], k= k, k+1;
            for i in range(layer, n-layer-1):
                matrix[i][n-layer-1], k = k, k+1;
            for j in range(n-layer-1, layer, -1):
                matrix[n-layer-1][j], k = k, k+1;
            for i in range(n-layer-1, layer, -1):
                matrix[i][layer], k = k, k+1;
        if n%2==1: matrix[n/2][n/2] = k;
        return matrix;

if __name__ == '__main__':
    s = Solution()
    print s.generateMatrix(0)
    print s.generateMatrix(1)
    print s.generateMatrix(2)
    print s.generateMatrix(3)
