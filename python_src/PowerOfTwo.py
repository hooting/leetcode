class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        start = 1
        while n > start:
            start += start
        if n == start: return True
        else: return False
            