# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        res = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            list_level = []
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                list_level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)

            res.append(list_level)
        return res