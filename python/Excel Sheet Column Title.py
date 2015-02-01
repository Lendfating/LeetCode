#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

小问题大陷阱啊，好好想想，千万不要太大意。
不同于一般的26进制数，普通的26进制数是从0开始的，而这个是从1开始的。且每一位都是用 A表示1，没有表示0

A.... Z AA.....AZ
1....26 27.....52 ——> 对应的十进制数
0....25 26.....51 ——> 对应的编号

也不完全是27进制，因为没有 A0.
观察上述数，与普通的26进制的区别：A表示0，但是0可以继续做高位出现，即允许存在以0开始的数，且该数不同于省略掉0后的值。
一位数共有 26个，两位数共有 26*26个， n位数共有26^n个
而普通的26进制数位：一位及以下的数共有 26个，两位及以下的数共有 26*26个，n位及以下的数共有 26^n个。

Let's see the relationship between the Excel sheet column title and the number:

A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

But how to get the column title from the number? We can't simply use the n%26 method because:

ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

We can use (n-1)%26 instead, then we get a number range from 0 to 25.

"""
class Solution:
    # @return a string
    def convertToTitle(self, num):
        # this is not 27 base number, and not common 26 base number,
        # because there is no A0 in the number list
        result = ""
        while num>0:
            result = chr(65+(num-1)%26)+result
            num = (num-1)/26
        return result

if __name__ == '__main__':
    pass
