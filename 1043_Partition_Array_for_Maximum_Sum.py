class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * len(A)
        for i in range(0, len(A)):
            cur_max = -1
            for k in range(1, min(K, i + 1) + 1):       # k 表示最后一组有几个数
                cur_max = max(cur_max, A[i - k + 1])
                if i + 1 == k:                          # 所有的都为一组
                    dp[i] = max(dp[i], cur_max * k)
                else:
                    dp[i] = max(dp[i], dp[i - k] + cur_max * k)
        # print(dp)
        return dp[-1]
