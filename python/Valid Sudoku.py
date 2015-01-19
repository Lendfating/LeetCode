#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        marks1 = [[0]*9, [0]*9, [0]*9]   # row, colum, gong
        marks2 = [[0]*9, [0]*9, [0]*9]   # row, colum, gong
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j]==".": continue
                mark = 1<<int(board[i][j])
                marks2[0][i] |= mark & marks1[0][i]
                marks2[1][j] |= mark & marks1[1][j]
                marks2[2][i/3*3+j/3] |= mark & marks1[2][i/3*3+j/3]
                marks1[0][i] |= mark
                marks1[1][j] |= mark
                marks1[2][i/3*3+j/3] |= mark
        for i in xrange(3):
            for j in xrange(9):
                if marks2[i][j]>0: return False
        return True
    
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku1(self, board):
        marks = [[0]*9, [0]*9, [0]*9]   # row, colum, sqr
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j]==".": continue
                mark = 1<<int(board[i][j])
                if (mark & marks[0][i]) or (mark & marks[1][j]) or (mark & marks[2][i/3*3+j/3]):
                    return False
                marks[0][i] |= mark
                marks[1][j] |= mark
                marks[2][i/3*3+j/3] |= mark
        return True

if __name__ == '__main__':
    s = Solution()
    board = ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
    print s.isValidSudoku(board)
    print s.isValidSudoku1(board)
