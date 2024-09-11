# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_height(root):
            if root is None: return 0
            return 1 + max(get_height(root.left), get_height(root.right))
        
        if root is None:
            return True
        balance = get_height(root.left) - get_height(root.right)
        if balance > 1 or balance < -1: 
            return False
        if self.isBalanced(root.left) == False or self.isBalanced(root.right) == False:
            return False
        return True
        