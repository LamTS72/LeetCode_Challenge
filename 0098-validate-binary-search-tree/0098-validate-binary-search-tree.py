# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def utilsBST(root, min_v, max_v):
            if root is None:
                return True
            if root.val < min_v or root.val > max_v:
                return False
            return utilsBST(root.left, min_v, root.val - 1) and utilsBST(root.right, root.val + 1, max_v)
        
        return utilsBST(root, float("-inf"), float("inf"))