#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a boolean
    def isValid(self, s):
        if len(s)%2==1: return False
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if len(stack)==0: return False
                top = stack.pop()
                if not ((top=='(' and ch==')') or (top=='[' and ch==']') or (top=='{' and ch=='}')):
                    return False
        return len(stack)==0

if __name__ == '__main__':
    pass
