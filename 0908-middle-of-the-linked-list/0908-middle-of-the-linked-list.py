# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        plist = []
        curr = head
        while curr:
            plist.append(curr.val)
            curr = curr.next
        n = len(plist) // 2
        pivot = head
        while n > 0:
            pivot = pivot.next
            n -= 1
        return pivot

        