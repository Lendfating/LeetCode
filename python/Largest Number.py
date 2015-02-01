#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

思路都一样，自定义比较顺序的排序。
如何确定两个元素的大小，即谁在前，谁该在后？
找规律进行比较太费劲了，直接利用规则 y+x>x+y来比较 x与y的顺序即可。
这个式子有点难证明。主要是中间状态可能会有影响，比如 "30 5 304" > "304 5 30"
如果x/y 相邻，则上式成立易证。如果不相邻，那么就得好好考虑一下排序过程，是否能够确保该数据能够更好地传递。
结合最终结果的状态，（num列表单调有序），所以上述担心的情况应该不会出现。

我们可以考虑把所有数 按词典顺序进行组织，然后按数字组织称一层一层的桶，然后从最后一层桶向前整理结果即可。
对于两个串的前后顺序，应该结合其可能分配到桶的位置去考虑。
难点应该是父子桶之间的组合顺序，即对30和30303之间的顺序，确定比较复杂。

该题很明显，前缀大的放在前面，前缀小的放在后面。如果前缀相同，如30和303，则比较复杂，需要将303第三位开始，重现看做一个前缀，
在与前面比较。

（桶排序实现不是很靠谱。）

"""
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num=map(str,num)
        num = sorted(num, cmp=lambda x,y:cmp(y+x, x+y))
        return ''.join(num).lstrip('0') or '0'
            

if __name__ == '__main__':
    s = Solution()
    print s.largestNumber([1,2])
