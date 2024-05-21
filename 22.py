from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, s):
            if len(s) == 2 * n:
                result.append(s)
                return

            if left < n:
                backtrack(left + 1, right, s + '(')
            if left > right:
                backtrack(left, right + 1, s + ')')

        result = []
        backtrack(0, 0, '')
        return result