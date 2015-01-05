#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
广搜。从上下左右四个边界往里走，凡是能碰到的'O' ，都是跟边界接壤的，应该保留。

注意，本地的 python 跟服务器的不太一样，所以字符串在本地直接改是不可以的
"""
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board)<3: return;
        high, width = len(board), len(board[0]);
        for i in range(high):
            if board[i][0]=='O': self.bfs(board, i, 0);
            if board[i][width-1]=='O': self.bfs(board, i, width-1);
        for j in range(width):
            if board[0][j]=='O': self.bfs(board, 0, j);
            if board[high-1][j]=='O': self.bfs(board, high-1, j);
        for i in range(high):
            for j in range(width):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                elif board[i][j]=='B':
                    board[i][j] = 'O'
        
    def bfs(self, board, i, j):
        high, width, queue = len(board), len(board[0]), [];
        board[i][j] = 'B'
        queue.append((i,j));
        while len(queue)>0:
            (i,j) = queue.pop(0);
            nexts = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)];   # left -> up -> right -> down
            for (i, j) in nexts:
                if i>=0 and i<high and j>=0 and j<width and board[i][j]=='O':
                    board[i][j] = 'B'
                    queue.append((i,j));
        
        """
        status = [[False] * len(row) for row in board];
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O' and not status[i][j] and self.isSurrounded(board, status, i, j):
                    self.capture(board, i, j);
                    
    
    # @param board, a 2D array
    # @param status, a 2D array for whether checked or not 
    # @param i, j, the position to be checked
    # check the postion has been surrounded or not
    def isSurrounded(self, board, status, i, j):
        status[i][j], ret = True, True;
        if j<=0 or (board[i][j-1]=='O' and not status[i][j-1] and not self.isSurrounded(board, status, i, j-1)):
            ret = False;
        if i<=0 or (board[i-1][j]=='O' and not status[i-1][j] and not self.isSurrounded(board, status, i-1, j)):
            ret = False;
        if j>=len(board[0])-1 or (board[i][j+1]=='O' and not status[i][j+1] and not self.isSurrounded(board, status, i, j+1)):
            ret = False;
        if i>=len(board)-1 or (board[i+1][j]=='O' and not status[i+1][j] and not self.isSurrounded(board, status, i+1, j)):
            ret = False;
        return ret;
    
    # @param board, a 2D array
    # @param i, j, the position to be capture
    # capture all point in next to (i,j)
    def capture(self, board, i, j):
        board[i] = "" + str(board[i][:j]) + "X" + str(board[i][j+1:]);
        if j>0 and board[i][j-1]=='O':  # left
            self.capture(board, i, j-1);
        if i>0 and board[i-1][j]=='O':# up
            self.capture(board, i-1, j);
        if j<len(board[0])-1 and board[i][j+1]=='O':# right
            self.capture(board, i, j+1);
        if i<len(board)-1 and board[i+1][j]=='O':   # down
            self.capture(board, i+1, j);
    """
if __name__ == '__main__':
    A = ["XOXOOOO","XOOOOOO","XOOOOXO","OOOOXOX","OXOOOOO","OOOOOOO","OXOOOOO"]
#["XOXOXOOOXO","XOOXXXOOOX","OOOOOOOOXX","OOOOOOXOOX","OOXXOXXOOO","XOOXXXOXXO","XOXOOXXOXO","XXOXXOXOOX","OOOOXOXOXO","XXOXXXXOOO"]
    #["OXOOOOOOO","OOOXOOOOX","OXOXOOOOX","OOOOXOOOO","XOOOOOOOX","XXOOXOXOX","OOOXOOOOO","OOOXOOOOO","OOOOOXXOO"]
    #["XXXXX","XOOOX","XXOOX","XXXOX","XOXXX"];#["XXX","XOX","XXX"];#["XXXX","XOOX","XXOX","XOXX"];
    s = Solution();
    print A;
    s.solve(A);
    print A;
