#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S = sorted(S)
        result, last = [], [[]]
        for L in xrange(1, len(S)+1):
            result.extend(last)
            cur = []
            for i in xrange(L-1, len(S)):
                for item in last:
                    if len(item)>0 and item[-1]>=S[i]: break
                    cur.append(item[:])
                    cur[-1].append(S[i])
            last = cur
        result.extend(last)
        return result
    
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets1(self, S):
        # We should find that, for one element in S, it only has two case, 
        # in the result subset or not in the result subset. And we will find
        # the number of this two kinds of subsets is same.
        S = sorted(S)
        return self.__subsets(S)
    
    def __subsets(self, S):
        # We should find that, for one element in S, it only has two case, 
        # in the result subset or not in the result subset. And we will find
        # the number of this two kinds of subsets is same.
        if len(S)==0: return [[]]
        result = self.__subsets(S[1:])
        for i in range(len(result)):    # don't use xrange()
            result.append([S[0]]+result[i])
        return result
    
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets2(self, S):
        # implement last idea in a more straight way
        S = sorted(S)
        result = [[]]
        for ch in S:
            result += [subset+[ch] for subset in result]
        return result
    
        
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets3(self, S):
        # from front idea, we will find it is very like a number.
        # init result as [[]]*(1<<len(S)), and append(S[i]) into result[num] will
        # be time limit out, maybe because result[index] cost too much time.
        S = sorted(S)
        result, len_S = [], len(S)
        for num in xrange(1<<len_S):
            temp = []
            for i in xrange(len_S):
                if ((num>>i)&1)>0:
                    temp.append(S[i])
            result.append(temp)
        return result
        
    

if __name__ == '__main__':
    s = Solution()
    print s.subsets3([])
    print s.subsets3([1])
    print s.subsets3([1,4])
