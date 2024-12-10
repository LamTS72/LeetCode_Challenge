# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Solution: loop
        # Requirement: O(n)
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        dummyNode = curr = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr.next = ListNode(val=list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(val=list2.val)
                list2 = list2.next
            curr = curr.next
        
        if list1 is None:
            curr.next = list2
        if list2 is None:
            curr.next = list1
        return dummyNode.next
