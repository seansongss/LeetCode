class Solution:
    def climbStairs(self, n: int) -> int:
        # def countStairs(step_left):
        #     if step_left == 0:
        #         return 1
        #     elif step_left < 0:
        #         return 0
        #     return countStairs(step_left-1) + countStairs(step_left-2)
        
        # count = countStairs(n)
        # return count
        def solve(n, dp):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = solve(n - 1, dp) + solve(n -2, dp)

            return dp[n]

        dp = [-1] * (n+1)
        return solve(n, dp)