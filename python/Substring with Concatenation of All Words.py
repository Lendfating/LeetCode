#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

方案一： 最基本的，用hash去记录每个单词，然后subStr的下标顺序遍历S，依次查看从i位置开始的连续子串是否包含所有单词。
        注意，同一单词可能会出现多次，因此用计数，而非bool

方案二：在方案一的基础上，考虑优化。方案一存在的重复遍历情况放生在“重复单词”的处理。因此，方案二就以单词为单位进行遍历，对已经查找过的单词，在后续子串的匹配中考虑跳转

方案三：结合方案二的实现，会发现跳跃的过程指针 j一直没有折回现象，此时利用start记录当前有效串的长度。可以在转变一个思路，固定子串长度，检查子串内有效单词数，即滑动窗口的策略。

最后提供了一个看着玩的hash策略，但是hash很难保证，所以真实情况下不能使用。
"""
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if len(L)==0: return []
        map, map1, result, len_L, len_w = {}, {}, [], len(L), len(L[0])
        for item in L:
            map[item] = map[item]+1 if map.has_key(item) else 1
            map1[item] = map[item]
        for i in xrange(len(S)-len_w*len_L+1):
            for j in xrange(len_L):
                word = S[i+j*len_w:i+(j+1)*len_w]
                if map.has_key(word) and map[word]>0:
                    map[word] = map[word]-1
                else:
                    for k in xrange(j): map[word] = map1[word]
                    break
            else:
                result.append(i)
                
        return result
    
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring1(self, S, L):
        # continue optimize
        """
        a) initially store the number of occurences of each word in Hash table "cn".
        b) For i = 0 to w
            start = i; 
            For w : all words at intervals i, i+w, i+2w, .. n
                i) check if word w is  valid, if not set start to next word as the substring uptil now will be invalid.

                ii) if word is valid, check the number of occurences of this word in the substring is less than availbale words increment count of the word in the hash table cntL 

                iii) if the word is valid , but already occured maximum number of times, then consider the substring starting after the first occurence of this word.set start.

            if (all the dictionary words are used then store the start as the valid substring start.
        """
        if len(L)==0: return []
        map, result, len_S, len_L, len_w = {}, [], len(S), len(L), len(L[0])
        for item in L:
            map[item] = map[item]+1 if map.has_key(item) else 1
        for start in xrange(len_w):
            map1, j = map.copy(), 0       # response the length of the words has matched
            while start<=len_S-len_L*len_w:
                while j<len_L:
                    word = S[start+j*len_w:start+(j+1)*len_w]
                    if map1.has_key(word) and map1[word]>0:
                        map1[word], j = map1[word]-1, j+1
                    else:
                        while S[start:start+len_w]!=word:
                            map1[S[start:start+len_w]] += 1
                            start, j = start+len_w, j-1
                        start += len_w
                        if start>len_S-len_L*len_w: break
                else:
                    result.append(start)
                    map1[S[start:start+len_w]] += 1
                    start, j = start+len_w, j-1
        return result
    
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring2(self, S, L):
        # use slide window
        if len(L)==0: return []
        map, result, len_S, len_L, len_w = {}, [], len(S), len(L), len(L[0])
        for item in L:
            map[item] = map[item]+1 if map.has_key(item) else 1
        len_map = len(map)
        for start in xrange(len_w):
            map1, cnt = map.copy(), 0
            # the right end of the window
            for j in xrange((len_S-start)/len_w):
                word = S[start+j*len_w:start+(j+1)*len_w]
                if map1.has_key(word):
                    map1[word] -= 1
                    if map1[word]==0: cnt += 1  # the count of word occur in window
                if cnt==len_map: result.append(start+(j+1-len_L)*len_w)
                if j>=len_L-1:
                    word = S[start+(j+1-len_L)*len_w:start+(j+2-len_L)*len_w]
                    if map1.has_key(word):
                        if map1[word]==0: cnt -= 1
                        map1[word] += 1
        return sorted(result)
    
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring3(self, S, L):
        # take full use of hash, but not insure right
        # just for fun, don't use it!
        n = len(L) #num words
        w = len(L[0])  #length of each word
        t = n*w    # total length
    
        hashsum = sum([hash(x) for x in L])
        h = [hash(S[i:i+w])*(S[i:i+w] in L) for i in xrange(len(S)-w+1)]
        return [i for i in xrange(len(S)-t+1) if sum(h[i:i+t:w])==hashsum]

if __name__ == '__main__':
    s = Solution()
    print s.findSubstring2("aaaaaaaa", ["aa","aa","aa"])
    print s.findSubstring1("barfoothefoobarman", ["foo","bar"])
    
    
