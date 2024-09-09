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
            list_a.append(curr)
            curr = curr.next
        
        n = len(list_a)/2
        print(n)
        idx = 0
        curr = head
        while curr is not None:
            idx += 1
            curr = curr.next
            if idx == n:
                print(idx)
                head = list_a[idx]
                break
        return head
        