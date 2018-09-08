class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        turn = len(nums) & 1
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)):
            if turn:
                dp[i][i] = nums[i]
            else:
                dp[i][i] = 0
        for k in range(1, len(nums)):
            turn ^= 1
            for i in range(len(nums) - k):
                j = i + k
                if turn:
                    dp[i][j] = max(dp[i][j-1] + nums[j], dp[i+1][j] + nums[i])
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i+1][j])
        return 2 * dp[0][len(nums)-1] >= sum(nums)
