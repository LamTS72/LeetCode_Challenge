# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list_a = []
        curr = head
        flag_merge = False
        tmp = 0
        while curr is not None:
            if flag_merge == True:
                tmp += curr.val
            if curr.val == 0 and flag_merge == False:
                flag_merge = True
            if curr.val == 0 and flag_merge == True:
                list_a.append(tmp)
                tmp = 0
            curr = curr.next

        dummy = rhead = ListNode(0)
        for i in range(len(list_a)):
            rhead.next = ListNode(list_a[i])
            rhead = rhead.next
        dummy = dummy.next
        return dummy.next
            



        