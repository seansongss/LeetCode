from typing import List, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]
    
a = Solution()
print(a.topKFrequent([1,1,1,2,2,3], 2))

#sol