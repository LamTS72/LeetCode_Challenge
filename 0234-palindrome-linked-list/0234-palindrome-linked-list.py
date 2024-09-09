# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listA = []
        curr = head
        while curr != None:
            listA.append(curr.val)
            curr = curr.next
        return listA == listA[::-1]

        
        