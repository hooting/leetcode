class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        max_length = start = end = 0
        for i in range(size):
            j = k = i
            while k < size - 1 and s[k] == s[k+1]: k += 1
            i = k + 1
            while j > 0 and k < size - 1 and s[j-1] == s[k+1]: 
                j -= 1
                k += 1
            temp = k - j
            if temp > max_length:
                max_length = temp
                start = j
                end = k
        return s[start:end+1]