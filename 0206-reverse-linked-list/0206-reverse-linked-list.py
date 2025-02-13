# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        curr = head
        prev = None
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.show(prev)
        return prev

    def show(self, node):
        lists = []
        while node:
            lists.append(node.val)
            node = node.next
        print(lists)         