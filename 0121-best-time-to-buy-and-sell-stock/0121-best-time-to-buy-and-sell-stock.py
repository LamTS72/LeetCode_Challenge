class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            tmp_profit = prices[i] - min_price
            if tmp_profit > max_profit:
                max_profit = tmp_profit
        return max_profit

