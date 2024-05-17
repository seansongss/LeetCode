from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        l = 0
        r = len(nums) - 1
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
                
            m = l + 1
            r = len(nums) - 1

            while m < r:
                total = nums[l] + nums[m] + nums[r]
                
                if total < 0:
                    m += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[l], nums[m], nums[r]])
                    m += 1

                    while nums[m] == nums[m - 1] and m < r:
                        m += 1
        return result
    
# print(Solution().threeSum([-1,0,1,2,-1,-4]))