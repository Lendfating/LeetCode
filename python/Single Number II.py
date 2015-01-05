#!/usr/bin/python  
# -*- coding: utf-8 -*- 
import random

"""
# soluction
很遗憾，是三个的数群中夹杂着一个一个的，如果是两个的数群中夹杂着一个一个的，直接用异或操作即可。
3个的数群中夹杂1个的数的话，通过求雨判断异常区间，二分查找。时间复杂度： n+n/2+n/4.。。。是常数
方案一：
    二分查找：查找过程中，对原数组部分排序，使左右子树相对有序。时间复杂度：n+n/2+n/4+...... = O(n)
    但是提交时不能使用 random，故无法验证
方案二：
    位操作。以位为单位去思考问题，[0 0 0 1 1 1 x], 每个位都是有3m个0，3n个1，我们期望通过一系列的位操作，过滤掉这些0和1，剩余最终的x
    基本方法——统计法，将每位的数值加和，然后对3求余，所得即为 x 
    位操作技巧——通过集中位操作，综合搭配获得x。如，我可以在每位通过位运算模仿三进制加法。

"""
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        left, right = 0, len(A)-1;
        while left<right:
            seed = random.randint(left, right);
            A[left], A[seed] = A[seed], A[left];
            cur, l, r = A[left], left, right;
            while l<r:
                while l<r and A[r]>cur: r -= 1;    # pay attention to case =
                A[l] = A[r];
                while l<r and A[l]<=cur: l += 1;
                A[r] = A[l];
            A[l] = cur;
            if (l+1-left)%3==1:   # the except num in the left part
                right = l;
            else:   # the except num in the right part
                left = l+1;
        return A[left];
    
    # @param A, a list of integer
    # @return an integer
    def singleNumber1(self, A):
        # count the number of 1 in each bit, and use it to restore X
        count, result = [0] *32, 0;
        for item in A:
            for i in range(32):
                count[i] += (item>>i) & 1;
        for i in range(32):
            if count[i]%3==1:
                result |= 1<<i;
        return result if result<0x80000000 else result-0x100000000; # python error for negative
    
    # @param A, a list of integer
    # @return an integer
    def singleNumber2(self, A):
        # use bit manipulation to filter 3m of 0 and 3n of 1
        high_bit, low_bit = 0, 0;
        for item in A:
            # Simulate the ternary addition
            low_bit ^= item;    # new low bit
            high_bit |= (~low_bit) & item;  # Isopsephy
            temp = ~(high_bit & low_bit);   # reach to 3
            low_bit &= temp;
            high_bit &= temp;
        return low_bit;
    
    # @param A, a list of integer
    # @return an integer
    def singleNumber3(self, A):
        # use bit manipulation to filter 3m of 0 and 3n of 1
        high_bit, low_bit = 0, 0;
        for item in A:
            # Simulate the ternary addition
            low_bit = (low_bit ^ item) & ~high_bit;
            high_bit = (high_bit ^ item) & ~low_bit;    # depth thinks
        return low_bit;

if __name__ == '__main__':
    A = [-2,-2,1,1,-3,1,-3,-3,-4,-2]#[1,2,3,1,2,5,3,3,2,1]
    s = Solution()
    print s.singleNumber(A)
    print s.singleNumber1(A)
    print s.singleNumber2(A)
    print s.singleNumber3(A)
