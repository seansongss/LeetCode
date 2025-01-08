class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bs(nums, target, findStart):
            l, r = 0, len(nums) - 1
            pos = -1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    pos = mid
                    if findStart:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                
            return pos
        
        start_pos = bs(nums, target, True)
        end_pos = bs(nums, target, False)

        return [start_pos, end_pos]