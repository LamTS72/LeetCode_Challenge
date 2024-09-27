# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None
        
        s1 = ""
        s2 = ""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        
        total = int(s1[::-1]) + int(s2[::-1])
        print(total)
        dumpy = curr = ListNode()
        for s in str(total)[::-1]:
            print(s, type(s))
            curr.next = ListNode(int(s))
            curr = curr.next
        return dumpy.next

