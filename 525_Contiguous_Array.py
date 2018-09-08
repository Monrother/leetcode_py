class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        mapping = {0: 0}
        max_len = 0
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in mapping:
                max_len = max(i - mapping[count] + 1, max_len)
            else:
                mapping[count] = i + 1
        return max_len