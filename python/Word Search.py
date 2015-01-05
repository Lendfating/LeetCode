#!/usr/bin/python  
# -*- coding: utf-8 -*-  

'''
Created on Nov 18, 2014

@author: Zhen
'''
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # 该问题有点像贪吃蛇，使用类似贪吃蛇的思路去解决一下
        if len(word)==0: return True;
        if len(board)==0: return False;
        rows, cols = len(board), len(board[0]);
        mark = [[ False for item in row] for row in board];
        # 循环遍历
        for i in xrange(rows):
            for j in xrange(cols):
                if self.checkFromFixedPoint(i, j, board, mark, word):
                    return True;
        return False;
    
    
    # @param i,j, the position of start of the word
    # @param board, the char board
    # @param mark, a list of lists of bool value, which show whether it is used or not.
    # @param word,a string
    # @return boolean
    def checkFromFixedPoint(self, i, j, board, mark, word):
        # 从固定点开始寻找该word是否存在与该board中
        if board[i][j]==word[0]:
            if len(word)==1:    # word没有子串时，递归终止
                return True;
            # 当前位置匹配正常，则向四周递归
            rows, cols, mark[i][j] = len(board), len(board[0]), True;
            # 向左侧递归
            if j>0 and not mark[i][j-1] and self.checkFromFixedPoint(i, j-1, board, mark, word[1:]):
                return True;
            # 向上侧递归
            if i>0 and not mark[i-1][j] and self.checkFromFixedPoint(i-1, j, board, mark, word[1:]):
                return True;
            # 向右侧递归
            if j<cols-1 and not mark[i][j+1] and self.checkFromFixedPoint(i, j+1, board, mark, word[1:]):
                return True;
            # 向下侧递归
            if i<rows-1 and not mark[i+1][j] and self.checkFromFixedPoint(i+1, j, board, mark, word[1:]):
                return True;
            # 四周的递归都失败，则要先将标记恢复常态
            mark[i][j] = False;
            return False;
        else:
            # 当前位置和word首位不匹配
            return False;
        
    # 该问题其实是深度优先遍历。感觉这份代码比上边的整洁
    def dfs(self, i, j, board, visited, word):
        if len(word)==0:    # 检查完
            return True;
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]): # 越界，剪枝
            return False;
        if board[i][j]!=word[0]: # 不相等，剪枝
            return False;
        if visited[i][j]: # 已访问，剪枝
            return False;
        
        visited[i][j] = True;   # 按 左 -> 上 -> 右 -> 下 的顺序进行递归
        ret = self.dfs(i, j-1, board, visited, word[1:]) or \
              self.dfs(i+1, j, board, visited, word[1:]) or \
              self.dfs(i, j+1, board, visited, word[1:]) or \
              self.dfs(i+1, j, board, visited, word[1:]); 
        visited[i][j] = False;
        return ret;
        
        
    
if __name__ == "__main__":
    board = [
                "ABCE",
                "SFCS",
                "ADEE"
            ];
    s = Solution();
    print s.exist(["aa"], "aa");
    print s.exist(board, "ABCCED")
    print s.exist(board, "SEE")
    print s.exist(board, "ABCB")
    
    
    