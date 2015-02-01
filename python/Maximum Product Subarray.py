#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

分析一下整个过程，明显是一个动态规划的题，明显不想使用O(n)的空间，所以想办法一次扫描直接累计得到最大结果。
那就分析一下计算的过程。
    这个与加法的区别就是负数可以变号，将曾经最小的变为最大的。所以，我们可以统计最小值和最大值，然后如果是负数的话，
    会将最小值变为最大值，否则按正常情况更新最小、最大值即可。
    此外，要特别注意0的情况。0应该理解为新的起点。
对应的方案有三种：
方案一：0将结果清空，故可以理解为0将原数组切分成更小的子问题。
        然后，对每个独立子问题，我们标记第一次负号出现的位置，这样我们累计两个连乘积：从开始到现在，从第一个负数的下一个位置到现在，
        设这两个结果分别为 P1 和 P2，则无论何时，P1和P2中一定会有一个是正数，有可能最最终结果有价值。
        
方案二：统计到目前为止的最大值和最小值，利用当前值去更新最大值和最小值，然后再更新 结果。
        实现一、每次最大值、最小值都会取自 max*val, min*val, val 三者中的一个。（加入val是考虑0后重新开始）
        实现二、如果负数，交换最大最小值。然后 最大值取自 max*val, val, 最小值取自：min*val, val
        
方案三：从两边扫描，累积连乘积，这样即使某个abs最大值在左方向没有算到，那么在有方向也会算到.
        因为每一部分内，结果一定以某个负数分割，在左半部分或者有半部分内。即最终子串或者从起点开始，或者以终点结尾。

"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A)==0: return 0
        product1, product2, result, tag = 1, 1, -(1<<32), False
        for val in A:
            # 0 can split A into two separate parts
            if val==0:
                result = max(0, result)
                product1, product2, tag = 1, 1, False
                continue
            # the accumulate product from the start
            product1 *= val
            result = max(product1, result)
            if tag:
                # the accumulate product from first sign reversal
                product2 *= val
                result = max(product2, result)
            # reverse sign from next item
            if not tag and val<0: tag = True
        return result
            
    # @param A, a list of integers
    # @return an integer
    def maxProduct1(self, A):
        max_prod, min_prod, result = 1, 1, -(1<<32)
        for val in A:
            # the max product and min product of the sub-array ending at current position
            # can be achieved from next three number
            a = max_prod*val
            b = min_prod*val
            c = val
            # update the max product and min product
            max_prod = max(a, b, c)
            min_prod = min(a, b, c)
            # use max product to update result
            result = max(result, max_prod)
        return result
    
    # @param A, a list of integers
    # @return an integer
    def maxProduct2(self, A):
        max_prod, min_prod, result = 1, 1, -(1<<32)
        # calculate the max product for the sub-array ending with current number
        for val in A:
            # negative number will swap the max product and min product
            if val<0: max_prod, min_prod = min_prod, max_prod
            # update max product and min product
            max_prod = max(val, max_prod*val)   # val denotes new start after 0
            min_prod = min(val, min_prod*val)
            # update result
            result = max(result, max_prod)
        return result
    
    # @param A, a list of integers
    # @return an integer
    def maxProduct3(self, A):
        # scan from left and right
        left, right, result, length = 1, 1, -(1<<32), len(A)
        for i in xrange(length):
            left, right = left*A[i], right*A[length-1-i]
            result = max(result, left, right)
            if A[i]==0: left = 1        # new start
            if A[length-1-i]==0: right = 1
        return result

if __name__ == '__main__':
    pass
