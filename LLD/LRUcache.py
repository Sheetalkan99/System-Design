# LRU Cache (Python) — O(1) get/put using HashMap + Doubly Linked List

class Node:
    """Doubly linked list node for (key, value)."""
    __slots__ = ("key", "value", "prev", "next")
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache with:
      - dict: key -> Node (O(1) lookup)
      - doubly linked list: head=MRU side, tail=LRU side
    """
    def __init__(self, capacity: int):
        assert capacity > 0, "Capacity must be positive"
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head/tail to simplify edge cases
        self.head = Node(0, 0)  # MRU side
        self.tail = Node(0, 0)  # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---------- Public API ----------
    def get(self, key: int) -> int:
        """Return value if present; otherwise -1. Marks as most recently used."""
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert/update key with value. If capacity exceeded, evict LRU node.
        """
        node = self.cache.get(key)
        if node:
            node.value = value
            self._move_to_front(node)
            return

        # New key: create node, add to front, store in map
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

        if len(self.cache) > self.capacity:
            self._evict_lru()

    # ---------- Internal DLL helpers ----------
    def _add_to_front(self, node: Node) -> None:
        """Insert node right after head (mark as MRU)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: Node) -> None:
        """Unlink node from the list."""
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _move_to_front(self, node: Node) -> None:
        """Make existing node the MRU."""
        self._remove(node)
        self._add_to_front(node)

    def _evict_lru(self) -> None:
        """Remove least-recently-used node (before tail) from list and map."""
        lru = self.tail.prev
        self._remove(lru)
        del self.cache[lru.key]


# ---------- Quick sanity test ----------
if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)             # {1=1}
    lru.put(2, 2)             # {1=1, 2=2}
    print(lru.get(1))  # 1    # {2=2, 1=1}  (1 becomes MRU)
    lru.put(3, 3)             # evict 2 -> {1=1, 3=3}
    print(lru.get(2))  # -1
    lru.put(4, 4)             # evict 1 -> {3=3, 4=4}
    print(lru.get(1))  # -1
    print(lru.get(3))  # 3
    print(lru.get(4))  # 4