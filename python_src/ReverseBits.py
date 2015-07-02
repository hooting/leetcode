class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        dic = dict()
        value = 1
        for i in range(0,32):
            dic[i] = value
            value *= 2
        result = 0
        for k in reversed(dic.keys()):
            if dic[k] > n: continue
            n -= dic[k]
            result += dic[31 - k]
        return result
            
        