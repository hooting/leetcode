class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        size = len(s)
        ret = 0
        for i in range(0,size):
            ret += (ord(s[i]) - 65 + 1) * (26 ** (size - 1 - i))
        return ret