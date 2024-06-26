from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while (l < r):
            max_height = min(height[l], height[r])
            if (max_height * (r - l) > max_area):
                max_area = max_height * (r - l)
            
            if (height[l] > height[r]):
                r -= 1
            else:
                l += 1
        return max_area