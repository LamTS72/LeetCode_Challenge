# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        # find length 
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # find times rotate
        k = k % length
        if k == 0:
            return head
        break_point = length - k
        curr = head
        for _ in range(break_point - 1):
            curr = curr.next

        # end 1st list
        new_head = curr.next
        curr.next = None

        # merge
        tail.next = head
        return new_head
        


    # def show(self, node):
    #     curr = node
    #     lists = []
    #     while curr:
    #         lists.append(curr.val)
    #         curr = curr.next

    #     print(lists)