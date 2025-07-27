"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        if not root.children:
            return 1

        max_depth = 0

        for child in root.children:
            child_depth = self.maxDepth(child)
            max_depth = max( max_depth, child_depth)
            

        return 1 + max_depth     