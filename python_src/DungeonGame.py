"""
reference to https://leetcode.com/discuss/20829/c-dp-solution
Use hp[i][j] to store the min hp needed at position (i, j), then do the calculation from right-bottom to left-up.
"""
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        column = len(dungeon[0])
        dp = [ [0] * column for x in range(row)]
        dp[row-1][column-1] = min(0,dungeon[row-1][column-1])
        for i in range(column-2,-1,-1):
            dp[row-1][i] = min(0,dp[row-1][i+1]+dungeon[row-1][i])# last row
        for i in range(row-2,-1,-1):
            dp[i][column-1] = min(0,dp[i+1][column-1] + dungeon[i][column-1])#last column
        for i in range(row-2,-1,-1):
            for j in range(column-2,-1,-1):
                dp[i][j] = min(0,max(dp[i+1][j] + dungeon[i][j],dp[i][j+1] + dungeon[i][j]))
        return -dp[0][0] + 1