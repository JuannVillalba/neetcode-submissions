class Node:
    def __init__(self, key , val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> Node

        #sentinels
        self.left = Node(0,0)
        self.right = Node(0,0)

        #pointers
        self.left.next = self.right
        self.right.prev = self.left

    
    def remove(self, node): #eg remove node B
        prevn = node.prev # A-[B]-C | store A node
        nxt = node.next # store C node
        prevn.next = nxt # A pointer to C node
        nxt.prev = prevn # C ponter to A node

    def insert(self, node): # insert B in A-C | A-C-B
        prevn = self.right.prev # store node que sentinel derecho points to the left = C node
        nxt = self.right # store sentinel derecho
        prevn.next = node # sset pointer de C al nuevo node = B 
        nxt.prev = node # set pointer del Sentinel derecho a B
        node.prev = prevn # set pointer  C <- B 
        node.next = nxt # set pointer de B -> Sentinel Right   

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
