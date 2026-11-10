class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        myMap = {None : None}

        cur = head

        while cur:
            copy = Node(cur.val)
            myMap[cur] = copy
            cur = cur.next
        
        cur = head 

        while cur:
            copy = myMap[cur]
            copy.next = myMap[cur.next]
            copy.random = myMap[cur.random]
            cur = cur.next
        return myMap[head] 