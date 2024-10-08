class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def backtracking(remain, count):
        #     if remain == 0:
        #         return count
        #     if remain < 0:
        #         return float("inf")
        #     min_coins = float("inf")
        #     for coin in coins:
        #         result = backtracking(remain - coin, count + 1)
        #         min_coins = min(result, min_coins)
        #     return min_coins
        # result = backtracking(amount, 0)
        # return result if result != float("inf") else -1
        
        # Tạo mảng dp với kích thước amount + 1, khởi tạo tất cả là vô cực
        dp = [float('inf')] * (amount + 1)
        
        # Không cần đồng xu nào để tạo ra số tiền 0
        dp[0] = 0
        
        # Lặp qua tất cả các số tiền từ 1 đến amount
        for i in range(1, amount + 1):
            # Thử từng đồng xu
            for coin in coins:
                if i - coin >= 0:  # Chỉ xét khi số tiền còn lại >= 0
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Nếu dp[amount] vẫn là vô cực, nghĩa là không thể đổi được số tiền đó
        return dp[amount] if dp[amount] != float('inf') else -1
        