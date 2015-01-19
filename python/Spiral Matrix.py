#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix)<=0: return []
        m, n, result, padding = len(matrix), len(matrix[0]), [], -1
        for padding in xrange(min(m,n)/2):
            for j in xrange(padding, n-padding-1):
                result.append(matrix[padding][j])
            for i in xrange(padding, m-padding-1):
                result.append(matrix[i][n-padding-1])
            for j in xrange(n-padding-1, padding, -1):
                result.append(matrix[m-padding-1][j])
            for i in xrange(m-padding-1, padding, -1):
                result.append(matrix[i][padding])
        if min(m, n)%2==1:  # middle row or column
            padding += 1
            if m<n: # rest part is one row
                for j in xrange(padding, n-padding):
                    result.append(matrix[padding][j])
            else:
                for i in xrange(padding, m-padding):
                    result.append(matrix[i][padding])
        return result
            

if __name__ == '__main__':
    pass
