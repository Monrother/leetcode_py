class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_map = {}
        ans = []
        for num in nums1:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1
        for num in nums2:
            if num in num_map:
                ans.append(num)
                num_map[num] -= 1
                if num_map[num] == 0:
                    num_map.pop(num)
        return ans
