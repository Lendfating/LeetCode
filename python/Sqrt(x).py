#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
原题没有考察小数点后的四舍五入，所以自己四舍五入之后反而会无法通过

主要思路可以归为两类：牛顿方法、二分查找、数据组合的思路。
牛顿方法：
    没的说，很经典，实验结果也是最快的。求导逼近。收敛速度明显比二分查找更快。主要是更新公式的计算，如下：
    目标是求 零点，目标函数：y = x^2-a (a为目标值，即题中的x)
        据此计算迭代公式，当 x=i时，y=i^2-a，此处的斜率为2x=2*i，根据斜率公式，求得此处切线方程为：2i=(y-(i^2-a))/(x-i)
        然后计算该切线与x轴的交点，结果为 x=(i^2+a)/(2*i)
        即得到i的迭代公式：j = (i+a/i)/2 即，(i+x/i)/2
    然后依次迭代，直到收敛即可
    
二分查找：因为开根号没有直接的计算方法，我们只知道结果在[0, x]区间内，所以我们就需要挨个试期间的那个数是最接近的一个。
    为了提高查询速度，很明显，我们可以通过二分查找优化。
    （只是单纯的用val/2迭代查找很不好，相比于二分查找，这样很难处理结果出现在中值有半部分的情况）
    
数据组合：考虑结果的二进制表示，有一串10串组成。我们可以考虑从高位到低位查看每一位是0还是1
    其实这种方法本质上跟二分查找是相通的，类似于区间树的思想。先找一个最大整数val(val*val<=x)，
    然后再在val的基础上添加某个值，使其更逼近结果。添加新值的时候，利用同样的思想。

"""
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        # binary search, find the first integer which's pow is bigger than x
        l, r = 0, x+1
        while l<r:
            mid = (l+r)>>1
            if mid*mid<=x:
                l = mid+1
            else:
                r = mid
        return l-1
        # note: following is rounding for decimal part
        if (l-0.5)*(l-0.5)<=x:  # [0.5, 1)
            return l
        else:               # [0, 0.5)
            return l-1
    
    # @param x, an integer
    # @return an integer
    def sqrt1(self, x):
        # use Newton method。
        i = 1.0
        while True:
            j = (i+x/i)/2.0
            if abs(i-j)<0.000000005:    # 0 as more as can
                break
            i = j
        return int(i)
    
    # @param x, an integer
    # @return an integer
    def sqrt2(self, x):
        # check every bit of the ans should be 1 from high to low
        ans, bit = 0, 1 << 15
        while bit>0:
            ans |= bit
            if ans*ans>x:
                ans ^= bit  # recover this bit
            bit >>= 1
        return ans

if __name__ == '__main__':
    pass
