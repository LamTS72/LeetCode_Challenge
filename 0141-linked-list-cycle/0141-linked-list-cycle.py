# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list_a = []
        curr = head
        while curr is not None:
            if curr in list_a:
                return True
            list_a.append(curr)
            curr = curr.next
        
        return False
        