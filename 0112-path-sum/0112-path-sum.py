# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node , cursum):
            if not node:
                return False

            cursum += node.val
            if not node.left and not node.right:
                return cursum == targetSum

            return (dfs(node.left, cursum) or dfs(node.right, cursum)    )
        return dfs(root,0)    