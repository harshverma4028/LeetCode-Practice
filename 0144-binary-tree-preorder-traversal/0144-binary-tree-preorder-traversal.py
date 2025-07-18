# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def recursive(node):
            if not node:
                return
            result.append(node.val)
            recursive(node.left)
            recursive(node.right)    
        recursive(root)
        return result