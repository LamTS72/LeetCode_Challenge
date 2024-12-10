# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        hashtable = {}
        curr = head
        while curr:
            if curr not in hashtable:
                hashtable[curr] = 1
            else:
                return True
            curr = curr.next
        return False