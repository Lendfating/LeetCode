#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 4, 2014

@author: Zhen
'''

"""
# problem
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
Link: https://oj.leetcode.com/problems/maximal-rectangle/

# solution
方法一：暴利，枚举所有极大矩形，然后找出面积最大者。因为极大矩形有两种发现策略，对应的就有两种便利策略。
    1. 根据矩形的左上角位置发现极大矩形。并据此进行遍历。如果细心，我们会发现，这个方法遍历的并不都是极大矩阵，但是影响并不大。
    2. 根据矩形的最短腰发现极大矩形（我们发现，一个极大矩形都会有一个短板--即腰部），然后通过这种腰部进行矩形的发现与遍历。
    两种方法都会频繁的用到横向长度信息，因此需要利用动态规划的方法提前准备所有的横向长度信息。很明显，两种方法的效率都不怎么高，应该是O(M*N*M)，应该尝试利用剪枝法降低时间复杂度。
    
方法二：问题拆分，可以将该问题看作是 N 个 Largest Rectangle in Histogram 的合并。通过将每一行看做一个Histogram，然后该问题就可以拆解。

"""
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        """暴利求解法之瘦腰遍历
        """
        # slices 切片值表示从当前点右边连续1的个数
        slices = [[int(item) for item in row] for row in matrix];
        for i in xrange(len(matrix)):
            for j in range(len(matrix[0])-1)[::-1]:
                if matrix[i][j]=='0':
                    slices[i][j] = 0;
                else:
                    slices[i][j] = slices[i][j+1]+1;
        max = 0;
        # 根据slices切片值进行最大切片统计
        for i in xrange(len(slices)):
            for j in xrange(len(slices[i])):
                high = 1;
                # 向上查找顶部
                for k in xrange(i-1, -1, -1):
                    if slices[k][j]>=slices[i][j]:
                        high += 1;
                    else:
                        break;
                # 向下查找底部
                for k in xrange(i+1, len(slices)):
                    if slices[k][j]>=slices[i][j]:
                        high += 1;
                    else:
                        break;
                # 比较判断
                if high*slices[i][j]>max:
                    max = high*slices[i][j];
        return max;
    
    def maximalRectangle1(self, matrix):
        """利用 Largest Rectangle in Histogram 的思路进行求解
        Link: http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
        """
        cols = len(matrix[0]) if len(matrix)>0 else 0;
        his, ans = [0] * (cols+1), 0;
        for row in matrix:
            stack = []; # 存储的是递增柱的下标。意义，两个元素之间的缺省的数据都比后面的高
            for i in xrange(cols+1):
                # 统计 Histogram 高度，如当前内容为‘0’，则清空高度。
                his[i] = his[i]+1 if i<cols and row[i]=='1' else 0;
                # 利用 Largest Rectangle in Histogram 算法求解Histogram最大矩形
                while len(stack) and his[i]<his[stack[-1]]:
                    top = stack.pop();
                    # 注意，当前top对应的his，比所有已弹出的、目前栈顶之后的元素都小。
                    left_index = stack[-1]+1 if len(stack) else 0;
                    ans = max(ans, (i-left_index)*his[top]);
                stack.append(i);
        return ans;
        
                    
    
if __name__ == '__main__':
    A=[['0','1','1'],['1','1','1']];
    s=Solution();
    print s.maximalRectangle(A);
    print s.maximalRectangle1(A);