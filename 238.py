class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        solution = [1] * length
        pre = 1
        post = 1

        for i in range(length):
            solution[i] *= pre
            pre = pre * nums[i]
            solution[length - i - 1] *= post
            post = post * nums[length - i - 1]

        return solution