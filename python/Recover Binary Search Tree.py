#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

注意这个题直接交换 mistake 节点的val，这样才能达到 oj 的时间要求。
但是真实情况下，我觉得更应该交换两个节点，交换两个节点的实现在方法 def recoverTree1(self, root):中

"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        # in-order traverse, and find the inverted sequence
        first, second = None, None
        cur, prev = root, TreeNode(-(1<<32))
        # use moke method to in-order traverse
        while cur is not None:
            if cur.left is None:
                if cur.val<prev.val:
                    if first is None: first = prev
                    second = cur
                prev = cur
                cur = cur.right
            else:
                prior = cur.left
                while prior.right is not None and prior.right!=cur:
                    prior = prior.right
                if prior.right is None:
                    # first time to visit cur, store cur in cur's prior's right
                    prior.right = cur
                    cur = cur.left
                else:
                    # back from the left sub-tree
                    prior.right = None  # recover its prior's information
                    # visit cur
                    if cur.val<prev.val:
                        if first is None: first = prev
                        second = cur
                    # visit cur's right sub-tree
                    prev = cur
                    cur = cur.right
        if first is not None:
            first.val, second.val = second.val, first.val
        return root
    
    # @param root, a tree node
    # @return a tree node
    def recoverTree1(self, root):
        # in-order traverse, and find the inverted sequence
        unusuals = []   # should be 2 or 4 elements
        cur, prev = root, TreeNode(-(1<<32))
        # use morris method to in-order traverse with constant space
        while cur is not None:
            if cur.left is None:
                if cur.val<prev.val:
                    unusuals.append(prev)
                    unusuals.append(cur)
                prev = cur
                cur = cur.right
            else:
                prior = cur.left
                while prior.right is not None and prior.right!=cur:
                    prior = prior.right
                if prior.right is None:
                    # first time to visit cur, store cur in cur's prior's right
                    prior.right = cur
                    cur = cur.left
                else:
                    # back from the left sub-tree
                    prior.right = None  # recover its prior's information
                    # visit cur
                    if cur.val<prev.val:
                        unusuals.append(prev)
                        unusuals.append(cur)
                    # visit cur's right sub-tree
                    prev = cur
                    cur = cur.right
        if len(unusuals)==0: return root
        dummy = TreeNode(0)
        dummy.left = root
        parent1 = self.getParent(dummy, unusuals[0])
        parent2 = self.getParent(dummy, unusuals[-1])
        self.swapNode(unusuals[0], unusuals[-1], parent1, parent2)
        return dummy.left
        
    def getParent(self, root, target):
        cur, result = root, None
        while cur is not None:
            if cur.left is None:
                if cur.left==target or cur.right==target: result = cur
                cur = cur.right
            else:
                prior = cur.left
                while prior.right is not None and prior.right!=cur:
                    prior = prior.right
                if prior.right is None:
                    prior.right = cur
                    if cur.left==target or cur.right==target: result = cur
                    cur = cur.left
                else:
                    prior.right = None
                    cur = cur.right
        return result
            
    def swapNode(self, node1, node2, parent1, parent2):
        if parent1.left==node1:
            parent1.left = node2
        else:
            parent1.right = node2
        if parent2.left==node2:
            parent2.left = node1
        else:
            parent2.right = node2
        node1.left, node1.right, node2.left, node2.right = node2.left, node2.right, node1.left, node1.right
        

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)
    s.recoverTree(root)
