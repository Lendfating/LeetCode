#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a string
    def intToRoman(self, num):
        return self.digit2Roman(num/1000, "M", "?", "?")\
                + self.digit2Roman(num%1000/100, "C", "D", "M")\
                + self.digit2Roman(num%100/10, "X", "L", "C")\
                + self.digit2Roman(num%10, "I", "V", "X")
        
            
    def digit2Roman(self, digit, one, five, ten):
        if digit%5==4:
            return one + (five if digit==4 else ten)
        else:
            return (five if digit>=5 else "")+"".join([one for i in range(digit%5)])
        

if __name__ == '__main__':
    pass
