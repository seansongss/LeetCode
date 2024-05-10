class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_num = {}
        for i in nums:
            if (freq_num.get(i)):
                freq_num[i] += 1
            else:
                freq_num[i] = 1
        
        freq_num = dict(sorted(freq_num.items(), key=lambda item: item[1]))
        freq_list = list(freq_num.keys())
        freq_len = len(freq_num)
        
        result = []
        for i in range(k):
            result.append(freq_list[freq_len - i - 1])

        return result
    
a = Solution()
print(a.topKFrequent([1,1,1,2,2,3], 2))