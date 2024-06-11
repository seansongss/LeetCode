from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arrays = []
        num = 1
        min_val = min(candidates)
        def backtrack(num, remain, arr):
            if num == 0 and remain == 0:
                arrays.append(arr)
                return
            elif num == 0 or remain < 0:
                return
            else:
                for i in candidates:
                    new_arr = arr + [i]
                    backtrack(num - 1, remain - i, new_arr)
                
        while True:
            if not candidates or min_val * num > target:
                res = []
                for array in arrays:
                    array.sort()
                    if not array in res:
                        res.append(array)
                return res
            else:
                backtrack(num, target, [])
                num += 1

print(Solution().combinationSum([8,7,4,3], 11))