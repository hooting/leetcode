"""
reference to https://leetcode.com/discuss/56982/o-sqrt-n-in-ruby-c-c
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0: n /= 4
        if n % 8 == 7: return 4
        a = 0
        while a ** 2 <= n:
            b = int(math.sqrt(n - a ** 2))
            if a ** 2 + b ** 2 == n:
                if a == 0: return 1
                else: return 2
            a += 1
        return 3
        