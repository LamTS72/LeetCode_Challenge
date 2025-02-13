# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        tmp = self.reverseList(head)
        self.show(tmp)
        if n == 1:
            tmp = tmp.next
            return self.reverseList(tmp)

        curr = tmp
        prev = None
        while n > 1:
            n -= 1
            prev = curr
            curr = curr.next
        if curr.next:
            prev.next = curr.next
        else:
            prev.next = None

        return self.reverseList(tmp)


    
    def reverseList(self, node):
        curr = node
        prev = None
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        
        return prev

    def show(self, node):
        curr = node
        lists = []
        while curr:
            lists.append(curr.val)
            curr = curr.next
        print(lists)