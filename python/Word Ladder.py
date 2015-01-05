#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if len(dict)>26:    # 主要考虑到 self.transferable 的计算比hash慢，故不再 *len(start)
            return self.ladderLength2(start, end, dict)
        else:
            return self.ladderLength1(start, end, dict)
        
    def ladderLength1(self, start, end, dict):
        rest, letters, j = [dict, []], [[start],[]], 0
        for i in range(len(dict)+1):
            letters[(i+1)%2] = []
            for letter in letters[i%2]:
                if self.transferable(letter, end):
                    return i+2
                for d in rest[j%2]:
                    if self.transferable(letter, d):
                        letters[(i+1)%2].append(d)
                    else:
                        rest[(j+1)%2].append(d)
                rest[j%2], j = [], j+1
            if len(letters[(i+1)%2])==0: return 0
        return 0
    
    # @return an integer
    def ladderLength2(self, start, end, dict):
        dic, queue = {}, [start]
        for letter in dict:
            dic[letter] = 0;
        dic[start] = 1
        while len(queue)>0:
            letter = queue.pop(0);
            if self.transferable(letter, end):
                return dic[letter]+1
            for j in range(len(letter)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    temp = letter[:j]+ch+letter[j+1:]
                    if dic.has_key(temp) and dic[temp]==0:
                        queue.append(temp)
                        dic[temp] = dic[letter]+1
        return 0
            
    def transferable(self, origin, target): 
        return 1 == sum([origin[i]!=target[i] for i in range(len(origin))])
        

if __name__ == '__main__':
    s = Solution()
    print s.ladderLength('a', 'c', ['a','b','c'])
    print s.ladderLength("hot", "dog", ["hot","dog","dot"])
    print s.ladderLength2("hit", "cog", ["hot","dot","dog","lot","log"])
