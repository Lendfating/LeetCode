#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit = 0;
        for i in xrange(2, len(prices)-2):
            max_profit = max(max_profit, \
                             self.maxProfitOneTran(prices[:i])+self.maxProfitOneTran(prices[i:]))
        return max_profit
        
    def maxProfitOneTran(self, prices):
        max_profit, start = -1000000, 0
        for i in xrange(1, len(prices)):
            max_profit = max(max_profit, prices[i]-prices[start])
            if prices[i]<=prices[start]:
                start = i
        return max_profit

if __name__ == '__main__':
    pass
