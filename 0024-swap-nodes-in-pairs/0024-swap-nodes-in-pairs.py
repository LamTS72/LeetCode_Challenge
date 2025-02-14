# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr = head
        dumpyNode = ListNode()
        prev = dumpyNode
        while curr and curr.next is not None:
            # node3 = node2.next
            node2 = curr.next
            node3 = node2.next
            
            # swap
            node2.next = curr
            curr.next = node3
            prev.next = node2

            prev = curr
            curr = node3

        self.show(dumpyNode.next)
        return dumpyNode.next
    
    def show(self, node):
        curr = node
        lists = []
        while curr:
            lists.append(curr.val)
            curr = curr.next
        print(lists)
        
