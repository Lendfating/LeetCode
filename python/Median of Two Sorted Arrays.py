#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
要达到O(lg(m+n))的时间复杂度，必须采用二分查找了。重点是如何在两个数组间结合二分查找
分析一下最终结果的状态，即 N-th 所在位置及特点：
    A [0, 1, ...., i-1] | [i, i+1, ..., m]
    B [0, 1, ...., j-1] | [j, j+1, ..., n]
如上图，假如 N-th 点在分界线处（min(A[i],B[j])），则我们很容易发现如上结果集{A，B}一定满足如下两条性质：
    (1) 左部分共有 N个元素。（i+j=N)
    (2) 所有左部分的元素都小于右部分的元素，（A[i-1]<=A[j] && B[j-1]<=A[i]）
由于要结合两个数组，因此我们可以采用一主一辅的策略。利用二分查找找 A 数组的分界点，B数组用来对A数组的每次查找结果进行校正。
利用B数组去校正A数组查找点时（两个数组结合的关键），要充分利用性质（1）、（2），由于有两个性质要控制，所以我们可以固定一个性质，
利用另一个性质作为反馈去修改对 A 中分界点的查找。因此对应的就有两种方法。
方法一：固定（2），根据（1）的反馈进行逼近 A 的分界点
    对A进行二分查找，找到分界点 val, 然后在B中找满足性质（2）的分界位置，然后判断条件（1）是否满足，并据此确定最终A的分界点在左边还是右边
方案二：固定（1），根据（2）的反馈进行逼近 A 的分界点
    对A进行二分查找，找到分界点val， 然后在B中找满足条件（1）的分界位置，然后判断条件（2）是否满足，并根据反馈对A进行下一步的查找
    
上面的方法采用了一主一辅的结合策略，还有一种方法就是对两个数组不分主辅，直接对两个数组融合二分查找的思想。
此时，充分利用 N 进行二分，而不是 m 和 n 去二分。先去掉N/2比结果小的，再去掉N/4, N/8 .....
"""
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l = (len(A)+len(B)-1)>>1
        r = (len(A)+len(B))>>1
        return (self.findNthSortedArrays(A, B, l) + self.findNthSortedArrays(A, B, r))/2.0
        
    # @param A, first sorted array
    # @param B, second sorted array
    # @param n, the index of the target item. it can be token as 0
    # @return the n-th element of A and B
    def findNthSortedArrays(self, A, B, n):
        mid, len_A, len_B = len(A)/2, len(A), len(B)
        if len_A==0: return B[n]
        if len_B==0: return A[n]
        index = self.binarySearch(B, A[mid])
        # !!! import, use mid+1 to avoid trap of exact division
        if mid+index == n:  # A[mid] is the n-th item
            return A[mid]
        elif mid+index > n: # the n-th item in the left part of A and B
            return self.findNthSortedArrays(A[:mid], B[:index], n)
        else:
            return self.findNthSortedArrays(A[mid+1:], B[index:], n-mid-1-index)
        
    def binarySearch(self, B, val):
        # find the index of the first item bigger than or equal val
        left, right = 0, len(B)
        while left<right:
            mid = (left+right)/2
            if val==B[mid]:
                return mid
            elif val<B[mid]:
                right = mid
            else:
                left = mid+1
        return left
    
    # @param A, first sorted array
    # @param B, second sorted array
    # @param n, the index of the target item. it can be token as 0
    # @return the n-th element of A and B
    def findNthSortedArrays1(self, A, B, n):
        if len(A)>len(B): return self.findNthSortedArrays1(B, A, n)
        if n>=len(A)+len(B): return 0
        left, right, len_A, len_B = max(0,n-len(B)), min(len(A),n+1), len(A), len(B)
        while left<right:
            mid = (left+right)/2
            index = n-mid       # the split index of B which suit (1)
            if (index==0 or A[mid]>=B[index-1]) and (index==len_B or mid==0 or B[index]>=A[mid-1]):
                return min(A[mid], B[index]) if index!=len_B else A[mid]    # avoid rock
            elif index==0 or A[mid]>=B[index-1]: # we can prove A[mid]>=B[index]
                right = mid
            else:       # B[index]>A[mid]
                left = mid+1    # !!! important, avoid trap
        return B[n-left]
    
    # @param A, first sorted array
    # @param B, second sorted array
    # @param n, the index of the target item. it can be token as 0
    # @return the n-th element of A and B
    def findNthSortedArrays2(self, A, B, n):
        if len(A)>len(B): return self.findNthSortedArrays2(B, A, n)
        if len(A)==0: return B[n]
        if n==0: return min(A[0], B[0])
        index_A = min(len(A)-1, n/2)
        index_B = min(len(B)-1,n-1-index_A)     # important: n-th not at index_B or index_A
        if A[index_A]>B[index_B]:
            return self.findNthSortedArrays2(A, B[index_B+1:], n-index_B-1)
        else:
            return self.findNthSortedArrays2(A[index_A+1:], B, n-index_A-1)


if __name__ == '__main__':
    pass
