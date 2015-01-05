#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
Ratings:
                    Peak
        Peak        |
        |           | |
      | |           | | |   
    | | | |       | | | | |       | | |
  | | | | | |   | | | | | | |     | | |
| | | | | | | | | | | | | | | | | | | |
                Candies:
1 2 3 4 5 3 2 1 2 3 5 4 3 2 1 1 1 2 1 1
x---a---x
        x--b--x    
        
如上图，原题的主要难点应该集中在山峰属于哪侧山坡。很明显应该是更长的那侧山坡。
可以采用两遍扫描（第一次从左往右，第二次从右往左），然后获得所有点的高度，然后在统计高度累计和。
或者一遍扫描，这时对上升山坡直接统计即可，对下降山坡，要统计山顶位置和悬崖落差。然后根据下降山坡的长度，及时修改下降山坡上点的高度。
"""
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if ratings is None or len(ratings)==0: return 0
        sum_candies, cur_candies, peak, fall = 1, 1, -1, 1000000
        for i in xrange(1, len(ratings)):
            if ratings[i]>ratings[i-1]: # “up” slopes
                cur_candies += 1
            elif ratings[i]==ratings[i-1]:  # “equal”， we can treat it as a new start
                cur_candies, peak, fall = 1, i-1, 1000000
            else:                       # “down” slopes
                if cur_candies>1:   # cliff point
                    peak, fall = i-1, cur_candies-1
                    cur_candies = 1
                else:               # update all the point in the "down" slopes
                    sum_candies += i-1-peak  # 
                    if fall==1: # update peak if no cliff in the "down" slopes
                        sum_candies += 1
                    else:
                        fall -= 1
            sum_candies += cur_candies
        return sum_candies
    
    # @param ratings, a list of integer
    # @return an integer
    def candy1(self, ratings):
        # get all points' height with two-pass scan
        heights = [1] * len(ratings)
        # First scan from left to right,
        # update the height of points in the "up" slopes
        for i in xrange(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                heights[i] = heights[i-1]+1
        # Second scan from right to left
        # update the height of points in the "down" slopes
        for i in xrange(len(ratings)-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                heights[i] = max(heights[i], heights[i+1]+1)    # take care of peak
        # sum the result
        return sum(heights)

if __name__ == '__main__':
    pass
