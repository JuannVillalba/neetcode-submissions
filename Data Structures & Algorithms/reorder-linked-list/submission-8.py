# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        l1 = head
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None
        prev = None
        
        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt
        
      
        # [2 -> 4 ] [8 -> 6]
        # prev = 8 , l1 = 2
        l2 = prev
        
        while l2:
            l1nxt = l1.next # 4
            l2nxt = l2.next # 6

            l1.next = l2
            l2.next = l1nxt

            l1 = l1nxt
            l2 = l2nxt
        
        
        