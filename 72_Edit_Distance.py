class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = list()
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 and j == 0:
                    dp.append(0)
                elif i == 0:
                    dp.append(j)
                else:
                    if j == 0:
                        temp = dp[0]    # 记录 dp[i-1][j-1]
                        dp[0] += 1
                    else:
                        temp2 = dp[j]
                        if word1[i - 1] == word2[j - 1]:
                            dp[j] = temp
                        else:
                            dp[j] = min(dp[j], dp[j-1]) + 1
                        temp = temp2
        return dp[-1]
            