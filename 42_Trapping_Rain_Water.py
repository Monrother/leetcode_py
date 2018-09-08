class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left = [0]
        right = [0]
        temp = height[0]
        for i in range(1, len(height)):
            left.append(temp)
            temp = max(temp, height[i])
        temp = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right.insert(0, temp)
            temp = max(temp, height[i])
        count = 0
        for i in range(1, len(height) - 1):
            temp = min(left[i], right[i])
            if temp > height[i]:
                count += temp - height[i]
        return count
