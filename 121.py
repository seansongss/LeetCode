from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for i in prices[1:]:
            if i < lowest:
                lowest = i

            max_profit = max(max_profit, i - lowest)
        
        return max_profit