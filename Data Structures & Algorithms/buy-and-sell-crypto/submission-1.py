class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = 0, 1
        maxProfit = 0
        while high < len(prices):
            if prices[low] > prices[high]:
                low = high
            else:
                maxProfit = max(prices[high] - prices[low], maxProfit)
            high += 1
        return maxProfit 