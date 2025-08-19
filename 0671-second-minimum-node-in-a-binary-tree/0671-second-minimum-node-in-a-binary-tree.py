# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return -1

        min_val = root.val
        second_min = float('inf')

        def dfs(node):
            nonlocal second_min
            if node is None:
                return
            
            if min_val < node.val < second_min:
                second_min  = node.val
            elif node.val == min_val:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        if second_min == float('inf'):
            return -1
        else:
            return second_min
