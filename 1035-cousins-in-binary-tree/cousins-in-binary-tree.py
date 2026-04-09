# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.xp = self.yp = None
        self.xd = self.yd = -1

        def dfs(node, parent, depth):
            if not node:
                return
            
            if node.val == x:
                self.xp = parent
                self.xd = depth
            if node.val == y:
                self.yp = parent
                self.yd = depth

            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)

        return self.xd == self.yd and self.xp != self.yp