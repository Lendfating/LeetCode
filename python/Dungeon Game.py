#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

明显是动态规划的题目，采用滚动数组的方式进行实现。

"""
class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        row, colum = len(dungeon), len(dungeon[0])
        # initialize the health point for each state.
        hps = [1<<32]*(colum+1) # use max_int to set the board of right and bottom.
        hps[-2] = 1     # the least health point of the last position.
        # refresh health point value from right to left, bottom to up
        for i in range(row)[::-1]:
            for j in range(colum)[::-1]:
                # calculate the min health point for coming into current room.
                # Before go into bottom room, he need prepare hps[j] points, while
                # need hps[j+1] points before go into the right one. Find the smaller
                # one, and plus the cost at current room(-dungeon[i][j]), we will
                # get the health point which he should have before come into here.
                # What's more, he must have at least 1 health point at any time.
                hps[j] = max(min(hps[j], hps[j+1])-dungeon[i][j], 1)
        # hps[0] is the min start health point
        return hps[0]

if __name__ == '__main__':
    pass
