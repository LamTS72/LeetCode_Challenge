# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def height(root):

            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
        
        self.diameter = 0
        height(root)
        return self.diameter
