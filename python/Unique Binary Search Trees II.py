#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

第一种方法 Memory Limit Exceeded。
实在想象不出为什么内存会超限，我没有做多余的工作呀……是不是Python指针复制时自动复制的对应的对象了？？！！

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        #！！！！　can't pass oj!!! Memory Limit Exceeded。
        # dp[i][l] 表示[i, i+l)部分形成的树信息
        dp = [[[]]*(n+1) for i in xrange(n+2)]
        for i in xrange(1, n+2): dp[i][0].append(None)
        for l in xrange(1, n+1):
            for i in xrange(1, n+2-l):
                for k in xrange(l):
                    for left in dp[i][k]:
                        for right in dp[i+k+1][l-k-1]:
                            node = TreeNode(i+k)
                            node.left = left
                            node.right = right
                            dp[i][l].append(node)
        return dp[1][n]
    
    # @return a list of tree node
    def generateTrees1(self, n):
        return self.__generateTrees(1, n+1)
    
    def __generateTrees(self, start, end):
        if start>=end: return [None]
        result = []
        for i in xrange(start, end):
            lefts = self.__generateTrees(start, i)
            rights = self.__generateTrees(i+1, end)
            for left in lefts:
                for right in rights:
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    result.append(node)
        return result
    

if __name__ == '__main__':
    pass
