from typing import List, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # .most_common(n) returns a list of n most common elements
        # ex) Counter([1, 1, 1, 2, 2, 3]).most_common(2) = [(1, 3), (2, 2)]
        return [num for num, _ in counter.most_common(k)]

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))