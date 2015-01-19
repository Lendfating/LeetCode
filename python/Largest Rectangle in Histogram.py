#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.insert(0,0)
        height.append(0)
        lefts, max_area = [0], 0
        for i in xrange(1, len(height)):
            while height[i]<height[lefts[-1]]:
                top = lefts.pop()
                max_area = max(max_area, height[top]*(i-lefts[-1]-1))
            lefts.append(i)
        return max_area

if __name__ == '__main__':
    pass
