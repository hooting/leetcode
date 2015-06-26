class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n <= 0:
            return 0
        ways = [];
        ways.append(1)
        ways.append(2)
        steps = 2
        while steps < n:
            ways.append(ways[steps - 1] + ways[steps - 2])
            steps += 1
        return ways[n - 1]
        