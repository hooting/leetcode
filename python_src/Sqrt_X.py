#reference to :
#https://leetcode.com/discuss/8897/share-my-o-log-n-solution-using-bit-manipulation
#the time complexity is in constant complexity
#the highest digit position is (1 << h) ** 2 <= x and (1 << (h + 1)) ** 2 > x
#we then, check its h - 1, h - 2, ..., 0 digit positions.
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0:
            return 0
        h = 0
        while (1 << h) * (1 << h) <= x:
            h += 1
        h -= 1
        gotten = 1 << h
        h -= 1
        while h >= 0:
            if (gotten | 1 << h) ** 2 <= x:
                gotten |= 1 << h
            h -= 1
        return gotten
        