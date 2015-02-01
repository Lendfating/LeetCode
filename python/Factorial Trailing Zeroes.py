#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

编程之美原题，统计从 1~n中有几个5，有几个5就会有几个0.
然后用n/5，表示1~n中5的倍数的数的个数， 对结果贡献一个 0
n/5/5，表示1~n中25的倍数的数的个数，对结果再贡献 一个 0
。。。。
最后得到的即可统计得到一共有多少个5

"""
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        counts = 0
        while n>0:
            counts += n/5
            n = n/5
        return counts

if __name__ == '__main__':
    pass
