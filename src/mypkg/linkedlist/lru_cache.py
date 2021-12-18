"""LRU chache."""
from typing import Dict, Optional


class Node:
    """Doubly linked list node."""

    def __init__(self, key: int, data: int, next_node=None, prev_node=None):
        self.key = key
        self.data = data
        self.next = next_node
        self.prev = prev_node


class LRUCache:
    """Least Recently Used (LRU) cache."""

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache: Dict[int, Node] = dict()
        self._head: Optional[Node] = None  # most recently accessed node
        self._tail: Optional[Node] = None  # least recently accessed node

    def _inset_first(self, node: Node) -> None:
        """Insert the given node at the beginning of the list."""
        if self._head is None:
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def _delete(self, node: Node):
        """Delete the given node."""
        prev_node = node.prev
        next_node = node.next

        if prev_node is None and next_node is None:  # deleting the only node
            self._head = self._tail = None
        elif prev_node is None:  # deleting the first node
            next_node.prev = None
            self._head = next_node
        elif next_node is None:  # deleting the last node
            prev_node.next = None
            self._tail = prev_node
        else:  # deleting a middle node
            prev_node.next = next_node
            next_node.prev = prev_node

    def get(self, key: int) -> int:
        """Return the value of the key if the key exists, otherwise return -1."""
        value = -1
        if key in self._cache:
            cur_node = self._cache[key]
            self._delete(cur_node)
            cur_node.prev = None
            cur_node.next = None
            self._inset_first(cur_node)
            value = cur_node.data

        return value

    def put(self, key: int, value: int) -> None:
        """Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.

        If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        """
        if key in self._cache:
            cur_node = self._cache[key]
            self._delete(cur_node)
            cur_node.data = value
            cur_node.prev = None
            cur_node.next = None
            self._inset_first(cur_node)
        else:
            if len(self._cache) == self._capacity:
                assert isinstance(self._tail, Node)
                del self._cache[self._tail.key]
                self._delete(self._tail)

            new_node = Node(key, value)
            self._inset_first(new_node)
            self._cache[key] = new_node
