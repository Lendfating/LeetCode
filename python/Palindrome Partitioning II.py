#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

基本思想就是动归。
方案一：依次统计s的所有前缀子串的切分次数。对某个给定的前缀子串 s[:end], 我们仅需要查看所有以end结束的子串是否是回文序列，
    如果是，则我们可以考虑利用 nums[start]+1去更新该前缀子串 s[:end]的切分结果。
    
方案二：还是针对上述方案，其时间复杂度为 O(n^3)， 因为判断回文序列的时候我们对每一个子串都是从头到尾检查了一遍，明显浪费了很多时间。
    所以，考虑回文序列检查过程的优化。对于某个字串 s[start:end]，如果是回文序列，则s[start]==s[end]，且s[start+1:end-1]
    也是回文序列。而我们还注意到，当我们在判断 s[start:end] 是否是回文序列时，早已经进行过 s[start+1:end-1]的判断，因此
    我们可以采用动态规划的方法，对每一步判断回文序列的结果也进行记录，方便后续使用。
    
方案三：针对方案二，我们再进一步看看还有什么地方可以优化。时间已经不可优化，主要看空间。观察我们记录回文序列的过程，我们可以思考
    因为每个回文序列的结果在纪录之后只被使用了一次，因此我们可以考虑一下是不是可以不记录直接使用？
    那么我们就需要按回文序列之间的转换关系进行组织遍历，而不再是方案一中的s[:end]前缀子串。我们注意到，回文序列的扩张是通过两边
    增加相同的字符组成的，也就是说回文序列具有对称性，我们根据对称性信息可以不必记录之前所有的回文检测信息，只需记录当前状态即可，
    因此，我们不再用前缀子串 s[:end]的方式遍历s的子结构，而是以回文中点的方式构造子结构，即以mid进行遍历， s[:mid+l]才构成s
    的前缀子串。
    经过仔细分析，我们会发现这种访问顺序是合理的，没有打破子结构件的依赖顺序。


"""
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if len(s)==0: return 0
        nums = [1<<32]*(len(s)+1)
        nums[0] = -1
        for end in xrange(1, len(s)+1):
            for start in xrange(end):
                if self.isPalindrome(s[start:end]):
                    nums[end] = min(nums[end], nums[start]+1)
        return nums[-1]
                
    def isPalindrome(self, s):
        return s==s[::-1]
    
    # @param s, a string
    # @return an integer
    def minCut1(self, s):
        if len(s)==0: return 0
        pals = [[False]*len(s) for i in s]
        nums = [i-1 for i in xrange(len(s)+1)]
        for end in xrange(len(s)):
            for start in xrange(end+1):
                if s[start]==s[end] and (start+1>=end or pals[start+1][end-1]):
                    pals[start][end] = True
                    nums[end+1] = min(nums[end+1], nums[start]+1)
        return nums[-1]
    
    # @param s, a string
    # @return an integer
    def minCut2(self, s):
        if len(s)==0: return 0
        length = len(s)
        nums = [i-1 for i in xrange(length+1)]
        for mid in xrange(length):
            for l in xrange(min(mid+1, length-mid)):    # for the odd length
                if s[mid-l]!=s[mid+l]: break
                nums[mid+l+1] = min(nums[mid+l+1], nums[mid-l]+1)
            for l in xrange(min(mid+1, length-mid-1)):  # for the even length
                if s[mid-l]!=s[mid+l+1]: break
                nums[mid+l+2] = min(nums[mid+l+2], nums[mid-l]+1)
        return nums[-1]
    

if __name__ == '__main__':
    pass
