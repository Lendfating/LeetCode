#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        # used binary search in second and first dimensionality
        if len(matrix)==0 or len(matrix[0])==0 or target<matrix[0][0] or target>matrix[len(matrix)-1][len(matrix[0])-1]:
            return False;
        low, high = 0, len(matrix);
        while high-low>1:
            mid = (low+high)/2;
            if matrix[mid][0]>target:
                high = mid;
            else:
                low = mid;
        left, right = 0, len(matrix[0])-1;
        while left<right:
            mid = (left+right)/2;
            if matrix[low][mid]>=target:
                right = mid;
            else:
                left = mid+1;
        return True if matrix[low][left]==target else False;
    
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix1(self, matrix, target):
        # don't treat it as a 2D matrix, just treat it as a common array
        # note: log(m*n)=log(m)+log(n), so it's same to the upper one
        if len(matrix)==0: return False;
        first, last, n = 0, len(matrix)*len(matrix[0])-1, len(matrix[0])
        while first<last:
            mid = (first+last)/2;
            if matrix[mid/n][mid%n]>=target:
                last = mid;
            else:
                first = mid+1;
        return True if matrix[first/n][first%n]==target else False;

if __name__ == '__main__':
    s = Solution()
    A = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
    print s.searchMatrix(A, 3)
    print s.searchMatrix(A, 8)
    print s.searchMatrix(A, 49)
    print s.searchMatrix(A, 58)
    print s.searchMatrix1(A, 3)
    print s.searchMatrix1(A, 8)
    print s.searchMatrix1(A, 49)
    print s.searchMatrix1(A, 58)
