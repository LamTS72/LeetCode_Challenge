# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        temp = ListNode()
        temp = list1
        if list1.val > list2.val:
            temp = list2
            list2 = list2.next
        else:
            list1 = list1.next
        
        curr = temp
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next
        if list1 is None:
            curr.next = list2
        else:
            curr.next = list1
        
        return temp
        