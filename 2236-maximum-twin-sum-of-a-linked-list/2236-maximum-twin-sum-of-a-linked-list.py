# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list_a = []
        list_b = []
        curr = head
        while curr:
            list_a.append(curr.val)
            curr = curr.next
        for i in range(0, (len(list_a)//2) - 1):
            sum_p = list_a[i] + list_a[len(list_a) - i - 1]
            list_b.append(sum_p)
            
        return max(list_b)