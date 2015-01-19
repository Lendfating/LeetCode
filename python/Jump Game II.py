#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A)<=1: return 0  # for case: A=[1]
        edge, next_edge, step, len_A = 0, 0, 0, len(A)
        for i in xrange(len_A):
            if i>edge:  # with step can't reach i, so use step+1
                edge, step = next_edge, step+1
                # if next step can also not reach i, so i will not be reached.
                if i>edge: return -1
            if i+A[i]>next_edge:
                next_edge = i+A[i]  # update next step's edge info with A[i]
                if next_edge>=len_A-1: return step+1    # next step can reach end
        return step   # in this case, we have reach end
        
if __name__ == '__main__':
    pass
