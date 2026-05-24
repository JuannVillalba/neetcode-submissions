class Node:
    def __init__(self, key, value):
        self.key = key
        self.value =value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        #sentinels
        self.left = Node(0,0)
        self.right = Node(0,0)
        #p0inters
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self , node): #A-[B]-C
        prevn , nxtn = node.prev , node.next # A, C
        prevn.next = nxtn
        nxtn.prev = prevn

    def insert(self , node): # A-C [B]
        prevn , nxtn = self.right.prev , self.right # C-B-Sentinel
        prevn.next = node
        nxtn.prev = node
        node.prev = prevn
        node.next = nxtn

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value) # Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
