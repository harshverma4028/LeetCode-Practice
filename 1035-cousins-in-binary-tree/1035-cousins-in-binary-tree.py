# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        queue = deque([(root, None)]) 

        while queue:
            size = len(queue)
            foundX = foundY = None

            for _ in range(size):
                node, parent = queue.popleft()

                if node.val == x:
                    foundX = parent
                if node.val == y:
                    foundY = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            # check after each level
            if foundX and foundY:
                return foundX != foundY   # same level but different parent
            if foundX or foundY:
                return False

        return False
