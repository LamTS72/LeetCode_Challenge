# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        curr = ListNode()
        res = curr
        while head != None:
            if head.val != val:
                curr.next = head
                curr = curr.next
            head = head.next
        curr.next = None
        return res.next

        