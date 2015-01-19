#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if n<k or k<1 or n<1: return []
        if k==1: return [[i] for i in xrange(1, n+1)]
        result = []
        for i in xrange(n, k-1, -1):
            sub = self.combine(i-1, k-1)
            for part in sub:
                part.append(i)
                result.append(part)
        return result
    
    # @return a list of lists of integers
    def combine1(self, n, k):
        # C(n, k) = C(n-1, k-1) + [n + C(n-1, k)]
        if n<k or k<1 or n<1: return []
        result = self.combine(n-1, k-1)
        if len(result)==0:
            result.append([n])
        else:
            for i in xrange(len(result)):
                result[i].append(n)
        result.extend(self.combine(n-1, k))
        return result

if __name__ == '__main__':
    pass
