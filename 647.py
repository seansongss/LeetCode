class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0
        for len_s in range(1, len(s)+1):
            for i in range(len(s) + 1 - len_s):
                if len_s == 1:
                    dp[len_s-1][i] = True
                    res += 1
                elif len_s == 2:
                    if s[i] == s[i+1]:
                        dp[len_s-1][i] = True
                        res += 1
                else:
                    prev_len = len_s - 2
                    if dp[prev_len-1][i+1] and s[i] == s[i+len_s-1]:
                        dp[len_s-1][i] = True
                        res += 1
        
        return res
