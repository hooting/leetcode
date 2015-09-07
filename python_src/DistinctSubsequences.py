#reference to https://leetcode.com/discuss/2143/any-better-solution-that-takes-less-than-space-while-in-time
#Solution (DP):
#We keep a m*n matrix and scanning through string S, while
#m = T.length() + 1 and n = S.length() + 1
#and each cell in matrix Path[i][j] means the number of distinct subsequences of 
#T.substr(1...i) in S(1...j)
# Path[i][j] = Path[i][j-1]            (discard S[j])
#              +     Path[i-1][j-1]    (S[j] == T[i] and we are going to use S[j])
#                 or 0                 (S[j] != T[i] so we could not use S[j])
# while Path[0][j] = 1 and Path[i][0] = 0.
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sLen = len(s)
        tLen = len(t)
        if tLen > sLen: return 0
        dis = [[0] * (sLen + 1) for x in range(tLen + 1)]
        for i in range(sLen + 1): dis[0][i] = 1
        for i in range(1,tLen+1):
            for j in range(1,sLen+1):
                dis[i][j] += dis[i][j-1]
                if t[i-1] == s[j-1]:
                    dis[i][j] += dis[i-1][j-1]
        return dis[tLen][sLen]
        