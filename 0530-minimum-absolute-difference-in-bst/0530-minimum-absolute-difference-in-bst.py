# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None
        self.min_dff = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)    
            
            if self.prev is not None:
                self.min_dff = min(self.min_dff, abs(node.val - self.prev))
            self.prev = node.val    

            inorder(node.right)

        inorder(root)
        return self.min_dff