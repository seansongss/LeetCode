from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def costCalc(step):
           if step < 2:
               return cost[step]
           if step not in memo:
               memo[step] = cost[step] + min(costCalc(step - 1), costCalc(step - 2))
           
           return memo[step]
        
        memo = {}
        length = len(cost)
        return min(costCalc(length - 1), costCalc(length - 2))