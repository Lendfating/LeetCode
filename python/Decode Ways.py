#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s)==0: return 0;
        nums = [1] * (len(s)+1);  # the num for the substr which start from i
        if s[len(s)-1]=='0': nums[len(s)-1]=0;
        for i in range(len(s)-1)[::-1]:
            if s[i]=='0':
                nums[i] = 0;
            elif s[i]=='1' or s[i]=='2' and s[i+1] in '0123456':
                nums[i] = nums[i+1] + nums[i+2];
            else:
                nums[i] = nums[i+1];
        return nums[0];
    
    # @param s, a string
    # @return an integer
    def numDecodings1(self, s):
        # 没有上面的那种思路清晰，对 0 的情况说不太清楚
        if len(s)==0 or s[0]=='0': return 0;
        prev, cur = 1, 1;
        for i in xrange(1, len(s)):
            if s[i]=='0': cur = 0;  # all depends on prev
            if not (s[i-1]=='1' or (s[i-1]=='2' and s[i]<='6')):
                prev = 0;   # all depends on cur
            cur, prev = prev + cur, cur;
        return cur;

if __name__ == '__main__':
    s = Solution();
    print s.numDecodings("12")
