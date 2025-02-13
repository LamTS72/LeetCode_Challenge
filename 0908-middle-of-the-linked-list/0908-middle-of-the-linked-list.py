# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        slow = fast = head
        while fast:
            fast = fast.next
            # slow = 1
            # fast = 2
            # check null
            if fast:
                slow = slow.next
                # slow = 2
                fast = fast.next
                # fast = 4
        return slow

