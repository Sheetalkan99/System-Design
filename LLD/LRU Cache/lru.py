from abc import ABC, abstractmethod

# ------------------------------
# Eviction Policy Interface
# ------------------------------
class EvictionPolicy(ABC):
    @abstractmethod
    def key_accessed(self, key):
        pass

    @abstractmethod
    def evict_key(self):
        pass

# ------------------------------
# Node Class (Doubly Linked List Node)
# ------------------------------
class Node:
    def __init__(self, key, value):
        self.key = key          # Cache key
        self.value = value      # Cache value
        self.prev = None        # Pointer to previous node
        self.next = None        # Pointer to next node

# ------------------------------
# LRU Eviction Policy (Least Recently Used)
# ------------------------------
class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.head = Node(None, None)     # Dummy head
        self.tail = Node(None, None)     # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}            # Maps key to node

    def _remove(self, node):
        # Detach node from the list
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert_at_front(self, node):
        # Insert node right after head (most recently used position)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def key_accessed(self, key):
        # Move the accessed node to the front (MRU)
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove(node)
            self._insert_at_front(node)

    def insert(self, key, value):
        if key in self.key_to_node:
            # Update existing node and move to front
            node = self.key_to_node[key]
            node.value = value
            self.key_accessed(key)
        else:
            # Create and insert new node
            node = Node(key, value)
            self.key_to_node[key] = node
            self._insert_at_front(node)

    def evict_key(self):
        # Evict least recently used (node before tail)
        if self.tail.prev == self.head:
            return None  # Nothing to evict
        node = self.tail.prev
        self._remove(node)
        del self.key_to_node[node.key]
        return node.key

    def get_node(self, key):
        return self.key_to_node.get(key, None)

# ------------------------------
# Cache Class (uses Eviction Policy)
# ------------------------------
class Cache:
    def __init__(self, capacity, policy: LRUEvictionPolicy):
        self.capacity = capacity
        self.policy = policy
        self.store = {}  # Stores key → value

    def get(self, key):
        if key not in self.store:
            return -1
        self.policy.key_accessed(key)
        return self.store[key]

    def put(self, key, value):
        if key in self.store:
            self.store[key] = value
            self.policy.key_accessed(key)
        else:
            if len(self.store) >= self.capacity:
                evicted_key = self.policy.evict_key()
                if evicted_key is not None:
                    del self.store[evicted_key]
            self.store[key] = value
            self.policy.insert(key, value)

# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":
    print("✅ Testing LRU Cache with Strategy Pattern")
    lru_policy = LRUEvictionPolicy()
    cache = Cache(capacity=2, policy=lru_policy)

    cache.put(1, 'A')      # Cache: {1:A}
    cache.put(2, 'B')      # Cache: {2:B, 1:A}
    print(cache.get(1))    # Output: 'A', Cache: {1:A, 2:B}
    cache.put(3, 'C')      # Evicts 2, Cache: {3:C, 1:A}
    print(cache.get(2))    # Output: -1 (evicted)
    print(cache.get(3))    # Output: 'C'
    print(cache.get(1))    # Output: 'A'
