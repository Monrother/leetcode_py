class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        l1 = len(s)
        l2 = len(t)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1 + 1)]
        dp[0][0] = 1
        for i in range(l1 + 1):
            for j in range(min(i+1, l2+1)):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = dp[i-1][j]
                if j > 0 and s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[l1][l2]
    