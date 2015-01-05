#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
唉，O（2n）会有 Memory Limit Exceeded 异常。
"""
class MinStack:
    def __init__(self):
        self.stack = [];
        self.min = 0;
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.stack)==0:
            self.stack.append(0);
            self.min = x;
        else:
            self.stack.append(x-self.min);
            if x<self.min:  # 通过负数，记录了变更最小值的位置
                self.min = x;

    # @return nothing
    def pop(self):
        if len(self.stack)>0:
            pop = self.stack.pop();
            if pop<0:   # 负数表示最小值变更点，需要变更回去
                self.min = self.min-pop;

    # @return an integer
    def top(self):
        if len(self.stack)>0:
            top = self.stack[len(self.stack)-1];
            if top>=0:
                return top + self.min;
            else:
                return self.min;

    # @return an integer
    def getMin(self):
        return self.min;

class MinStack1:
    def __init__(self):
        self.stack = [];
        self.minStack = [];
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x);
        if len(self.minStack)==0 or x<=self.getMin():
            self.minStack.append(x);

    # @return nothing
    def pop(self):
        if len(self.stack)>0 and self.stack.pop()==self.getMin():
            self.minStack.pop();

    # @return an integer
    def top(self):
        if len(self.stack)>0:
            return self.stack[len(self.stack)-1];

    # @return an integer
    def getMin(self):
        if len(self.minStack)>0:
            return self.minStack[len(self.minStack)-1];
    
if __name__ == '__main__':
    s=MinStack();
    s.pop();
    s.push(5);
    s.push(2);
    s.push(7);
    print s.getMin();
    print s.top();
