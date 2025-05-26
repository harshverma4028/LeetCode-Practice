# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        paths = []
        def recursive(node,path):
            if not node:
                return
            if not node.left and not node.right:
                paths.append(path + str(node.val))
                return

            recursive(node.left, path + str(node.val) + "->")   
            recursive(node.right, path + str(node.val) + "->")      

        recursive(root,"")
        return paths