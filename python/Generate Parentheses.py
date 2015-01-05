#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
方案一：
    充分利用括号间排列关系，嵌套和毗邻，因此，每个串都是由若干个子串通过嵌套和毗邻组成的：(inner)sibling
    因此，通过动态规划，累积记录n=0：n-1时的值，然后对于n=n时，只需要搭配 inner 和 sibling的值即可去边所有情况。
    
方案二：n个（与）的排列组合。
    1. 递归法：从前往后，依次排列所有的 (与)的排列方案，利用剪枝法去除掉无效子串 （ 当前“)”比“(”多 ）
    2. 插入法：在所有"((...("的基础上插入‘）’，要保证所有插入状态下该串仍有效 （不会出现“)”比"("多的子串 ）

"""
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        lists = [[""]]
        for i in xrange(1, n+1):
            parenthesis = [];
            for j in xrange(i):
                for inner in lists[j]:
                    for sibling in lists[i-j-1]:
                        parenthesis.append("("+inner+")"+sibling);
            lists.append(parenthesis);
        return lists[n]
 
    # @param an integer
    # @return a list of string
    def generateParenthesis1(self, n):
        return self.addingPar("", n, n);
        
    # @param prefix, the valid combination with current '(' and ')'
    # @param l_n, r_n, the remaind number of '(' and ')'
    # @return a list of valid complated combinations
    def addingPar(self, prefix, l_n, r_n):
        result = [prefix] if l_n==0 and r_n==0 else [];
        if l_n>0:
            result.extend(self.addingPar(prefix+"(", L_n-1, r_n));
        if r_n>l_n:
            result.extend(self.addingPar(prefix+")", l_n, r_n-1));
        return result;     
      
    # @param an integer
    # @return a list of string
    def generateParenthesis2(self, n):
        return self.permutate("("*n, n);
        
    # @param lefts, string of '('
    # @param n, the counts of ')' to be inserted into lefts
    # @return all the cases insert n '('s into lefts.
    def permutate(self, lefts, n):
        if n>len(lefts):    # invaild
            return [];
        elif n<=0:
            return [lefts]
        else:
            result, rights = [], "";
            for i in range(n+1):    # how many ')' should we leave for the end of lefts
                subPermutations = self.permutate(lefts[:-1], n-i);
                for sp in subPermutations:
                    result.append(sp+"("+rights)
                rights += ")"
            return result;
 

if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(2);
    print s.generateParenthesis(3);
    print s.generateParenthesis(4);
    print s.generateParenthesis1(4);
    print s.generateParenthesis2(4);
