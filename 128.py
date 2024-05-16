from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        count = 0
        current = -1
        for i in num_set:
            if (i-1) not in num_set:
                length = 1
                while (i+length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
    
print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
