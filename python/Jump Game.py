#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A)==0: return False
        board, len_A = 0, len(A)
        for i in xrange(len_A):
            if board<i: return False
            board = max(board, i+A[i])
            if board>=len_A-1: return True
        return True

if __name__ == '__main__':
    pass
