#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

方案一：最直接的，将两轮交易切割为两部分，分别求每部分的最大交易，然后遍历切割条件，从而找到最优。
    为了加快速度，可以才有动态规划的方法记录两边子区间的最有交易结果。
    
方案二：从前往后扫描，用四个变量分别记录 “买入一次”，“卖出一次”，“买入两次”，“卖出两次”时的最大利润情况，
    然后从左往右扫描过程中，不断更新此值。
    我们只需要控制四个变量的计算顺序，即可以达到控制交易的顺序的目的。
    
    这种问题可以理解为带着历史状态的优化，（买入一次损失最小），（在前面买入一次，损失最小的前提下，再卖出一次，受益最大哦）。。。
    有点类似于找最大值，次大值的过程。

方案三：分析一下一轮交易的情况。假设子区间   【start, end】是一轮交易时的最大盈利区间，那么在二轮交易时，该区间会有两种情况。
    case 1: 区间【start, end】在结果的两个区间中。 那么另外一个区间一定在[:start] 或[end:]内，都找一下即可。
    case 2: 区间【start, end】不在结果的两个区间中。这种情况比较复杂，下面重点分析一下。
    很容易直到，结果的两个区间 [s1, e1], [s2, e2], 其中e1和s2一定在【start, end】。而且，s1=start, e2=end
    然后再想想，为什么会出现这种情况？为什么区间【start, end】不在结果的两个区间中呢？为什么要取[start, end]的两个小部分？
    显然，一定是因为[start, end]中间有一个很大的下降区间，由于这个区间的影响，导致end-start<e1-start+end-s2.

"""
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<2: return 0
        length = len(prices)
        # calculate the max profit of the interval of prices[:i+1]
        profits1, min_price = [0]*length, prices[0]
        for i in xrange(1, length):
            min_price = min(min_price, prices[i])
            profits1[i] = max(profits1[i-1], prices[i]-min_price)
        # calculate the max profit of the interval of prices[i:]
        profits2, max_price = [0]*length, prices[-1]
        for i in range(length-1)[::-1]:
            max_price = max(max_price, prices[i])
            profits2[i] = max(profits2[i+1], max_price-prices[i])
        # split prices into two interval, [:i] and [i+1:], and 
        # calculate the sum of the max profit of two interval.
        max_profit = profits2[0];
        for i in xrange(1, length-1):
            max_profit = max(max_profit, profits1[i]+profits2[i+1])
        return max_profit
            
    # @param prices, a list of integer
    # @return an integer
    def maxProfit1(self, prices):
        if len(prices)<2: return 0
        length = len(prices)
        # calculate the max profit of the interval of prices[:i+1]
        history_profits, min_price = [0]*length, prices[0]
        for i in xrange(1, length):
            min_price = min(min_price, prices[i])
            history_profits[i] = max(history_profits[i-1], prices[i]-min_price)
        # calculate the max profit of the interval of prices[i:]
        feture_profits, max_price, max_profit = [0]*length, prices[-1], history_profits[-1]
        for i in range(length-1)[::-1]:
            max_price = max(max_price, prices[i])
            feture_profits[i] = max(feture_profits[i+1], max_price-prices[i])
            max_profit = max(max_profit, history_profits[i]+feture_profits[i+1])
        return max_profit
    
    # @param prices, a list of integer
    # @return an integer
    def maxProfit2(self, prices):
        buy1, sale1, buy2, sale2 = -(1<<32), 0, -(1<<32), 0
        for price in prices:    # we have 0 money at begin.
            sale2 = max(sale2, buy2+price)  # if we just sale 2nd stock, it make profit of price
            buy2 = max(buy2, sale1-price)   # if we just buy 2nd stock, it make profit of -price
            sale1 = max(sale1, buy1+price)  # if we just sale 1st stock, it make profit of price
            buy1 = max(buy1, -price)        # if we just buy 1st stock, it make profit of -price
        return sale2    # sale will always bigger than sale1 
    
    # @param prices, a list of integer
    # @return an integer
    def maxProfit3(self, prices):
        profit, start, end = self.maxProfitOneTrade(prices)
        l_p, dummy, dummy = self.maxProfitOneTrade(prices[:start])
        r_p, dummy, dummy = self.maxProfitOneTrade(prices[end+1:])
        m_p, s2, e1 = self.maxProfitOneTrade(prices[start:end+1][::-1]) # don't use [end:start-1:-1] since start can be 0
        profit += max(l_p, r_p, m_p)
        return profit
        
    
    def maxProfitOneTrade(self, prices):
        if len(prices)<2: return 0, 0, len(prices)-1
        start, end, min_p, profit = 0, 0, 0, 0
        for i in xrange(len(prices)):
            if prices[i]<prices[min_p]: min_p = i
            if prices[i]-prices[min_p]>profit:
                start, end = min_p, i
                profit = prices[end]-prices[start]
        return profit, start, end

if __name__ == '__main__':
    s = Solution()
    print s.maxProfit3([1,2,4,2,5,7,2,4,9,0])
