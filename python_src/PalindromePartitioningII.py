"""
reference to https://leetcode.com/discuss/6691/my-dp-solution-explanation-and-code
Calculate and maintain 2 DP states:

pal[i][j] , which is whether s[i..j] forms a pal

d[i], which is the minCut for s[i..n-1]

Once we comes to a pal[i][j]==true:

if j==n-1, the string s[i..n-1] is a Pal, minCut is 0, d[i]=0;
else: the current cut num (first cut s[i..j] and then cut the rest s[j+1...n-1]) is 1+d[j+1], 
compare it to the exisiting minCut num d[i], repalce if smaller.
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        cut = [0] * length
        is_palindrome = [[False for x in range(length)] for x in range(length)]
        for i in range(length):
            cut[i] = i
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i - j < 2 or is_palindrome[j+1][i-1]):
                    is_palindrome[j][i] = True
                    if j == 0:
                        cut[i] = 0
                    else:
                        cut[i] = min(cut[i],1 + cut[j-1])
        return cut[length - 1]
        