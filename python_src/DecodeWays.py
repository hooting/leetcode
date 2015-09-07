class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0: return 0 
        kinds = [0] * len(s)
        if s[0] == '0': kinds[0] = 0
        else: kinds[0] = 1
        for i in range(1,len(s)):
            if int(s[i]) > 0:
                kinds[i] += kinds[i-1]
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                if i == 1:kinds[i] += 1
                else: kinds[i] += kinds[i-2]
        return kinds[len(s) - 1]
            