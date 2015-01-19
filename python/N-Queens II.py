#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
注： 方法二的移位操作更直接。对于左斜线掩码只需将上一行的掩码左移一位即可。对于右斜线掩码，同样只需将上一行的掩码右移一位即可。

"""
class Solution:
    # @return an integer
    def totalNQueens(self, n):
        return self.__totalNQueens(n, 0, 0, 0, 0)
    
    # @param n, a integer response n-queue
    # @param m, a integer response rest rows of chessboard 
    # @param mark1, a mark response the used info of columns
    # @param mark2, a mark response the used info of left-oblique
    # @param mark3, a mark response the used info of right-oblique
    # @return the num of feasible solutions start from i-th row with current marks
    def __totalNQueens(self, n, i, mark1, mark2, mark3):
        if i>=n: return 1
        result = 0
        for j in xrange(n):
            # unused in column, left-oblique and right-oblique
            if (1<<j)&mark1==0 and (1<<(i+j))&mark2==0 and (1<<(i-j+n-1))&mark3==0:
                result += self.__totalNQueens(n, i+1, mark1|(1<<j), mark2|(1<<(i+j)), mark3|(1<<(i-j+n-1)))
        return result
    
    # @return an integer
    def totalNQueens1(self, n):
        return self.__totalNQueens1(n, 0, 0, 0, 0)
    
    # @param n, a integer response n-queue
    # @param i, a integer response i-th row of the chessboard
    # @param mark1, a mark response the used info of columns
    # @param mark2, a mark response the used info of right-oblique(main diagonal)
    # @param mark3, a mark response the used info of left-oblique(anti diagonal)
    # @return the num of feasible solutions start from i-th row with current marks
    def __totalNQueens1(self, n, row, mark1, mark2, mark3):
        if row>=n: return 1
        result, col = 0, 1<<(n-1)
        while col>0:
            # (mark1 | mark2 | mark3) response the used info for current row
            if col & ~(mark1 | mark2 | mark3) > 0:
                result += self.__totalNQueens1(n, row+1, mark1|col, (mark2|col)>>1, (mark3|col)<<1)
            col = col>>1
        return result

if __name__ == '__main__':
    pass
