#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<2: return 0
        profit = 0
        for i in xrange(1, len(prices)):
            profit += max(0, prices[i]-prices[i-1])
        return profit

if __name__ == '__main__':
    pass
