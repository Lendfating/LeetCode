#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

按如下格式，写一下Pascal树：
1
1,1
1,2,1
1,3,3,1
1,4,6,4,1
可知，从右往左计算更靠谱

利用公式，第k行的结果为 [C(k,0), C(k,1), C(k,2), ... ,C(k,k)]
而 C(k, m+1)=C(k,m)*(k-m+1)/m

"""
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        last_row, cur_row = [1], []
        for i in xrange(rowIndex):
            cur_row = [1]
            for j in xrange(i):
                cur_row.append(last_row[j]+last_row[j+1])
            cur_row.append(1)
            last_row = cur_row
        return last_row
    
    # @return a list of integers
    def getRow1(self, rowIndex):
        row = [0]*(rowIndex+1)
        row[0] = 1
        for i in xrange(rowIndex+1):
            for j in range(i)[::-1]:
                row[j+1] += row[j]
        return row
    
    # @return a list of integers
    def getRow2(self, rowIndex):
        row = [1]
        for i in xrange(1, rowIndex/2+1):
            row.append(row[-1]*(rowIndex-i+1)/i);
        if rowIndex&1>0:
            row.extend(row[::-1])
        else:
            row.extend(row[-2::-1])
        return row

if __name__ == '__main__':
    pass
