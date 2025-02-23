# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.diameter = 0
        self.get_height_diameter(root)
        return self.diameter

    def get_height_diameter(self, root):
        if root is None:
            return 0
        left = self.get_height_diameter(root.left)
        right = self.get_height_diameter(root.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)