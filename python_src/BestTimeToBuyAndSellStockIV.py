"""
reference to https://leetcode.com/discuss/25603/a-concise-dp-solution-in-java
temp_max = (max profit in (i - 1) transactions and j - 1 prices) + 
            (the lowest price between h(we assume the (i-1)th transaction end at price h - 1) to j - 1) 
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        num = len(prices)
        
        if(k > num / 2):
            max_profit = 0
            for i in range(1,num):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i] - prices[i-1]
            return max_profit
        result = [[0] * num  for i in range(k+1)]
        for i in range(1,k+1):
            temp_max = -prices[0]
            for j in range(1,num):
                result[i][j] = max(result[i][j-1], temp_max + prices[j])
                temp_max = max(temp_max, result[i-1][j-1] - prices[j])
        return result[k][num - 1]