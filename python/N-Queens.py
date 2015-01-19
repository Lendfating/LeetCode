#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        return self.__solveNQueens(n, n, 0, 0, 0)
    
    # @param n, a integer response n-queue
    # @param m, a integer response rest rows of chessboard 
    # @param mark1, a mark response the used info of columns
    # @param mark2, a mark response the used info of left-oblique
    # @param mark3, a mark response the used info of right-oblique
    # @return all solution of rest m rows with marks
    def __solveNQueens(self, n, m, mark1, mark2, mark3):
        if m<=0: return [[]]
        result = []
        for i in xrange(n):
            # unused in column, left-oblique and right-oblique
            if (1<<i)&mark1==0 and (1<<(n-m+i))&mark2==0 and (1<<(n-m-i+n-1))&mark3==0:
                row = "".join(["."]*i)+"Q"+"".join(["."]*(n-i-1))
                follows = self.__solveNQueens(n, m-1, mark1|(1<<i), mark2|(1<<(n-m+i)), mark3|(1<<(n-m-i+n-1)))
                for follow in follows:
                    follow.insert(0, row)
                    result.append(follow)
        return result

if __name__ == '__main__':
    s = Solution()
    print s.solveNQueens(4)
