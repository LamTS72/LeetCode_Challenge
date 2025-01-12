# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_height(root):
            if root is None:
                return 0
            left_h = get_height(root.left)
            right_h = get_height(root.right)
            self.diameter = max(self.diameter, left_h + right_h)
            return 1 + max(left_h, right_h)
        
        get_height(root)
        return self.diameter