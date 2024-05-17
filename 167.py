from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (True):
            total = numbers[l] + numbers[r]
            if (total < target):
                l += 1
            elif (total > target):
                r -= 1
            else:
                return [l + 1, r + 1]

# print(Solution().twoSum([2,7,11,15], 9))
# print(Solution().twoSum([2,3,4], 6))
# print(Solution().twoSum([-1,0], -1))
# print(Solution().twoSum([0,0,3,4], 0))