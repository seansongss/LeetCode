class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            if w*h > max_area:
                max_area = w*h
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area