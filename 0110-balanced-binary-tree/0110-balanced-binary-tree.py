# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        LH = self.get_height(root.left)
        RH = self.get_height(root.right)
        balanced = LH - RH
        if balanced > 1 or balanced < -1:
            return False
        if self.isBalanced(root.left) == False or self.isBalanced(root.right) == False:
            return False
        return True


    def get_height(self, root):
        if root is None:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return 1 + max(left, right)