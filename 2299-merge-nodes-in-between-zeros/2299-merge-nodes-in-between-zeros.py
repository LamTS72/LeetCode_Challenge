# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = -1 
        curr = head
        dumpy = pivot = ListNode()
        sump = 0
        while curr:
            if curr.val == 0 and check == -1:
                check = 1
            elif curr.val == 0 and check == 1:
                pivot.next = ListNode(sump)
                pivot = pivot.next
                sump = 0
            if curr.val != 0:
                sump += curr.val
            curr = curr.next
        return dumpy.next