#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

同样的思想，第二个实现的明显更酷

"""
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        p = [ str(i) for i in range(n+1)]  # 0 at the front just is a placeholder
        counts = [1]*n
        for i in range(n-1)[::-1]:
            counts[i] = (n-i)*counts[i+1]
        k -= 1
        for i in xrange(n):
            if k>=counts[i]:
                j = k/counts[i]
                tmp = p[i+j]
                while j>0: p[i+j], j = p[i+j-1], j-1
                p[i] = tmp
                k = k%counts[i]
        return "".join(p[1:])
    
    # @return a string
    def getPermutation1(self, n, k):
        # same idea with previous code, but implement more succinctly 
        array = range(1, n + 1)
        k = (k % math.factorial(n)) - 1
        permutation = []
        for i in xrange(n - 1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            permutation.append(array.pop(idx))  # cool
    
        return "".join(map(str, permutation))

if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(3, 4)
