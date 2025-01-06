class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(list, cur, digits):
            if not digits:
                if cur:
                    return list.append(cur)
                else:
                    return list
            
            for letter in digit_to_letter[digits[0]]:
                dfs(list, cur + letter, digits[1:])
            
            return list
        
        digit_to_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        sol = dfs([], "", digits)
        return sol
    
sol = Solution().letterCombinations("")
print(sol)
