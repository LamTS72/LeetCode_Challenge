# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue =[root]
        res = []
        while len(queue) != 0:
            size_queue = len(queue) - 1
            for i in range(len(queue)):
                tmp = queue.pop(0)
                if i == size_queue:
                    res.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
        return res
