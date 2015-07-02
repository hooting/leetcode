class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        num = 0
        while n > 0:
            num += 1
            n &= (n - 1)
        return num