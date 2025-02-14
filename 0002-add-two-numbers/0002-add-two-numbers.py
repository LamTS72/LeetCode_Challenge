# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        n1 = self.convert(l1)
        n2 = self.convert(l2)

        n = n1 + n2
        return self.split(n)


    def reverse(self, node):
        curr = node
        prev = None
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        return prev

    def convert(self, node):
        curr = node
        num = 0
        while curr:
            num = num * 10 + curr.val
            curr = curr.next
        return num

    def split(self, n):
        s = str(n)
        dumpyNode = ListNode()
        curr = dumpyNode
        for i in range(len(s) - 1, -1, -1):
            curr.next = ListNode(int(s[i]))
            curr = curr.next
        return dumpyNode.next
