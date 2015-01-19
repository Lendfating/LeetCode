#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        for i in range(len(num))[::-1]:
            if i>0 and num[i]>num[i-1]:
                for j in range(i, len(num))[::-1]:
                    if num[j]>num[i-1]: break
                num[i-1], num[j] = num[j], num[i-1]
                break
        # important: just reverse num[i:] id ok, because num[i:] is non-increasing
        l, r = i, len(num)-1
        while l<r:
            num[l], num[r] = num[r], num[l]
            l, r = l+1, r-1
        return num
    
        

if __name__ == '__main__':
    pass
