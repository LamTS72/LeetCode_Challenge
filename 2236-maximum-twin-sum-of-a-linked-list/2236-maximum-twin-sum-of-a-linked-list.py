# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        list_a = []
        list_b = []
        curr = head
        while curr is not None:
            list_a.append(curr.val)
            curr = curr.next
        
        for i in range(len(list_a)/2):
            tmp = list_a[i] + list_a[len(list_a)-1-i]
            list_b.append(tmp)
        res = max(list_b)
        print(res)
        return res

            
        