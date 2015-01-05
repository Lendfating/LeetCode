#!/usr/bin/python  
# -*- coding: utf-8 -*-  

'''
Created on Nov 4, 2014

@author: Zhen
'''

"""
# problem
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?
Link: https://oj.leetcode.com/problems/rotate-image/

# solution：
方案一：从外向内，一层层旋转
方案二：先转置，再左右翻转

"""
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        """从外向内，一层层旋转
            A A A A B
            D       B
            D       B
            D       B
            D C C C C
            ! 如上图, 对每一层进行 A->B->C->D->A， 四个区域内的元素换位
        """
        for i in xrange(len(matrix)//2):    # 层数
            L = len(matrix)-2*i;
            for j in xrange(L-1):   # 每层内每个元素
                # A|B|C|D <-- D|A|B|C
                (matrix[i][i+j],    # A 区元素
                matrix[i+j][i+L-1], # B 区元素
                matrix[i+L-1][i+L-1-j],# C 区元素
                matrix[i+L-1-j][i]  # D 区元素
                )=(
                matrix[i+L-1-j][i], # D 区元素
                matrix[i][i+j],     # A 区元素
                matrix[i+j][i+L-1], # B 区元素
                matrix[i+L-1][i+L-1-j]);# C 区元素
        return matrix;
    
    def rotate1(self, matrix):
        """先转置，再左右对调。这个方法比较难想，用纸转动
        """
        # 矩阵转置
        for i in xrange(len(matrix)):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j];
        # 左右对调
        matrix = [row[::-1] for row in matrix];
        return matrix;
    
if __name__ == '__main__':
    A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];
    print A;
    s = Solution();
    s.rotate(A);
    s.rotate1(A);
    print A;