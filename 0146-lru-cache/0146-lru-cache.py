class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        ## head <-> tail
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # evit(thu hồi)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        #insert
        self.insert_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            # evict(thu hồi)
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
            node.val = value
            #insert
            self.insert_tail(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.insert_tail(node)
            if len(self.cache) > self.capacity:
                self.remove_head(self.head.next.key)

        

    def insert_tail(self, node):
        node.prev = self.tail.prev 
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def remove_head(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.next = None
        del node
        del self.cache[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)