#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if len(matrix)==0: return ;
        m, n = len(matrix), len(matrix[0])
        col_mark = 0
        for i in xrange(m):
            row_mark = 0
            for j in xrange(n):
                if matrix[i][j]==0:
                    row_mark = 1
                    col_mark |= 1<<j
            if row_mark==1:
                for j in xrange(n):
                    matrix[i][j] = 0
        for j in xrange(n):
            if col_mark&(1<<j)>0:
                for i in xrange(m):
                    matrix[i][j] = 0
                    
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes1(self, matrix):
        # use first row and first column to store the information
        if len(matrix)==0: return ;
        if len(matrix[0])==0: return ;
        m, n = len(matrix), len(matrix[0])
        col0 = 1     # whether the first column has 0 or not
        # store the 0 information into its first row and column.
        for i in xrange(m):
            if matrix[i][0]==0: col0 = 0
            for j in xrange(1, n):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # use the 0 information to refill the matrix
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, 0, -1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
            if col0==0: matrix[i][0] = 0
            

if __name__ == '__main__':
    pass
