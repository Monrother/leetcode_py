class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s1 = []
        left = []
        for i in range(len(heights)):
            while s1 and heights[i] <= heights[s1[-1]]:
                s1.pop()
            if s1:
                left.append(s1[-1])
            else:
                left.append(-1)
            s1.append(i)
                
        s2 = []
        right = []
        for i in range(len(heights) - 1, -1, -1):
            while s2 and heights[i] <= heights[s2[-1]]:
                s2.pop()
            if s2:
                right.insert(0, s2[-1])
            else:
                right.insert(0, len(heights))
            s2.append(i)
            
        max_area = 0
        for i in range(len(heights)):
            cur_area = heights[i] * (right[i] - left[i] - 1)
            max_area = max(cur_area, max_area)
        return max_area
