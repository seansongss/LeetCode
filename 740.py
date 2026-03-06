class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        nums.sort()
        num_dict = {}
        num_set = set()
        for num in nums:
            if num not in num_dict.keys():
                num_dict[num] = 0
            num_dict[num] += 1
            num_set.add(num)
        num_lst = list(num_set)
        dp = [0] * len(num_lst)
        dp[0] = num_lst[0] * num_dict[num_lst[0]]

        if len(num_lst) == 1:
            return dp[0]

        if num_lst[1] - 1 == num_lst[0]:
            dp[1] = max(dp[0], num_lst[1] * num_dict[num_lst[1]])
        else:
            dp[1] = dp[0] + num_lst[1] * num_dict[num_lst[1]]

        for i in range(2, len(num_lst)):
            num = num_lst[i]
            total = num * num_dict[num]

            if num - 1 not in num_dict.keys():
                dp[i] = dp[i-1] + total
            else:
                dp[i] = max(dp[i-2] + total, dp[i-1])
            print(dp[i])
        return dp[-1]
