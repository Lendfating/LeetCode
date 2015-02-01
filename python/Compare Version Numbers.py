#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        vs1, vs2 = version1.split("."), version2.split(".")
        len1, len2 = len(vs1), len(vs2)
        vs1.extend([0]*(len2-len1))
        vs2.extend([0]*(len1-len2))
        for i in xrange(len(vs1)):
            v1, v2 = int(vs1[i]), int(vs2[i])
            if v1>v2:
                return 1
            elif v2>v1:
                return -1
        return 0
    
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion1(self, version1, version2):
        vs1, vs2 = version1.split("."), version2.split(".")
        len1, len2 = len(vs1), len(vs2)
        for i in xrange(max(len1, len2)):
            v1 = int(vs1[i]) if i<len1 else 0
            v2 = int(vs2[i]) if i<len2 else 0
            if v1>v2: return 1
            if v2>v1: return -1
        return 0
    
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion2(self, version1, version2):
        i, j, s1, s2 = 0, 0, "0","0"
        while i<len(version1) or j<len(version2):
            while i<len(version1) and version1[i]!='.': s1, i = s1+version1[i], i+1
            while j<len(version2) and version2[j]!='.': s2, j = s2+version2[j], j+1
            if int(s1)>int(s2): return 1
            if int(s1)<int(s2): return -1
            s1, s2, i, j = "0", "0", i+1, j+1
        return 0
            

if __name__ == '__main__':
    pass
