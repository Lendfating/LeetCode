#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

满目疮伤……………………

本打算在每一步选最少候选number的位置进行填充，但是这样会在每一步引入81*9的复杂度。得不偿失。
所以直接按循序从前往后选择下一个即可。
"""
class Candidates:
    # maintain the information about candidates
    def __init__(self, board):
        self.board = [[int(ch) if ch!="." else 0 for ch in row] for row in board]
        self.marks = [[0]*9, [0]*9, [0]*9]   # row, colum, sqr
        self.counts = 0
        for i in xrange(9):
            for j in xrange(9):
                if self.board[i][j]==0: continue
                self.marks[0][i] |= 1<<self.board[i][j]
                self.marks[1][j] |= 1<<self.board[i][j]
                self.marks[2][i/3*3+j/3] |= 1<<self.board[i][j]
                self.counts += 1
        
    def getOptPosit(self):
        opt_i, opt_j, opt_counts =-1, -1, 9
        for i in xrange(9):
            for j in xrange(9):
                if self.board[i][j]>0: continue
                counts = self.getNumbersCount(i, j)
                if counts<opt_counts:
                    opt_counts, opt_i, opt_j = counts, i, j
        return (opt_i, opt_j)
                
    def getNumbers(self, i, j):
        mark = self.marks[0][i] | self.marks[1][j] | self.marks[2][i/3*3+j/3]
        return ([i for i in range(1,10) if mark&(1<<i)==0])
    
    def getNumbersCount(self, i, j):
        mark = self.marks[0][i] | self.marks[1][j] | self.marks[2][i/3*3+j/3]
        return sum([1 for i in range(1,10) if mark&(1<<i)==0])
        
    def addNumber(self, i, j, num):
        self.board[i][j] = num
        self.marks[0][i] |= 1<<self.board[i][j]
        self.marks[1][j] |= 1<<self.board[i][j]
        self.marks[2][i/3*3+j/3] |= 1<<self.board[i][j]
        self.counts += 1
        
    def recover(self, i, j):
        self.marks[0][i] &= (1<<10-1-1<<self.board[i][j])
        self.marks[1][j] &= (1<<10-1-1<<self.board[i][j])
        self.marks[2][i/3*3+j/3] &= (1<<10-1-1<<self.board[i][j])
        self.board[i][j] = 0
        self.counts -= 1
        
    # @return a boolean
    def isValid(self):
        return self.counts==81
    
    def copy2Board(self, board):
        for i in xrange(9):
            board[i] = "".join(self.board[i])
        return board
    
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        # 这个方法每次为了查找最优候选位置，每次最少需要最少再查找额外的9*3个位置的更新情况，并比较最小值。
        # 带来额外代价比潜在的优化效果（潜在剪枝）更严重，因此该方法的时间复杂度更大，不足取。
        cand = Candidates(board)
        if self._solveSudoku(cand):
            board = cand.copy2Board(board)
    
    def _solveSudoku(self, cand):
        (i, j) = cand.getOptPosit() # 81
        if i<0: return cand.isValid()   # 1
        nums = cand.getNumbers(i, j)    # 9
        for num in nums:    # <9
            cand.addNumber(i, j, num)   # 3
            if self._solveSudoku(cand): return True
            cand.recover(i, j)  # 3
        return False
    
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku1(self, board):
        marks = [[0]*9, [0]*9, [0]*9]   # row, colum, sqr
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j]!=".":
                    self.modifyMark(marks, i, j, int(board[i][j]))
        self.__solveSudoku(board, marks, 0)
            
    def __solveSudoku(self, board, marks, start):
        for k in xrange(start, 81):
            if board[k/9][k%9]==".": break
        else:
            return True
        i, j = k/9, k%9
        mark = marks[0][i] | marks[1][j] | marks[2][i/3*3+j/3]
        for num in xrange(1, 10):
            if mark & (1<<num)==0:
                board[i] = board[i][:j]+str(num)+board[i][j+1:]
                self.modifyMark(marks, i, j, num)
                if self.__solveSudoku(board, marks, k+1): return True
                self.modifyMark(marks, i, j, num)
        board[i] = board[i][:j]+"."+board[i][j+1:]
        return False
        
    def modifyMark(self, marks, i, j, num):
        marks[0][i] ^= 1<<num
        marks[1][j] ^= 1<<num
        marks[2][i/3*3+j/3] ^= 1<<num
    
if __name__ == '__main__':
    s = Solution()
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    s.solveSudoku1(board)
    print board
