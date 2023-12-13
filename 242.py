# s = "ab"
# t = "a"
# if len(s) == len(t):
#     for i in range(len(t)):
#         s = s.replace(t[i], '', 1)
#     print(len(s))
# else:
#     print(-1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in range(len(t)):
                s = s.replace(t[i], '', 1)
            return len(s) == 0
        return False