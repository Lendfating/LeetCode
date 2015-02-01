#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

读这个题明显感觉到应该属于贪心类的题，但是贪心策略一时没有想到。
方案一：
    令 G(i) = gas(i)-cost(i), 表示经过第 i个加油站，可以积累多少油。
    然后，令 R(i) = sum(G(0)+G(1)+...+G(i-1)), 表示从开始到第 i个油站时还剩多少油。
    分析 R(i)的变化曲线，我们应该想到，如果原问题存在有效解的话，应该在 R(i)的最低点处开始，这样从 i开始往后的点都在 x轴之上，即都可达。
    仔细分析一下，会发现这里面存在一个问题，因为该跑场是一个圆圈，因此R(i)会以 len为单位重复（相对位置重复），这样很有可能根本找不到全局最低点
    然后我们再想一下，因为只要跑一圈即可，所以我们并不需要找全局最低点，只要保证某个点在其接下来的 len长度内是最低的即可。
    最直接的想法是挨个遍历每一个点，看看其后续 len个点是否都不比它小。时间复杂度为 O(n^2)
    然后，进一步优化，采用双指针的方法，一个start一个end, start标记当前最小值，end作为扫描前进指针，期间保证 R(start...end)>=R(start)
    只要end-start>len，那么该start即可完成任务
    
方案二：
    基于方案一，为了降低空间复杂度，将G(i)和R(i)的记录值去掉，每次重新计算即可。
    
方案三：
    随便初始化一个起点和终点，判断能否从起点到达终点（累积中间的加油量和油消耗量），如果可以到达，那么再往后走一站看是否仍然可达；
    如果不可达，那么提前一站作为起点，看看能不能获得更多的油量积累。
    这种贪心策略比较简单直观，而且效果很好。能够一次性把所有的情况都尝试一遍。
    简单证明一下这个贪心策略的正确性：  ... p ... start ... end ...（p是最终结果点）
    由方案一知道，p是全局最小点（从p往后的一圈，累积油量都不会比p点低）。
    那么先证明end不会越过p。当end到达p时，由于p是全局最低点，因此此时的剩余油量一定为负数。因此，一定会移动start，从而end不会越过p。
    再证明start不会越过p。当start==p时，由于p是最终解，故此时一定可以跑完一圈，一次start不会再移动。
    
方案四：
    S[i] = Sum{ gas[i] - cost[i], for 0..i }
    S[n-1] should >=0
    for a new start point of t, say G[i] = SUM{ gas[i] - cost[i] for t..i }
    G[i] = S[i] - S[t-1] for i>=t
         = S[n-1] - S[t-1] + S[i] for i<t which >= S[i] - S[t-1]
    so find the t such that S[t-1] is minimal, so all S[i] - S[t-1] >=0

"""
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas)==0: retrun -1
        length = len(gas)
        # calculate the gain for each station
        gain = [gas[i]-cost[i] for i in range(length)]
        hold = [gain[0]]*(2*length) # start from 0, how much gas will remain.
        for i in xrange(1, 2*length): hold[i] = hold[i-1]+gain[i%length]
        # check for each point, point i has least gas between [i:i+length], so we can start at point i+1
        i, j =0, 0
        while i<length:
            while j<2*length and hold[j]>=hold[i]: j += 1
            # no equal here. equal response that sums(gas)<sums(cost)
            if j-i>length: return (i+1)%length
            i = j
        return -1
    
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit1(self, gas, cost):
        # an greed implement.
        length, start, end, remain = len(gas), 0, 0, 0
        while start<length:
            while end<2*length and remain>=0:
                remain += gas[end%length]-cost[end%length]
                end += 1
            # no equal here. response we must back to the start point here.
            if end-start>length: return start
            start, remain = end, 0
        return -1
    
    
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit2(self, gas, cost):
        end, start = 0, len(gas)-1
        remain = gas[start]-cost[start]
        while start>end:
            if remain>=0:
                # if have enough gas in the rank, go to next station
                remain += gas[end]-cost[end]
                end += 1
            else:   # no gas to arrive next station, so start early.
                start -= 1
                remain += gas[start]-cost[start]
        return start if remain>=0 else -1
    
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit3(self, gas, cost):
        remain, min_remain, min_index = 0, 1<<32, 0
        for i in xrange(len(gas)):
            remain += gas[i]-cost[i]
            if remain<min_remain:
                min_remain, min_index = remain, i
        return (min_index+1)%(len(gas)) if remain>=0 else -1
    

if __name__ == '__main__':
    pass
