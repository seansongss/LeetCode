class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # l = 0
        # s1_len = len(s1)
        # s2_len = len(s2)
        # while l + s1_len <= s2_len:
        #     tmp = s1
        #     for i in s2[l:l+s1_len]:
        #         if i in tmp:
        #             tmp = tmp.replace(i, "", 1)
        #         else:
        #             break
        #     if len(tmp) == 0:
        #         return True
        #     l += 1
            
        # return False
        arr = [0] * 26
        for l in s1:
            arr[ord(l) - ord('a')] += 1
        l = 0
        sub_arr = [0] * 26
        def isEqual():
            for i in range(26):
                if arr[i] != sub_arr[i]:
                    return False
            return True
        for r in range(len(s2)):
            i = ord(s2[r]) - ord('a')
            sub_arr[i] += 1
            if isEqual():
                return True
            while sub_arr[i] > arr[i]:
                sub_arr[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False
    
# print(Solution().checkInclusion("ccc", "cbac"))