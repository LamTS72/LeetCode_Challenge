# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        i = 0
        tail_a = None
        tail_b = None
        curr = list1
        while curr:
            if i == a - 1:
                tail_a = curr
            if i == b + 1:
                tail_b = curr
            curr = curr.next
            i += 1
        
        tail_a.next = list2
        curr2 = list2
        while curr2.next is not None:
            curr2 = curr2.next
        curr2.next = tail_b
        return list1
        