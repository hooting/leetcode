#reference to https://leetcode.com/discuss/44281/4-lines-o-log-n-c-java-python
#for each m, we calculate the one number in the m digit position
class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        ones = 0
        m = 1
        while m <= n:
            a = n / m 
            ones += (a / 10) * m
            if (a % 10 >= 2):
                ones += m
            elif (a % 10 == 1):
                ones += n % m + 1
            m *= 10
        return ones
            
        