# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total_tilt = 0

        def dfs(node):
            if node is None:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            tilt = abs(left_sum - right_sum)

            self.total_tilt += tilt

            return left_sum + right_sum + node.val    
        
        dfs(root)
        return self.total_tilt