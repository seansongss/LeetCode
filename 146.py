class LRUCache(object):
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

        def to_head(obj):
            

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.head

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if not self.cache:
            self.cache[key] = self.Node(key, value)
            self.head = self.cache[key]
            self.tail = self.cache[key]
        
        if self.cache.__len__() == self.capacity:
            self.cache.pop([self.tail.key])
            self.tail = self.tail.prev
            self.tail.next = None

        if key in self.cache:
            self.cache[key].value = value
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev
            self.cache[key].prev = None
            self.cache[key].next = self.head
            self.head = self.cache[key]
        else:
            self.cache[key] = self.Node(key, value)
            self.cache[key].next = self.head
            self.head = self.cache[key]



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
print(obj.get(6))
print(obj.get(8))
obj.put(12, 1)
print(obj.get(2))
obj.put(15, 11)
obj.put(5, 2)
obj.put(1, 15)
obj.put(4, 2)
print(obj.get(4))
obj.put(15, 15)