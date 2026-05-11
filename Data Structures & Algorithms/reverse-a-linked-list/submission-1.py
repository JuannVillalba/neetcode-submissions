# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        #  Before    Null -> 1 -> 2 -> 3 -> Null  | 1 is head
        # After      Null <- 1 <- 2 <- 3 <- Null  | 3 is head
        
        
