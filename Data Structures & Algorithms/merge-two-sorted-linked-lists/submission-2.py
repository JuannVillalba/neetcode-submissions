# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = list1
        l2 = list2
        prev = None
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                prev = l1
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                prev = l2
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        
        if l1 == None:
                cur.next = l2
        elif l2 == None:
                cur.next = l1

        return dummy.next


