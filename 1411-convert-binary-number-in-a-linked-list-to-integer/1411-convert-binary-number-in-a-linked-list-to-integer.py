# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        curr = head
        list_a = []
        while curr is not None:
            list_a.append(curr.val)
            curr = curr.next
        list_a.reverse()
        res = 0
        for i in range(len(list_a)):
            res += list_a[i] << i
        return res 

        