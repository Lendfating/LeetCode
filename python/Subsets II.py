#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

知道这个问题区别于 Subsets I 的关键是重复值的处理。对重复值的出现情况进行分析可以发现，对重复元素不能
在前面所有元素的后都添加该元素（对于没有这个元素的，添加会当值跟前一个的结果重复），如下：
S = [1, 2, 2, 2]
subsets:
[]
[1]
[2], [1, 2]
[2, 2], [1, 2, 2]    !!! note: this 2 can only add to third line subsets
[2, 3, 2], [1, 2, 2, 2]    !!! note: this 2 can only add to fourth line subsets
因此，实现方式有两种，一种是每次记录上一行结果的开始位置，方便遇到重复元素时不从头开始；
另一种，我们发现第3-5行是对前面结果添加[1-3]个2形成的。因此，可以事先统计重复元素的个数，从而决定结果集中2可以重复几遍。

"""
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S = sorted(S)
        subsets, i, len_s = [[]], 0, len(S)
        while i<len_s:
            # [i, j) is the duplicates element of S[i]
            j = i+1
            while j<len_s and S[j]==S[i]: j += 1
            for k in range(len(subsets)):
                subsets += [subsets[k]+[S[i]]*l for l in xrange(1, j-i+1)]
            i = j   # skip the duplicates
        return subsets
    

if __name__ == '__main__':
    pass
