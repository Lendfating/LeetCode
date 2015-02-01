#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

尽量不要用python 的数组[i:j],这样是数组的重新拷贝，会导致 memory limit error。

第二种方法时间复杂度会达到 O（n）， 按前序遍历的结果（preorder）构造树，按中序遍历（inorder）的
顺序确定节点之间的父子关系。

分析前序遍历的结果，易知后续构造的节点只能是先前构造的节点的子节点，或者在该路径的右侧节点。（从祖先到当前节点的路径）
而通过利用中序遍历，我们可以区分出哪些是子节点，哪些是右侧节点。
整个数的构建过程类似于先序遍历，先沿左子树一路访问，然后是父结点的右子树，继续左子树访问到底。

"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.__buildTree(preorder, inorder, 0, 0, len(preorder))
    
    def __buildTree(self, preorder, inorder, i, j, length):
        if length==0: return None
        node = TreeNode(preorder[i])
        for k in xrange(length):
            if inorder[j+k]==preorder[i]:
                break
        node.left = self.__buildTree(preorder, inorder, i+1, j, k)
        node.right= self.__buildTree(preorder, inorder, i+k+1, j+k+1, length-k-1)
        return node
    
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree1(self, preorder, inorder):
        i, j, length = 0, 0, len(preorder)
        stack = [TreeNode(1<<32)]
        parent = None
        while j<length:
            if inorder[j]==stack[-1].val:
                # no left sub-tree for node stack[-1]
                parent = stack.pop()
                j += 1
            elif parent is not None:
                # construct the right sub-tree of parent node
                node = TreeNode(preorder[i])
                parent.right = node
                stack.append(node)
                parent = None
                i += 1
            else:
                # construct the left sub-tree of stack[-1] at default case.
                node = TreeNode(preorder[i])
                stack[-1].left = node
                stack.append(node)
                i += 1
        return stack.pop().left
    

if __name__ == '__main__':
    s = Solution()
    root = s.buildTree([1,2,3], [2,1,3])
    print root
