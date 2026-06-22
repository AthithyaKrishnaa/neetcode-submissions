class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=0
        for i in range(len(prices)):
            min_price=min(prices[i],min_price)
            profit=prices[i]-min_price
            max_profit=max(max_profit,profit)
        return max_profit
