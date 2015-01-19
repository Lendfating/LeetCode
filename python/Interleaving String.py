#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

仔细想想，会发现这个题很类似于编辑距离。
先写出递推公式，并采用递归的方式实现。然后再仔细分析，发现里面有很多重复计算的项，为了避免重复计算，参照编辑距离，
构造一个表格。每个位置表示从开始到当前位置是否可达。可达是指从上或者左可达，网格的每条线可以理解为一堵墙，
只会允许相同的字符通过，其他的会被过滤掉。

s3理解为我们有的一串钥匙，s1、s2为若干堵墙，相同的钥匙才能打开对应的门。因此，我们的目的就是利用现有的钥匙，
从左上角走到右下角。

"""
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        len_1, len_2, len_3 = len(s1), len(s2), len(s3)
        if len_1+len_2!=len_3: return False
        if len_1==0: return s2==s3
        if len_2==0: return s1==s3
        # one grid responses an room, we should check whether we can go to the
        # right_down room from left_upper one. We need check whether we can get
        # each room from left_upper with our keys.
        tables = [[True]*(len_2+1) for i in xrange(len_1+1)]
        for j in xrange(len_2): tables[0][j+1] = tables[0][j] and s2[j]==s3[j]
        for i in xrange(len_1):
            tables[i+1][0] = tables[i][0] and s1[i]==s3[i]
            for j in xrange(len_2):
                tables[i+1][j+1] = (tables[i+1][j] and s2[j]==s3[i+j+1]) or \
                                    (tables[i][j+1] and s1[i]==s3[i+j+1])
        return tables[len_1][len_2]

if __name__ == '__main__':
    s = Solution()
    print s.isInterleave("a", "b", "ab")
