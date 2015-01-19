#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # there is no guarantee that candidates is non-decrease 
        # note: there is no duplicate in candidates, so there will no duplicate in result
        candidates = sorted(candidates)
        return self._combinationSum(candidates, target)
    
    def _combinationSum(self, candidates, target):
        result = []
        if self.binarySearch(candidates, target)>=0:
            result.append([target])
        for i in xrange(len(candidates)):
            if candidates[i]>target/2: break
            # start from "i", so we can reuse candidates[i] for many times
            sub_res = self._combinationSum(candidates[i:], target-candidates[i])
            for sub in sub_res:
                sub.insert(0, candidates[i])
                result.append(sub)
        return result
    
    def binarySearch(self, candidates, target):
        l, r = 0, len(candidates)
        while l<r:
            mid = (l+r)/2
            if candidates[mid]==target:
                return mid
            elif candidates[mid]>target:
                r = mid
            else:
                l = mid+1
        return -1

if __name__ == '__main__':
    pass
