#reference to:
#https://leetcode.com/discuss/34918/one-line-c-solution
#if n > m, then the lowest bit must be 0,
#thus, the result is depended on the rest bits of m and n
#PS: there is no way that n < m
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        if n > m: return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1
        else: return m
    
        