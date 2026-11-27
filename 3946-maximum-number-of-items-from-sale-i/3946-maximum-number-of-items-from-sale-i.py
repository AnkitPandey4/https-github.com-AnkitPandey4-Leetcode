class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        dp = [0] * (budget + 1)
        min_price = min(price for _, price in items)

        for factor, price in items:
            gain = sum(1 for other_factor, _ in items if other_factor % factor == 0)
            for b in range(budget, price - 1, -1):
                if dp[b - price] + gain > dp[b]:
                    dp[b] = dp[b - price] + gain

        return max(dp[spent] + (budget - spent) // min_price for spent in range(budget + 1))
