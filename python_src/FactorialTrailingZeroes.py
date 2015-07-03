class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        ret = 0
        while 5 <= n:
            n = n / 5
            ret += n
        return ret