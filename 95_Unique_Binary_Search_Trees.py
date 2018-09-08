# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        if n == 0:
            return res
        root = TreeNode(1)
        res.append(root)
        for i in range(2, n + 1):
            temp = []
            for i in len(res):
                new = TreeNode(i)

                
            
        