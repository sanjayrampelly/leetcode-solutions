# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return root
            lr = self.invertTree(root.left)
            rs = self.invertTree(root.right)
            root.left = rs
            root.right = lr
            return root

        return dfs(root)
