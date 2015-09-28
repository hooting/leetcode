class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = map[s[0]]
        same_time = 1
        for i in range(1,len(s)):
            result += map[s[i]]
            if s[i] == s[i-1]:
                same_time += 1
            else:
                if map[s[i]] > map[s[i-1]]:
                    result -= map[s[i-1]] * same_time * 2
                same_time = 1
        return result
        
        