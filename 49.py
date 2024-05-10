from typing import List, DefaultDict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_map = DefaultDict(list)

        for word in strs:
            soreted_word = ''.join(sorted(word))
            anag_map[soreted_word].append(word)
        
        return list(anag_map.values())
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(["","", ""]))