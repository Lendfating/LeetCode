#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
Created on Nov 6, 2014

@author: Zhen
'''
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num)<4: return [];
        ans, cache, length = [], {}, len(num);
        num.sort();
        # 求和从右往左、遍历从左往右，这样可以很好的处理重复元素问题
        for i in range(length-1, 2, -1):
            if i<length-1 and num[i]==num[i+1]:continue;   # 跳过重复项
            for j in range(i-1, 1, -1):
                if j<i-1 and num[j]==num[j+1]:continue; # 跳过重复项
                sum = num[i]+num[j];
                if cache.has_key(sum):
                    cache[sum].append([j, i]);  # 下标包含的信息会更全
                else:
                    cache[sum] = [[j, i]];
        # 利用缓存信息重新计算     
        for i in xrange(length-3):
            if i>0 and num[i]==num[i-1]:continue;   # 跳过重复项
            for j in xrange(i+1, len(num)-2):
                if j>i+1 and num[j]==num[j-1]:continue;   # 跳过重复项
                sum = num[i]+num[j];
                if cache.has_key(target-sum):
                    for [k3,k4] in cache[target-sum]:
                        if j<k3:
                            ans.append([num[i],num[j],num[k3],num[k4]]);
        return ans;
        
            
    # 类似于threeSum的思路，但是由于python的问题，这个版本是不能通过的。
    def fourSum1(self, num, target):
        if len(num)<4: return [];
        ans = [];
        num.sort(); # 递增排序
        for i in xrange(len(num)-3):
            if i>0 and num[i]==num[i-1]:continue;   # 跳过重复项
            for j in xrange(i+1, len(num)-2):
                if j>i+1 and num[j]==num[j-1]:continue;   # 跳过重复项
                left, right = j+1, len(num)-1;
                while left<right:
                    sum = num[i]+num[j]+num[left]+num[right];
                    if (sum==target):
                        ans.append([num[i], num[j], num[left], num[right]]);
                        while left<right and num[left]==num[left+1]: left+=1;   # 跳过重复项
                        while left<right and num[right]==num[right-1]: right-=1;
                        left += 1;  # 不可直接跳出，中间还有可能存在别的匹配对
                        right -= 1;
                    elif sum<target:
                        left += 1;
                    else:
                        right -= 1;
        return ans;
    
        
        
if __name__ == '__main__':
    list = [1,1,1, 0 ,-1, 0, -2, 2];#[14,4,6,-1,10,9,-8,7,-13,14,-13,-11,-8,-9,11,14,-8,-14,-13,7,-10,-15,-13,-11,-11,11,14,13,2,-14,1,-7,-2,14,-1,-15,9,7,-1,3,6,1,7,5,-1,-5,4,-2,-4,-1,-9,-7,-1,-7,-11,3,12,10,-7,-1,12,1,8,-13,1,14,9,-13,6,-7,-3,-11,2,-11,10,-14,-1,-9,0,2,5,6,3,-11,6,7,0,3,3,0,-12,-8,-13,3,-14,-5,2,10,-11,-14,-12,1,-10,5,5,7,-1,11,14,6,-10,-4,-3,8,-7,10,1,8,-1,-11,-15,-6,-12,-13,12,-11]

    s = Solution();
    print s.fourSum(list,0);
    print s.fourSum1(list,0);
    