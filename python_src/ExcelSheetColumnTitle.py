class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        ret = []
        while n > 0:
            remainder = (n - 1) % 26
            ret.append(chr(remainder + 65))
            n = (n - 1) / 26
    
        ret.reverse()
        return "".join(ret)