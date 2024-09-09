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
        idx = 0
        curr1 = list1
        tail_a = None
        tail_b = None
        while curr1 is not None:
            if idx == a - 1:
                tail_a = curr1
            if idx == b + 1:
                tail_b = curr1

            curr1 = curr1.next
            idx += 1
        #print(tail_a.val,tail_b.val)
        tail_a.next = list2
        curr2 = list2
        while curr2 is not None and curr2.next is not None:
            curr2 = curr2.next
        curr2.next = tail_b

        return list1


