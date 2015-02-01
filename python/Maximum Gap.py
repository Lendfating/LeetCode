#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

基本方案有两个，桶排序（基数排序），牌完或者不排完
方案一：直接基数排序，完全排序后，挨个查找最大间距。时间复杂度为 O(8n)，不知道算不算 O(n)，不过可以通过 oj

方案二：考虑到 num中的最大值和最小值，据此计算平均间距 aver_gap = (max-min)/(length-1)
        则，易知最大间距不会比平均间距小。然后，我们以aver_gap为间距进行分桶，将num分到 (length+1)桶中去，
        这样，每个桶内的 gap一定小于 aver_gap，即最大间距一定发生在桶间，因此，我们只需记录每个桶的最大值和最小值，
        然后依次统计相邻桶（中间可以有空桶）之间的 gap即可。

"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        # use bucket sort
        # initialize 16 buckets
        buckets = [[] for i in xrange(16)]
        # since integer has 32 bit, so we only need dispense and collect 8 times.
        for t in xrange(8): # Repeat 8 times
            bit = t*4       # the bit of active
            # Step 1. dispense num into buckets
            for val in num:
                buckets[val>>bit&0XF].append(val)
            # Step 2. collect num from buckets into num list.
            num = []
            for i in xrange(16):
                num.extend(buckets[i])
                buckets[i] = []
        # compare each successive elements, and get the max gap
        max_gap = 0
        for i in xrange(1, len(num)):
            max_gap = max(max_gap, num[i]-num[i-1])
        return max_gap
            
    # @param num, a list of integer
    # @return an integer
    def maximumGap1(self, num):
        if len(num)<2: return 0
        # use buckets[index][0] to store the max value in buckets[index]
        # and use buckest[index][1] to store the min value in buckets[index]
        max_val, min_val, length = max(num), min(num), len(num)
        buckets, aver_gap = [[] for i in xrange(length+1)], 1.0*(max_val-min_val)/(length-1)
        # split num into length buckets, with bucket gap (max_val-min_val)/(length-1)
        for val in num:
            index = int((val-min_val)/aver_gap)
            if len(buckets[index])==0:
                buckets[index] = [val, val]
            else:
                buckets[index][0] = min(buckets[index][0], val)
                buckets[index][1] = max(buckets[index][1], val)
        # calculate the max gap between neighbor buckets.
        max_gap, max_val = 0, buckets[0][1]
        for i in xrange(1, length):
            if len(buckets[i])>0:
                max_gap = max(max_gap, buckets[i][0]-max_val)
                max_val = buckets[i][1]
        return max_gap

if __name__ == '__main__':
    pass
