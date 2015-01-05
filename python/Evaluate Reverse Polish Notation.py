#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''

"""
# problem
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Link: https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/

# soluction
利用栈即可解决

"""
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = [];
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                operand2 = stack.pop();
                operand1 = stack.pop();
                if token=='+':
                    stack.append(operand1+operand2);
                elif token=='-':
                    stack.append(operand1-operand2);
                elif token=='*':
                    stack.append(operand1*operand2);
                elif token=='/':
                    stack.append(int(1.0*operand1/operand2));
            else:
                stack.append(int(token));
        return stack.pop();
                

if __name__ == '__main__':
    s = Solution();
    print s.evalRPN(["2", "1", "+", "3", "*"])
    print s.evalRPN(["4", "13", "5", "/", "+"])
    print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
