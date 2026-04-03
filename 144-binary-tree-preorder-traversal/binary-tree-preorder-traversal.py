# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        # if not root:
        #     return []
        # # print(root.val)
        # l.append(root.val)
        # l.extend(self.preorderTraversal(root.left))
        # l.extend(self.preorderTraversal(root.right))
        self.dfs(root,l)
        return l

    def dfs(self,root,res):
        if not root:
            return
        res.append(root.val)
        self.dfs(root.left,res)
        self.dfs(root.right,res)

        