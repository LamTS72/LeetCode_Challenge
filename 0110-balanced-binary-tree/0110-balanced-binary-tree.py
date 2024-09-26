# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            lheight = height(root.left)
            rheight = height(root.right)
            return 1 + max(lheight, rheight)
        
        if root is None:
            return True
        
        LH = height(root.left)
        RH = height(root.right)
        balance = LH - RH
        if balance > 1 or balance < -1:
            return False
        if self.isBalanced(root.left) == False or self.isBalanced(root.right) == False:
            return False
        return True