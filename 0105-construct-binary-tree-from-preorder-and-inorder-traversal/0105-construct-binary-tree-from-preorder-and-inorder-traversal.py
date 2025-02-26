# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return []
        
        return self.build(preorder, inorder)
    
    def build(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])

            root.left = self.build(preorder, inorder[:idx])
            root.right = self.build(preorder, inorder[idx+1:])
            return root