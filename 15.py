from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        l = 0
        r = len(nums) - 1
        nums.sort()
        while(l + 1 < r):
            m = l + 1
            while(m < r):
                if (nums[l] + nums[m] + nums[r] == 0):
                    result.append([nums[l], nums[m], nums[r]])
                m += 1
            if ()
