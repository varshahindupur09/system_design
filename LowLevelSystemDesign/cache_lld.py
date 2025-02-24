# https://www.youtube.com/watch?v=iuqZvajTOyA
# doubly linked list - to know LRU/MRU values
# https://leetcode.com/problems/lru-cache/

class Node:
    """ Doubly Linked List """
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """ Initialize LRU with given capacity """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key -> Node pair mapping for O(1) access

        # dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # connect
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """ Removing node from Doubly Linked List """
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def _add_to_front(self, node: Node):
        """Add a node right after the head (most recently used position)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Insert or update a key-value pair in the cache."""
        if key in self.cache:
            self._remove(self.cache[key])
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

        if len(self.cache) > self.capacity:
            # Remove the least recently used (LRU) node (before the tail)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
