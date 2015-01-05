#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
通过位操作，模拟除法过程。
或 做差统计法，但是普通的做差可以优化（2倍递增）
"""
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor==0:
            return None;
        quotient, remainder = self.divideWithRemainder(abs(dividend), abs(divisor))
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            return quotient;
        else:
            return -quotient;
        
        return quotient
            
    def divideWithRemainder(self, dividend, divisor):
        if dividend<divisor:
            return 0, dividend;
        else:
            high_bit, remainder = self.divideWithRemainder(dividend >> 1, divisor);
            dividend = remainder<<1 | dividend&1;
            if dividend>=divisor:
                low_bit, remainder = 1, dividend-divisor;
            else:
                low_bit, remainder = 0, dividend;
            return (high_bit<<1) + low_bit, remainder;
        
    # @return an integer
    def divide1(self, dividend, divisor):
        quotient, sign = 0, True if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else False;
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend>=divisor:
            i = 0;
            while dividend >= divisor<<(i+1):
                i += 1;
            quotient += 1<<i;
            dividend -= divisor<<i;
        return quotient if sign else -quotient; 
            

if __name__ == '__main__':
    s = Solution()
    print s.divide(17, 6)
    print s.divide(500, 9)
    print s.divide1(500, 9)
