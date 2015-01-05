#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        # use the slope and a passed point can indentify a line.
        result = min(2, len(points));
        for i in xrange(len(points)-1):
            slopes, duplicate = {}, 0;
            for j in xrange(i+1, len(points)):
                if points[i].x==points[j].x and points[i].y==points[j].y:
                    duplicate += 1;
                    continue;
                _gcd = self.gcd(points[i].y-points[j].y, points[i].x-points[j].x);
                # note: since the sign of reminder is same to the dividend, so key will be (?, 0 or 1)
                # if points[i].x-points[j].x<0: _gcd = -abs(_gcd);
                key = ((points[i].y-points[j].y)/_gcd, (points[i].x-points[j].x)/_gcd);
                slopes[key] = slopes[key]+1 if slopes.has_key(key) else 2;
            for key in slopes.keys():
                result = max(result, slopes[key]+duplicate);
            result = max(result, 1+duplicate);
        return result;
    
    # get the greatest common divisor
    def gcd(self, a, b):
        if b==0:
            return a;
        else:
            return self.gcd(b, a%b);
        
if __name__ == '__main__':
    points = [Point(), Point(1,1), Point(1,-1)]
    s = Solution()
    print s.maxPoints(points)
