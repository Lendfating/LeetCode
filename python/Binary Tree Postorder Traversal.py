#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 18, 2014

@author: Zhen
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def initTree(arr):
    if len(arr)==0 or arr[0]=='#':
        return arr[1:], None;
    else:
        root = TreeNode(arr[0]);
        arr, root.left = initTree(arr[1:]);
        arr, root.right = initTree(arr);
        return arr, root;
        
class Item:
    def __init__(self, p):
        self.point = p; # 指针
        self.tag = 1;   # 表示这是第几次被压进栈
        
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return [];
        else:
            ret = [];
            ret.extend(self.postorderTraversal(root.left));
            ret.extend(self.postorderTraversal(root.right));
            ret.append(root.val);
            return ret;
        
    def postorderTraversal1(self, root):
        # 利用栈的非递归实现方式
        if root is None:
            return [];
        else:
            ret, stack = [], [];
            stack.append(Item(root));
            p = root.left;
            while len(stack)>0:
                while p is not None:
                    stack.append(Item(p));
                    p = p.left;
                item = stack.pop();
                if item.tag == 1:   # 第一次出栈，准备再次入栈，并处理其有子节点
                    p = item.point.right;
                    item.tag = 2;
                    stack.append(item);
                else:               # 第二次出栈，直接输出
                    ret.append(item.point.val);
            return ret;
    

if __name__ == '__main__':
    arr = [1,'#',2,3];
    arr, root = initTree(arr);
    s = Solution();
    print s.postorderTraversal(root)
    print s.postorderTraversal1(root)
    