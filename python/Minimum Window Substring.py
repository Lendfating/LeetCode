#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

两种方法思想差不多，之所以用第二种在实现一遍，是因为第二个更加明确这是一个 双指针 的题目。
所以双指针，就是动态维护一个区间。尾指针不断往后扫，当扫到有一个窗口包含了所有 T 的字符后，
然后再收缩头指针，直到不能再收缩为止。最后记录所有可能的情况中窗口最小的。

"""
class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(T)==0: return ""
        counts, mark = {}, 0
        for ch in T:
            if not counts.has_key(ch):
                counts[ch] = 1
            else:
                counts[ch] += 1
            mark |= 1<<(ord(ch))
        starts, opt_len, opt_start = [], len(S)+1, 0
        for i in xrange(len(S)):
            if counts.has_key(S[i]):
                starts.append(i)
                counts[S[i]] -= 1
                # note: for each char, whose counts==0 only occur once at next line.
                if counts[S[i]]==0: mark ^= 1<<(ord(S[i]))
                if mark==0: # get one substring
                    while counts[S[starts[0]]]<0:
                        counts[S[starts[0]]] += 1
                        starts.pop(0)
                    if i-starts[0]<opt_len:
                        opt_len, opt_start = i-starts[0], starts[0]
        if opt_len<len(S)+1:    # have opt result
            return S[opt_start:opt_start+opt_len+1]
        else:
            return ""
        
    # @return a string
    def minWindow1(self, S, T):
        # use two to maintain a interval [start, end], shift end to scan S, 
        # once [start, end] contain T, shift start to shrink the interval.
        if len(T)==0: return ""
        if len(S)<len(T): return ""
        counts, requires = [0]*128, [False]*128
        for ch in T:
            counts[ord(ch)] += 1
            requires[ord(ch)] = True
        min_len, min_start = len(S)+1, 0
        start, appeared = 0, 0  # the count of char in T has occur
        for end in xrange(len(S)):
            if requires[ord(S[end])]:   # this is a part of T
                counts[ord(S[end])] -= 1
                if counts[ord(S[end])]>=0: appeared += 1
                if appeared==len(T):    # get a valid interval 
                    # shift start to shrink the interval
                    while not requires[ord(S[start])] or counts[ord(S[start])]<0:
                        counts[ord(S[start])] += 1
                        start += 1
                    if end-start+1<min_len:
                        min_len, min_start = end-start+1, start
        if min_len==len(S)+1: return ""
        return S[min_start:min_start+min_len]
        
                    

if __name__ == '__main__':
    s = Solution()
    print s.minWindow1("ADOBECODEBANC", "ABC")
