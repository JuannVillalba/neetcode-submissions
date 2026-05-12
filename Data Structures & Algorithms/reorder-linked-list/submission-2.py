# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None
        slow.next = None

        while second is not None:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first , second = head , prev
        while second is not None:       
            temp1 , temp2 = first.next , second.next # 2, 4 | 3 , None
            first.next = second    # 1->5 |   1->5->2->4  
            second.next = temp1     # 1->5->2 | 1->5->2->4->3 
            first , second = temp1 , temp2  # 2,4 | 3 , None 
        


        

