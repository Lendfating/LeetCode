#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        nums1, nums2 = [int(num1[-9:])], [int(num2[-9:])];
        for i in range(1, (len(num1)+8)/9):
            nums1.append(int(num1[-(i+1)*9:-i*9]))
        for i in range(1, (len(num2)+8)/9):
            nums2.append(int(num2[-(i+1)*9:-i*9]))
        # multiply respectively
        sums = [0] * (len(nums1)+len(nums2)-1); # long
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                sums[i+j] += nums1[j]*nums2[i]
        result, carry = "", 0
        for i in range(len(sums)):
            sums[i] = sums[i]+carry;
            result = ('%09d' % (sums[i]%1000000000)) + result;
            carry = sums[i]/1000000000;
        if carry>0:
            result = str(carry)+result;
            return result;
        else:
            for i in range(len(result)):
                if result[i]!='0':
                    return result[i:]
            return '0';

if __name__ == '__main__':
    s = Solution()
    print s.multiply('123456789254', '14233554462542')
