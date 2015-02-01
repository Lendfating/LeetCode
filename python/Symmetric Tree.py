#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

第二种方法用一个栈也ok，只是简单的将两个栈融合在一起用了。

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None: return True
        return self.__isSymmetric(root.left, root.right)
    
    def __isSymmetric(self, left, right):
        # both left and right go to the end
        if left is None and right is None: return True
        # one side goto the end or the value don't equals.
        if left is None or right is None or left.val!=right.val: return False
        # recursive to check the son of left and right.
        return self.__isSymmetric(left.left, right.right) and \
                self.__isSymmetric(left.right, right.left)
                
    # @param root, a tree node
    # @return a boolean
    def isSymmetric1(self, root):
        # convert previous recursive solution into iterative one.
        if root is None: return True
        left, right = root.left, root.right
        stack1, stack2 = [left], [right]
        while len(stack1)>0 and len(stack2)>0:
            left, right = stack1.pop(), stack2.pop()
            # both left sub-tree and right sub-tree goto the end.
            if left is None and right is None: continue
            # one side goto the end or the value don'y equals.
            if left is None or right is None or left.val!=right.val: return False
            # travel left tree by pre-order(parent->left->right)
            stack1.append(left.right)
            stack1.append(left.left)
            # travel right tree by order(parent->right->left)
            stack2.append(right.left)
            stack2.append(right.right)
        return True

if __name__ == '__main__':
    pass
