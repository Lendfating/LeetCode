#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''

"""
括号匹配，子串间的关系无非两种，嵌套和毗邻。
从前往后依次处理每个字符，当前状态无非有三种，饥饿状态、饱和状态、撑死状态。
1. 饥饿状态，左侧还有未匹配的‘（’，所以可以接受右侧新输入的‘）’。这时有可能会出现嵌套现象
2. 饱和状态，左侧‘（’和‘）’匹配完。此时有可能出现毗邻现象
3. 撑死状态，最后多一个‘）’，导致前面的串跟后续串不可能发生任何关系，因此完全可以重新开始。
饥饿状态需要记录饥饿程度，从而方便据此进食‘）’。
"""
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        # 利用栈记录饥饿程度，利用下标求解子串长度。每个‘（’的下标表示其后面的串都有效
        ans, lefts= 0, [-1];  # lefts记录了当前未匹配‘（’的下标，栈底留一位记录当前串起始位置
        for i in range(len(s)):
            if s[i]=='(':   # 直接入栈
                lefts.append(i);
            elif len(lefts)==1: # 已到栈底，处于撑死状态，重新开始
                lefts[0] = i;
            else:               # ‘）’要看情况处理，此时为饥饿状态
                lefts.pop();    # 进食一口，长度增加
                ans = max(ans, i-lefts[len(lefts)-1]);
        return ans;
    
    def longestValidParentheses1(self, s):
        # 不借助栈，采用动态规划的方式去记录
        ans, gaps = 0, [0]*len(s);  # gaps包含了从当前位开始有效串的长度
        for i in range(len(s)-1)[::-1]:
            matchs = i+gaps[i+1]+1;
            # case 嵌套：‘((...))’
            if s[i]=='(' and matchs<len(s) and s[matchs]==')':
                gaps[i] = gaps[i+1]+2;
                # case 毗邻：“((...))(...)”
                if matchs+1<len(s) and gaps[matchs+1]>0:
                    gaps[i] += gaps[matchs+1];
                ans = max(ans, gaps[i]);
        return ans;
    
    def longestValidParentheses2(self, s):
        # 仅利用扫描解决。空间复杂度为O(1)
        # 充分对不能完全匹配的情况进行分析。或者左括号多，或者有括号多。
        ans, depth, start = 0, 0, -1;
        for i in range(len(s)): # 从左往右，处理所有左括号少的子串
            if s[i]=='(':
                depth += 1;
            else:
                depth -= 1;
                if depth<0:
                    depth, start = 0, i;
                elif depth==0:  # 不可以都放在上面，不然正常匹配的串无法处理
                    ans = max(ans, i-start);
        depth, start = 0, len(s);
        for i in range(len(s))[::-1]:# 从右往左，处理所有右括号少的子自串
            if s[i]==')':
                depth += 1;
            else:
                depth -= 1;
                if depth<0:
                    depth, start = 0, i;
                elif depth==0:
                    ans = max(ans, start-i);
        return ans;

if __name__ == '__main__':
    s = Solution();
    print s.longestValidParentheses("(()")
    print s.longestValidParentheses(")()())")
    print s.longestValidParentheses("()(())")
    print s.longestValidParentheses1("(()")
    print s.longestValidParentheses1(")()())")
    print s.longestValidParentheses1("()(())")
    print s.longestValidParentheses2("(()")
    print s.longestValidParentheses2(")()())")
    print s.longestValidParentheses2("()(())")
    
