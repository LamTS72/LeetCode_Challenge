# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        dumpyNode = ListNode()
        curr = dumpyNode
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1 is None:
            curr.next = list2
        
        if list2 is None:
            curr.next = list1

        self.show(dumpyNode.next)
        return dumpyNode.next

    def show(self, node):
        while node:
            print(node.val)
            print("|")
            node = node.next
        print("Null")