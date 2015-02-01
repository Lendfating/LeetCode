#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

编程之美上面的题。

第二种方法，实现快排时要注意，因为这个数组中有大量重复数据，故快排的性能会很差，因此一般情况下应该考虑如果剪枝（只要子数组全部为同一值，立马结束循环过程）
，当然，也可以把第46行代码处的“=”去掉，这样左右子树会平衡一些，效果可能会好一些。
剪枝并不好减~~~

最后还有一个人用位操作，统计所有数中 1~32位上面出现的1的个数和0的个数，据此判断最终结果在此位是 1 还是 0，就不实现了。

"""
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        # convert this problem into a small one by deleting two different elements.
        # we can prove that the majority element still in the rest sets.
        candidate, counts = None, 0
        for val in num:
            if counts==0:
                candidate, counts = val, 1
            elif val==candidate:
                counts += 1
            else:
                counts -= 1
        return candidate
    
    # @param num, a list of integers
    # @return an integer
    def majorityElement1(self, num):
        # take full use of the idea of quick sort. But we needn't sort all the array,
        # we only sort the middle part of each level, and end once we get the middle
        # value in the whole array.
        # note: the middle of the whole array must be the majority element, not the 
        # element in the right half part.
        left, right, mid = 0, len(num)-1, len(num)/2
        while left<right:
            val, l, r = num[left], left, right
            while l<r:
                while l<r and num[r]>val: r -= 1
                if l<r: num[l], l = num[r], l+1
                while l<r and num[l]<val: l += 1    # no equal here. because many elements is same, it can make left and right balance.
                if l<r: num[r], r = num[l], r-1
            num[l] = val
            if l==mid:
                return num[l]
            elif l<mid:
                left = l+1
            else:
                right = l-1
        return num[left]
    

if __name__ == '__main__':
    s = Solution()
   