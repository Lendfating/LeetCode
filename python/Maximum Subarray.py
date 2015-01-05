#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum, sum = -1000000000, 0
        for item in A:
            sum = max(sum, 0) + item
            max_sum = max(max_sum, sum)
        return max_sum
    
    # @param A, a list of integers
    # @return an integer
    def maxSubArray1(self, A):
        maxSum, dump = self.subArray(A, None)
        return maxSum
    
    def subArray(self, A, side):
        # calculate maxSubArray and sum from one side
        if len(A)==0:
            return -1000000000, 0
        else:
            mid = len(A)/2
            l_sum, l_side_sum = self.subArray(A[:mid], 'right')
            r_sum, r_side_sum = self.subArray(A[mid+1:], 'left')
            max_side_sum, side_sum = 0, 0
            if side=='left':
                for item in A:
                    side_sum += item
                    max_side_sum = max(max_side_sum, side_sum)
            else:
                for item in A[::-1]:
                    side_sum += item
                    max_side_sum = max(max_side_sum, side_sum)
            return max(l_sum, r_sum, l_side_sum+A[mid]+r_side_sum), max_side_sum

if __name__ == '__main__':
    pass
