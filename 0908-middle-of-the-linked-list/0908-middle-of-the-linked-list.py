# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        list_a = []
        while curr is not None:
            list_a.append(curr.val)
            curr = curr.next
        
        n = len(list_a)/2
        print(n)
        idx = 0
        curr_res = head
        while curr_res is not None:
            idx += 1
            curr_res = curr_res.next
            if idx == n:
                print(idx)
                head = curr_res
                break
        return head
        