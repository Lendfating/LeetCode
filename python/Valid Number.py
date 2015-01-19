#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

这个题没有考察 十六进制、八进制和二进制问题。只是简单的考察了整数和浮点数的表示。
数据格式说明如下：
整数：
    十六进制： 0X 开始，后跟0~F字符        ==> X后可跟若干个0
    八进制：     0  开始，后跟0-7字符        ==> 前可跟若干个0
    十进制：    0~9字符的组合，不可以0开始（0除外，0可为若干的0连接）
    二进制：    b结尾，前面为0~1的组合        ==> 前面也可有若干个0
    
小数：
    A  。  B  e  C
    分为如上三部分，其中A、B、C三部分必须都是十进制数
    A、B不可同时省略
    (.B)可一起省略，但是此时A不可在省略
    C不可省略
    e C 可同时省略
    
isNumber是包含上面所有规则的实现，但是不能AC，因为有八进制与oj中的测试结果不一致。

对本题，只实现十进制整数与小数。
    整数：0~9组成，长度不能为0
    小数：A、B不可同时省略；（。B）可一起省略，但此时A不可在省略；e C可同时省略，但是C不可单独省略
实现思路主要有三：普通查找、正则表达式、确定有限状态机（DFA）
    普通查找：https://oj.leetcode.com/discuss/9013/a-simple-solution-in-cpp
    正则表达式：https://oj.leetcode.com/discuss/9772/java-regex-solution-comments-inline
    ("(\\s*)[+-]?((\\.[0-9]+)|([0-9]+(\\.[0-9]*)?))(e[+-]?[0-9]+)?(\\s*)");
    确定优先状态机（DFA）：https://oj.leetcode.com/discuss/13691/c-my-thought-with-dfa
    && pdf
    

"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()   # " 1 ", we think it is valid
        if len(s)>0 and (s[0]=='-' or s[0]=='+'): s = s[1:]    # negative OR positive
        if len(s)==0: return False
        if len(s)>1:
            if s[:2]=="0x" or s[:2]=="0X":  # hexadecimal integer
                f = lambda x: (x>=ord('0') and x<=ord('9')) or (x>=ord('A') and x<=ord('F')) or (x>=ord('a') and x<=ord('f'))
                return self.isDigit(s[2:], f)
            elif s[-1]=='b' or s[-1]=="B":  # binary integer
                f = lambda x: x>=ord('0') and x<=ord('1')
                return self.isDigit(s[:-1], f)
        for i in xrange(len(s)):
            if ord(s[i])<ord('0') or ord(s[i])>ord('9'):
                break
        else:
            if s[0]=="0":       # Octal integer
                f = lambda x: x>=ord('0') and x<=ord('7')
                return self.isDigit(s[1:], f)
            else:
                return True     # decimal integer
        if i==0 and s[i]!='.': return False     # must start with digit or '.'
        if s[i]=='.':   # float
            if len(s)==1: return False    # ".1" and "1." is valid, but "." is invalid
            for j in xrange(i+1, len(s)):
                if ord(s[j])<ord('0') or ord(s[j])>ord('9'):
                    break
            else:       # only float
                return True
            if j==1: return False     # ".e1" is also invalid
            i = j
        if s[i]=='e' or s[i]=='E':  # advance float with 10^x
            if i+1<len(s) and (s[i+1]=="-" or s[i+1]=="+"): i += 1   # for case 1e-1
            f = lambda x: x>=ord('0') and x<=ord('9')
            return self.isDigit(s[i+1:], f)
        return False
    
    def isDigit(self, s, f):
        if len(s)==0: return False
        # "000" is also valid
        for i in xrange(len(s)):
            if not f(ord(s[i])): return False
        return True
        
    # @param s, a string
    # @return a boolean
    def isNumber1(self, s):
        # scan from start to end to verify each char
        i, len_s = 0, len(s)
        
        # skip the whitespace at start
        while i<len_s and s[i]==' ': i += 1
        
        # skip sign bit if exist
        if i<len_s and (s[i]=='+' or s[i]=='-'): i += 1
        
        # scan to handle the decimal part 
        n_dots, n_num = 0, 0
        while i<len_s:
            if s[i]=='.':
                n_dots += 1
            elif ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
                n_num += 1
            else:
                break
            i += 1
        if n_dots>1 or n_num==0: return False   # good idea for handle ".", "1.", ".1", "1.1"
        
        # scan to handle exponent part
        if i<len_s and (s[i]=='e' or s[i]=='E'):
            i, n_num = i+1, 0
            if i<len_s and (s[i]=='+' or s[i]=='-'): i += 1
            while i<len_s and ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
                n_num, i = n_num+1, i+1
            if n_num==0: return False
            
        # skip the whitespace at end
        while i<len_s and s[i]==' ': i += 1
        return i==len_s     # must reach the end of the str
    
    
    # @param s, a string
    # @return a boolean
    def isNumber2(self, s):
        # use regex 
        # not test on oj
        import re
        p = re.compile("^(\s*)([+-]?(\d+(.\d*)?)|(.\d+))([eE][+-]?\d+)?(\s*)$")
        return True if p.match(s) else Fals
    
    # @param s, a string
    # @return a boolean
    def isNumber3(self, s):
        # use DFA(deterministic finite automaton)
        transfer = [#space sign digit dot e|E other
                    [   0,   1,   2,   3,  -1,  -1],  # S0: start state
                    [  -1,  -1,   2,   3,  -1,  -1],  # S1: one sign
                    [   8,  -1,   2,   4,   5,  -1],  # S2: integer
                    [  -1,  -1,   4,  -1,  -1,  -1],  # S3: one dot
                    [   8,  -1,   4,  -1,   5,  -1],  # S4: float
                    [  -1,   6,   7,  -1,  -1,  -1],  # S5: start of exponent
                    [  -1,  -1,   7,  -1,  -1,  -1],  # S6: sign
                    [   8,  -1,   7,  -1,  -1,  -1],  # S7: exponent
                    [   8,  -1,  -1,  -1,  -1,  -1]   # S8: end state
                    ]
        state = 0
        for ch in s:
            if ch == " ":
                input = 0   # space
            elif ch == "+" or ch =="-":
                input = 1   # sign
            elif ord(ch)>=ord('0') and ord(ch)<=ord('9'):
                input = 2   # digit
            elif ch == ".":
                input = 3   # dot
            elif ch == "e" or ch == "E":
                input = 4   # e|E
            else:
                input = 5   # others
            # update state info by transfer table
            state = transfer[state][input]
            # exit when state is -1
            if state==-1: return False
        # check whether the state is stable
        return state==2 or state==4 or state==7 or state==8
    
if __name__ == '__main__':
    pass
