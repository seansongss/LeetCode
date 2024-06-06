class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_str = 0
        l = 0
        freq = {}
        for r in range(len(s)):
            if not s[r] in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1

            count = r - l + 1
            if count - max(freq.values()) <= k:
                longest_str = max(longest_str, count)
            else:
                freq[s[l]] -= 1
                if not freq[s[l]]:
                    freq.pop(s[l])
                l += 1

        return longest_str
