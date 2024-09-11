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
        if head is None or head.next is None:
            return False
        hashtable = {}
        while head is not None:
            if head.next not in hashtable:
                hashtable[head.next] = 1
            else:
                return True
            head = head.next
        return False