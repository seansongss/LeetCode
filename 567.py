class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_len = len(s1)
        s2_len = len(s2)
        while l + s1_len <= s2_len:
            tmp = s1
            for i in s2[l:l+s1_len]:
                if i in tmp:
                    tmp = tmp.replace(i, "", 1)
                else:
                    break
            if len(tmp) == 0:
                return True
            l += 1
            
        return False
    
print(Solution().checkInclusion("ccc", "cbac"))