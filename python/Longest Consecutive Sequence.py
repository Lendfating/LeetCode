#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction
大胆发现区间之间的关系。很多性质可用
为了充分利用hash，最好将区间的两端都暴露出来。
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        # use hash to mark the info of count of consecutive begaining from current int
        # also mark the prev num for current num
        cons, prev, result = {}, {}, 1
        for item in num:
            cons[item] = 1
        for cur in cons:
            next = cur + cons[cur]
            if cons.has_key(next):
                cons[cur] += cons[next]
                while prev.has_key(cur):
                    cur = prev[cur]
                    cons[cur] += cons[next]
                prev[next] = cur
                result = max(result, cons[cur])
        return result
          
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive1(self, num):
        # use hash to save the left bound and right bound of each interval.
        # the bound inside interval may not be update. but the bounds of both side should be update.
        # for a num integer x:
        #        1) x inside a interval,(we have handle x yet), just ignore
        #        2) x will be the left bound of a new interval, update both left and right bound
        #        3) x will be the right bound of a new interval, update both left and right bound
        #        4) x will connect two intervals, update both left and right bound
        #    !note: since we need to check whether x is used, we must save visiting info
        lefts, rights, result = {}, {}, 0
        for k in num:
            if lefts.has_key(k): continue   # filter duplicate item
            l = lefts[k-1] if lefts.has_key(k-1) else k     # join with the left side interval
            r = rights[k+1] if rights.has_key(k+1) else k   # join with the right side interval
            lefts[r], rights[l] = l, r  # store the info
            lefts[k] = l    # !import: just mark as visted
            result = max(result, r-l+1)
        return result
            
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive2(self, num):
        # think it over, x can only be the left bound of a interval or the right bound of another intervial,
        # so, we can use one hash to save both left and right bound of a interval.
        # 
        # the bound inside interval may not be update. but the bounds of both side should be update.
        # for a num integer x:
        #        1) x inside a interval,(we have handle x yet), just ignore
        #        2) x will be the left bound of a new interval, update both left and right bound
        #        3) x will be the right bound of a new interval, update both left and right bound
        #        4) x will connect two intervals, update both left and right bound
        #    !note: since we need to check whether x is used, we must save visiting info
        bounds, result = {}, 0  # take full use of bounds, we can find the other bound with a bound of a interval.
        for k in num:
            if bounds.has_key(k): continue  # we have handled k, ignore
            bounds[k] = k   # for case 4, we need to mark it. 
            l = bounds[k-1] if bounds.has_key(k-1) else k   # left bound of the new interval
            r = bounds[k+1] if bounds.has_key(k+1) else k   # right bound of the new interval
            bounds[l], bounds[r] = r, l     # update the bounds info 
            result = max(result, r-l+1)     # update the longest length info
        return result
        

if __name__ == '__main__':
    s = Solution()
    print s.longestConsecutive1([9,-8,9,8,-7,9,-4,6,5,5,6,7,-9,-5,-4,6,-8,-1,8,0,1,5,4])
