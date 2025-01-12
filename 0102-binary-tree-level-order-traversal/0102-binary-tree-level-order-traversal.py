# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Solution; level = breadth first search -> queue
        if root is None:
            return []
        res = []
        queue = [root]
        while len(queue) > 0:
            temp_level = []
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                temp_level.append(tmp.val)
                if tmp.left is not None:
                    queue.append(tmp.left)
                if tmp.right is not None:
                    queue.append(tmp.right)
            res.append(temp_level)
        return res



