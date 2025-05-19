# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def countnodes(node):
            if not node:
                return 0
            return 1 + countnodes(node.left) + countnodes(node.right)

        return countnodes(root)
