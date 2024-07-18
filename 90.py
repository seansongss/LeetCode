from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def re(index, t):
            col.append(list(t))
            
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i-1]:
                    continue
                t.append(nums[i])
                re(i + 1, t)
                t.pop()
        col = []
        nums.sort()
        re(0, [])
        return col
        
print(Solution().subsetsWithDup([1,2,2]))