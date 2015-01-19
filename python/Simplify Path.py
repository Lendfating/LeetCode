#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

Note: such as "/home//foo/", we should ignore the redundant slashes.
In my code, since I split path with '/', it will generate some '' between '//',
we need ignore it.

It's the same case for '///' and '////'...

"""
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        names = path.split('/')
        dirs, name = [], ""
        for name in names:
            if name=="" or name==".":
                pass
            elif name=="..":
                if len(dirs)>0: dirs.pop()
            else:
                dirs.append(name)
        return "/" + "/".join(dirs)
    

if __name__ == '__main__':
    s = Solution()
    print s.simplifyPath("/...")
