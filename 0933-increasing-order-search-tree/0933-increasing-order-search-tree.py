# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inorder(node):
            nonlocal curr

            if not node:
                return 
            inorder(node.left)

            curr.right =  node
            node.left = None
            curr = node

            inorder(node.right)


        dummy = TreeNode(-1)
        curr = dummy
        inorder(root)
        return dummy.right

