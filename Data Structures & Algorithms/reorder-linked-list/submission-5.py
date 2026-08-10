# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        temp = slow.next
        slow.next = None
        prev = None

        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        
        first = head
        second = prev

        while second:
            temp1 , temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first , second = temp1 , temp2
            



