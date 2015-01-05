#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        self.sequence = []
        self.code = 0
        self.tigCode(n)
        return self.sequence;
    
    def tigCode(self, n):
        if n==0:
            self.sequence.append(self.code)
        else:
            self.tigCode(n-1)       # recursion 1
            self.code ^= 1<<(n-1)
            self.tigCode(n-1)       # recursion 2
            
    # @return a list of integers
    def grayCode1(self, n):
        # beautiful. translate recursion into loop
        # !important: recursion 2 is the reversed order of recursion 1
        sequence = [0]
        for i in xrange(0, n):
            for j in range(len(sequence))[::-1]:
                sequence.append(sequence[j]|(1<<i))
        return sequence
    
    # @return a list of integers
    def grayCode1(self, n):
        # 格雷码，和正常整数之间有相应的转换公式  y0=b0;yi=bi^bi-1(编号从左往右的话)
        sequence = []
        for i in xrange(1<<n):
            sequence.append(i^(i>>1))
        return sequence

if __name__ == '__main__':
    s = Solution()
    print s.grayCode(1)
    print s.grayCode(2)
    print s.grayCode1(1)
    print s.grayCode1(2)
