# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def GDC(self, a, b):
        if b == 0:
            return a
        return self.GDC(b, a%b)
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr is not None and curr.next is not None:
            tmp = self.GDC(curr.val, curr.next.val)
            curr_next = curr.next
            curr.next = ListNode(tmp, curr_next)
            curr = curr_next

        return head
