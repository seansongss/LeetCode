class Solution:
    def climbStairs(self, n: int) -> int:
        def countStairs(step_left):
            if step_left == 0:
                return 1
            elif step_left < 0:
                return 0
            return countStairs(step_left-1) + countStairs(step_left-2)
        
        count = countStairs(n)
        return count