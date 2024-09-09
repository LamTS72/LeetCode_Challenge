# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None:
            return None
        if headB is None:
            return None
        
        currA = headA
        currB = headB
        list_a = set()
        while currA is not None:
            list_a.add(currA)
            currA= currA.next

        while currB is not None:
            if currB in list_a:
                return currB
            currB = currB.next
        return None
        