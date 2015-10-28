class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 0x7fffffff
        max_profit = 0
        for price in prices:
            if price > min_price:
                max_profit += price - min_price
            min_price = price
        return max_profit
        