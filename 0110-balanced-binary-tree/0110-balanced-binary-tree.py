# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Solution: Recursive
        def get_height(root):
            if root is None:
                return 0
            left_h = get_height(root.left)
            right_h = get_height(root.right)
            return 1 + max(left_h, right_h)

        if root is None:
            return True
        LH = get_height(root.left)
        RH = get_height(root.right)
        balanced = LH - RH
        if balanced > 1 or balanced < -1:
            return False
        if self.isBalanced(root.left) == False or self.isBalanced(root.right) == False:
            return False
        return True
