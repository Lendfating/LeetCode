#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        dic, DEFAULT_DEPTH, queue, result = {}, len(dict)+3, [[start],[]], []
        for letter in dict:
            dic[letter] = {'depth':DEFAULT_DEPTH,'paths':[]} # not used yet
        dic[start] = {'depth':1,'paths':[[start]]}
        for i in xrange(len(dict)):
            while len(queue[i%2])>0:
                letter = queue[i%2].pop(0)
                if self.transferable(letter, end):
                    for path in dic[letter]['paths']:
                        path.append(end)
                    result.extend(dic[letter]['paths'])
                    continue
                for j in range(len(letter)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        temp = letter[:j]+ch+letter[j+1:]
                        if dic.has_key(temp) and dic[temp]['depth']>dic[letter]['depth']:
                            # Only sibling nodes can share child node
                            if dic[temp]['depth']==DEFAULT_DEPTH:
                                queue[(i+1)%2].append(temp)
                                dic[temp]['depth'] = dic[letter]['depth']+1
                            for p in dic[letter]['paths']:
                                path = p[:]
                                path.append(temp)
                                dic[temp]['paths'].append(path)
            if len(result)>0 or len(queue[(i+1)%2])==0:
                return result
        return result
        
        
    def transferable(self, origin, target): 
        return 1 == sum([origin[i]!=target[i] for i in range(len(origin))])
     
     
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders1(self, start, end, dict):
        # learn from Dijkstra, mark node's parent, and use it to find the path
        # for the order of path, we can just to find all path from 'end'
        dic, DEFAULT_DEPTH, queue = {}, len(dict)+3, [end]
        for letter in dict:
            dic[letter] = {'depth':DEFAULT_DEPTH,'parents':[]} # not used yet
        dic[end] = {'depth':1,'parents':[]}
        dic[start] = {'depth':DEFAULT_DEPTH,'parents':[]}
        while len(queue)>0:
            letter = queue.pop(0)
            if letter == start: break
            for i in range(len(letter)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    temp = letter[:i]+ch+letter[i+1:]
                    if dic.has_key(temp) and dic[temp]['depth']>dic[letter]['depth']:
                        # Only sibling nodes can share child node
                        if dic[temp]['depth']==DEFAULT_DEPTH:
                            queue.append(temp)
                        dic[temp]['depth'] = dic[letter]['depth']+1
                        dic[temp]['parents'].append(letter)
        return self.genPath(start, dic, []) if len(dic[start]['parents'])>0 else [];
        
    def genPath(self, node, dic, path):
        path.append(node)
        if len(dic[node]['parents'])==0: return [path]
        result = []
        for p in dic[node]['parents']:
            temp_path = path[:]
            result.extend(self.genPath(p, dic, temp_path))
        return result

if __name__ == '__main__':
    s = Solution()
    print s.findLadders1("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"])
