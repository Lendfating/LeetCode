#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        # error for denominator==0
        if denominator==0: return 0
        # Step 1. Judge the sign of the result
        sign = "" if numerator*denominator>=0 else "-"
        numerator, denominator = abs(numerator), abs(denominator)
        # Step 2. Calculate the integral part of the result
        decimal = sign + str(numerator/denominator)
        numerator = numerator % denominator
        # Step 3. Calculate the decimal part of the result if any exist.
        if numerator>0:
            # Step 3.1 initialize the variables to store the informations in decimal part
            decimal_part, remainders, index = [], {}, 0
            # Step 3.2 loop to handle each bit in the decimal part
            while numerator>0:
                # if this numerator has ever been seen, we find the repeating part
                if remainders.has_key(numerator):
                    decimal_part.insert(remainders[numerator], "(")
                    decimal_part.append(")")
                    break
                # calculate the quotient bit and remainder of each bit
                remainders[numerator] = index
                numerator = numerator*10
                decimal_part.append(str(numerator/denominator))
                numerator = numerator % denominator
                index += 1
            # Step 3.3 join the bits, and append to the result
            decimal += "." + "".join(decimal_part)
        return decimal

if __name__ == '__main__':
    pass
