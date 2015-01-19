#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        f = lambda n: "".join([" "]*n)
        result, word, line, cur_len = [], "", [], -1    # -1 for one space
        for word in words:
            if cur_len+1+len(word)>L:   # can't add this word into this line
                if len(line)==0: return None    # can't contain this word in one line
                if len(line)==1:        # left-justified
                    result.append(line[0]+f(L-cur_len))
                else:
                    m, c = (L-cur_len)/(len(line)-1)+1, (L-cur_len)%(len(line)-1)
                    if c==0:
                        result.append(f(m).join(line))
                    else:
                        result.append(f(m+1).join(line[:c+1])+f(m)+f(m).join(line[c+1:]))
                line, cur_len = [], -1  # -1 for last space
            # add this new word to current line
            line.append(word)
            cur_len += len(word)+1  # one space
        # left-justified for the last line
        result.append(" ".join(line)+f(L-cur_len))
        return result
    
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify1(self, words, L):
        f = lambda n: "".join([" "]*n)
        i, len_words, result = 0, len(words), []
        while i<len_words:
            cur_len, j = 0, i
            while j<len_words and cur_len+len(words[j])+j-i<=L:
                j, cur_len = j+1, cur_len+len(words[j])
            
            line, spaces = words[i], L-cur_len
            for i in xrange(i+1, j):
                sp = (spaces+j-i-1)/(j-i) if j<len_words else 1
                line += f(sp)
                line += words[i]
                spaces -= sp
            line += f(L-len(line))  # for last line
            result.append(line)
            i += 1      # for 真难使
        return result
                    

if __name__ == '__main__':
    pass
