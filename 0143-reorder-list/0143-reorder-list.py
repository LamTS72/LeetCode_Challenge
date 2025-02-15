# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        # Step 1: Find the middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half of the list
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            next_curr = curr.next
            curr.next = prev 
            prev = curr
            curr = next_curr

        # Step 3: Merge the two halves
        l1 = head
        l2 = prev

        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next, l2.next = l2, temp1
            l1, l2 = temp1, temp2
    #     self.show(head)
    # def show(self, node):
    #     curr = node
    #     lists = []
    #     while curr:
    #         lists.append(curr.val)
    #         curr = curr.next
    #     print(lists)
