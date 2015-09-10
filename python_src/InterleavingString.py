"""
refernce to https://leetcode.com/discuss/11694/my-dp-solution-in-c
Here is some explanation:

DP table represents if s3 is interleaving at (i+j)th position when s1 is at ith position, and s2 is at jth position. 0th position means empty string.

So if both s1 and s2 is currently empty, s3 is empty too, and it is considered interleaving. If only s1 is empty, then if previous s2 position is interleaving and current s2 position char is equal to s3 current position char, it is considered interleaving. similar idea applies to when s2 is empty. when both s1 and s2 is not empty, then if we arrive i, j from i-1, j, then if i-1,j is already interleaving and i and current s3 position equal, it s interleaving. If we arrive i,j from i, j-1, then if i, j-1 is already interleaving and j and current s3 position equal. it is interleaving.
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1,len2,len3 = len(s1),len(s2),len(s3)
        if len1 + len2 != len3: return False
        table = [[False] * (len2 + 1) ] * (len1 + 1)
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == j == 0:
                    table[i][j] = True
                elif i == 0:
                    table[i][j] = table[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    table[i][j] = table[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    table[i][j] = (table[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (table[i][j - 1] and s2[j-1] == s3[i+j-1])
        return table[len1][len2]
        
        