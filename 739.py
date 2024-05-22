from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        print(answer)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                answer[index] = i - index
            
            stack.append(i)
        
        return answer
    
temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))
