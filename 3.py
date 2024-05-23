class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        longest = set()

        for right in range(len(s)):
            while s[right] in longest:
                longest.remove(s[left])
                left += 1
            
            longest.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len