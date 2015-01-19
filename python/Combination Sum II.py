#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        # there is no guarantee that candidates is non-decrease 
        # note: there is duplicate in candidates, do there will be duplicate in result
        candidates = sorted(candidates)
        return self._combinationSum(candidates, target)
    
    def _combinationSum(self, candidates, target):
        result = []
        if self.binarySearch(candidates, target)>=0:
            result.append([target])
        for i in xrange(len(candidates)):
            if candidates[i]>target/2: break
            # use judge to avoid duplicate result
            if i>0 and candidates[i]==candidates[i-1]: continue
            # start from "i+1", so we will use candidates[i] only once
            sub_res = self._combinationSum(candidates[i+1:], target-candidates[i])
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
