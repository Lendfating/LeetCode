#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
原问题很明显抽象为计算 Fibonacci 数列，有三种方案：
方案一：动态规划，利用F(n-2)+F(n-1)计算更新 F(n)

方案二：利用矩阵加速计算过程，参看：http://www.cnblogs.com/xudong-bupt/archive/2013/03/19/2966954.html
    | F(n)  | = | 1  1| * | F(n-1) |
    | F(n-1)|   | 1  0|   | F(n-2) |
    因此，进一步罗列展开，我们可以得到如下公式：
    | F(n)  | = | 1  1| * | F(n-1) | = | 1  1| * | 1  1| * | F(n-2) | = | 1  1|^(n-1) * | F(1) |
    | F(n-1)|   | 1  0|   | F(n-2) |   | 1  0|   | 1  0|   | F(n-3) |   | 1  0|         | F(0) |
    由于矩阵满足结合律，易知上式成立。所以，我们只需要计算矩阵 | 1 1 | 的（n-1）次幂即可。求矩阵的pow与求整数的pow运算类似，我们可以采用2倍扩张的思想。
                                         | 1 0 |

方案三：利用 Fibonacci 数列的通项公式计算。利用待定系数构造等比数列（高中知识）的方法，可求得其通项公式如下：
    F(n) = 1/sqrt(5)*[ ((1+sqrt(5))/2)^n -(1-sqrt(5))^n ]
    时间复杂度理论上为线性，但是因为有 pow 的计算，所以其实效果跟方案二类似。

"""
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        # calculate the Fibonacci of n
        prev, cur = 1, 1    # start from 0, so we can handle the case when n==1
        for i in xrange(n-1):
            prev, cur = cur, prev+cur
        return cur
    
    # @param n, an integer
    # @return an integer
    def climbStairs1(self, n):
        # calculate the Fibonacci of n using matrix
        F = [[1],[1]]   # start matrix, with F(1) and F(0)
        transfer = [[1,1],[1,0]]    # transfer matrix
        result = self.multiply(self.pow(transfer, n-1), F)
        return result[0][0]
    
    def pow(self, matrix, n):
        # calculate the product of n matrixes
        result = [[0]*len(row) for row in matrix]   # it must be square matrix
        for i in xrange(len(matrix)): result[i][i] = 1   # unit matrix
        bit = 1
        while bit<=n:
            if n&bit>0:    # have this bit in result
                result = self.multiply(result, matrix)
            matrix = self.multiply(matrix, matrix)
            bit <<= 1
        return result
    
    def multiply(self, matrix1, matrix2):
        # calculate the product of two matrix
        # no out range verify here.
        m, K, n = len(matrix1), len(matrix2), len(matrix2[0])
        product = []
        for i in xrange(m):
            product.append([])
            for j in xrange(n):
                product[i].append(sum([matrix1[i][k]*matrix2[k][j] for k in xrange(K)]))
        return product
    
    # @param n, an integer
    # @return an integer
    def climbStairs1(self, n):
        # calculate the Fibonacci of n using formula
        # F(n) = 1/sqrt(5)*[ ((1+sqrt(5))/2)^n -(1-sqrt(5))^n ]
        import math
        sqrt_5 = math.sqrt(5)
        return 1/sqrt_5*(math.pow((1+sqrt_5)/2, n)-math.pow((1-sqrt_5)/2, n))

if __name__ == '__main__':
    s = Solution()
    print s.climbStairs1(4)
