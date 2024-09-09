# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        currA = l1
        listA = []
        while currA is not None:
            listA.append(currA.val)
            currA = currA.next
        
        currB = l2
        listB = []
        while currB is not None:
            listB.append(currB.val)
            currB = currB.next
        
        print(listA, listB)
        stringA = ""
        for i in range(len(listA)):
            stringA += str(listA.pop())
        
        stringB = ""
        for i in range(len(listB)):
            stringB += str(listB.pop())
        
        stringC = int(stringA) + int(stringB)
        stringC = str(stringC)[::-1]
        print(stringC)
        dummy = curr = ListNode(0)
        for i in stringC:
            curr.next = ListNode(int(i))
            curr = curr.next

        return dummy.next
        
        