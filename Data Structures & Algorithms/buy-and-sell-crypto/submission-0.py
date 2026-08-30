class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)-1, -1, -1):
            if i !=0:
                if (prices[i] - min(prices[:i])) > max:
                    max = prices[i] - min(prices[:i])
                
        return max