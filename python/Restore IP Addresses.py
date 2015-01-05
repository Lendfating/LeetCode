#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
注：这种递归，对结果数组进行拼接不如在底部拼接省事，每个递归中多一层循环！！！

"""
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        return self.splitString(s, 4);
    
    def splitString(self, s, n):
        if n<=0 or len(s)==0: return [];
        if n==1 and self.verify(s): return [s];
        result = [];
        for i in range(1,4):
            if self.verify(s[:i]):
                for postfix in self.splitString(s[i:], n-1):
                    result.append(s[:i]+"."+postfix);
        return result;
    
    def verify(self, s):
        if len(s)<=0: return False;
        if len(s)>1 and s[0]=='0': return False;
        return True if int(s)<=255 else False;

if __name__ == '__main__':
    s = Solution();
    print s.restoreIpAddresses("25525511135")
