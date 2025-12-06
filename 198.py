class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        prev = nums.pop(0)
        curr = max(nums.pop(0), prev)
        
        for i, n in enumerate(nums):
            tmp = prev + n
            prev = max(prev, curr)
            curr = tmp
        
        return max(curr, prev)
