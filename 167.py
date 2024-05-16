from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sorted_num = numbers
        sorted_num.sort()

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if sorted_num[i] + sorted_num[j] == target:
                    return [numbers.index(sorted_num[i]) + 1, numbers.index(sorted_num[j]) + 1]
                
# print(Solution().twoSum([2,7,11,15], 9))
# print(Solution().twoSum([2,3,4], 6))
# print(Solution().twoSum([-1,0], -1))
print(Solution().twoSum([0,0,3,4], 0))