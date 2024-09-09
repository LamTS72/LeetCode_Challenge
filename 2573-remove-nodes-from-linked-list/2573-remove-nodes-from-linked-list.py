# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        prev = None
        while curr is not None:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        rehead = prev
        max_a = 0
        list_a = []
        while rehead is not None :
            if max_a > rehead.val:
                pass
            else:
                max_a = rehead.val
                list_a.append(max_a)
            rehead = rehead.next
        print("max ", list_a)
        dummy_h = dummy =ListNode(0)
        for i in range(len(list_a)):
            dummy.next = ListNode(list_a.pop())
            dummy = dummy.next
        return dummy_h.next
        
        