class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_profit = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_profit:
                min_profit = prices[i]
            profit_tmp = prices[i] - min_profit
            if profit_tmp > profit:
                profit = profit_tmp
            

        return profit
         