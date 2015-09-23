class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        d = dict()
        start = 0
        for index, value in enumerate(s):
            if value in d and d[value] >= start:
                length = index - start
                result = max(result,length)
                start = d[value] + 1
            d[value] = index
        result = max(result, len(s) - start)
        return result
        