class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev, curr = nums[0], max(nums[0], nums[1])
        for n in nums[2:-1]:
            tmp = prev + n
            prev = max(prev, curr)
            curr = tmp
        first = max(prev, curr)
        
        prev, curr = nums[1], max(nums[1], nums[2]) 
        for n in nums[3:]:
            tmp = prev + n
            prev = max(prev, curr)
            curr = tmp
        last = max(prev, curr)

        return max(first, last)