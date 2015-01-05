#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dic, result = {}, []
        for s in strs:
            key = "".join((lambda x:(x.sort(),x)[1])(list(s)))
            if dic.has_key(key):
                if dic[key] is not None:
                    result.append(dic[key])
                    dic[key] = None
                result.append(s)
            else:
                dic[key] = s
        return result
        
    

if __name__ == '__main__':
    pass
