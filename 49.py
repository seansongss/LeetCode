from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs] 
        result = []
        count = 0
        while strs:
            result.append([])
            result[count].append(strs[0])
            str1 = strs[0]
            strs.remove(str1)
            to_remove = []
            for j in strs:
                if sorted(str1) == sorted(j):
                    result[count].append(j)
                    to_remove.append(j)

            for j in to_remove:
                strs.remove(j)
                
            count += 1
        
        # if (sorted(strs[0]) == sorted(result[count - 1][0])):
        #     result[count - 1].append(strs[0])
        # else:
        #     result.append([])
        #     result[count].append(strs[0])
        
        return result
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(["","", ""]))