# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        dumpyEven = ListNode()
        pivotE = dumpyEven
        dumpyOdd = ListNode()
        pivotO = dumpyOdd
        i = 1
        while curr:
            if i % 2 == 1:
                pivotO.next = ListNode(curr.val)
                pivotO = pivotO.next
            elif i % 2 == 0:
                pivotE.next = ListNode(curr.val)
                pivotE = pivotE.next
            curr = curr.next
            i += 1
        self.show(dumpyOdd.next)
        self.show(dumpyEven.next)

        if dumpyOdd.next is None:
            return dumpyEven.next
        if dumpyEven.next is None:
            return dumpyOdd.next
        pivotO.next = dumpyEven.next
        return dumpyOdd.next
    
    def show(self, node):
        curr = node
        lists = []
        while curr:
            lists.append(curr.val)
            curr = curr.next
        print(lists)
        