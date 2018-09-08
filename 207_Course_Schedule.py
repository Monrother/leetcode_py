from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inDegree = [0 for _ in range(numCourses)]
        edges = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            inDegree[edge[0]] += 1
            edges[edge[1]].append(edge[0])
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        while len(queue) != 0:
            cur = queue[0]
            queue.popleft()
            for course in edges[cur]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
        for i in range(numCourses):
            if inDegree[i] != 0:
                return False
        return True