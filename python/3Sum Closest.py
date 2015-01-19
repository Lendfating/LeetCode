#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num = sorted(num)
        dis = 1000000
        for i in xrange(len(num)-2):
            dis = self.TwoSumClosest(num[i+1:], target-num[i], dis)
        return target+dis
    
    def TwoSumClosest(self, num, target, dis):
        i, j = 0, len(num)-1
        while i<j:
            if abs(num[i]+num[j]-target)<abs(dis): dis = num[i]+num[j]-target
            if num[i]+num[j]<target:
                i += 1
            else:
                j -= 1
        return dis
    

if __name__ == '__main__':
    s = Solution()
    print s.threeSumClosest([1,1,1,0], 100)
