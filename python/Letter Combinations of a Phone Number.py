#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        letters = [''];
        for digit in digits:
            letters = self.cross(letters, self.mapDigit2Char(digit));
        return letters;
    
    def mapDigit2Char(self, digit):
        if digit=='0':
            return ' ';
        elif digit=='1':
            return '_';
        elif digit=='2':
            return 'abc';
        elif digit=='3':
            return 'def';
        elif digit=='4':
            return 'ghi';
        elif digit=='5':
            return 'jkl';
        elif digit=='6':
            return 'mno';
        elif digit=='7':
            return 'pqrs';
        elif digit=='8':
            return 'tuv';
        elif digit=='9':
            return 'wxyz';
    
    def cross(self, A, B):
        result = [];
        for prefix in A:
            for postfix in B:
                result.append(prefix+postfix);
        return result;
    
    # @return a list of strings, [s1, s2]
    def letterCombinations1(self, digits):
        keyboards = [' ','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        result, k = [[''], []], 0;
        for digit in digits:
            result[k^1] = [];
            for prefix in result[k]:
                for postfix in keyboards[int(digit)]:
                    result[k^1].append(prefix+postfix);
            k ^= 1;
        return result[k];

if __name__ == '__main__':
    s = Solution();
    print s.letterCombinations('')
    print s.letterCombinations1('32')
