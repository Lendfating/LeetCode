#!/usr/bin/python  
# -*- coding: utf-8 -*-  

'''
Created on Nov 6, 2014

@author: Zhen
'''
class Solution:
    # @return a string
    def countAndSay(self, n):
        seq = '1';
        for i in xrange(n-1):
            seq = self.generate(seq);
        return seq;
    
    def generate(self, seq):
        ans, tag, index = "", seq[0], 0;
        for i in xrange(1, len(seq)):
            if tag != seq[i]:
                ans += str(i-index) + tag;
                tag, index = seq[i], i;
        ans += str(len(seq)-index) + tag;
        return ans;
        
if __name__ == '__main__':
    s= Solution();
    print s.countAndSay(1);
    print s.countAndSay(5);
    