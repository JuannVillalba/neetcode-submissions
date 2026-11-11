# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:                  # [0,1,2,3]
            nxt = cur.next          # temmp memory of the next value of the original array
            cur.next = prev         # reversing 
            prev = cur              # updating the new prev value
            cur = nxt               # move to the next value of the original array
        
        return prev
