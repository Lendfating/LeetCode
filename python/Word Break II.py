#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

网上都说从前往后不行（因为aaaaaaaaaaaab的存在），但是我发现貌似从前往后、从后往前都可以。我的出问题是出在 [[]]*n,没有真正复制，应该写 [[] for i in xrange(n)]

最后一种更简单。直接递归实现了。其实dp真的没省多少事。因路径信息没有存档，所以需要单独生成路径信息，在路径的排列组合生成的过程中，时间复杂度会成指数上升。

比较而言，可能第二种方案会更快一点，因为我对截止到某个位置的前缀的结果进行了记录，这样可能会有一定的剪枝（避免重复计算）的效果。

"""
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        if s=="" or len(dict)==0: return []
        dic = {}
        for key in dict:
            dic[key] = True
        return self.__wordBreak(s, dic)
    
    def __wordBreak(self, s, dict):
        tos, to_check, checked, length = [[] for i in xrange(len(s)+1)], [len(s)], [False]*(len(s)+1), len(s)
        while len(to_check)>0:
            end = to_check.pop()
            if not checked[end]:
                checked[end] = True
                for start in xrange(end):
                    if dict.has_key(s[start:end]):
                        to_check.append(start)
                        tos[start].append(end)
        return self.__getSentence(s, "", tos, 0)
    
    def __getSentence(self, s, path, tos, start):
        if start==len(s): return [path]
        result = []
        if start>0: path += " "
        for end in tos[start]:
            result.extend(self.__getSentence(s, path+s[start:end], tos, end))
        return result
        
    def __wordBreak1(self, s, dict):
        froms, to_check, checked, length = [[] for i in xrange(len(s)+1)], [0], [False]*(len(s)+1), len(s)
        while len(to_check)>0:
            start = to_check.pop()
            if not checked[start]:
                checked[start] = True
                for end in xrange(start+1, length+1):
                    if dict.has_key(s[start:end]):
                        to_check.append(end)
                        froms[end].append(start)
        return self.__getSentence(s, {}, froms, len(s))
        
    def __getSentence(self, s, tables, froms, end):
        if tables.has_key(end): return tables[end]
        result = []
        for start in froms[end]:
            if start==0:
                result.append(s[start:end])
            else:
                prefixs = self.__getSentence(s, tables, froms, start)
                for prefix in prefixs:
                    result.append(prefix+" "+s[start:end])
        tables[end] = result
        return result
    
    
    def __wordBreak2(self, s, dict):
        return self.__genPath(s, dict, "", len(s))
    
    def __genPath(self, s, dict, path, end):
        if end==0: return [path[:-1]]
        result = []
        for start in xrange(end):
            if dict.has_key(s[start:end]):
                result.extend(self.__genPath(s, dict, s[start:end]+" "+path, start))
        return result

if __name__ == '__main__':
    s = Solution()
    print s.wordBreak("ab", ['a','b'])
