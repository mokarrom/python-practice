"""Doubly LinkedList."""
from typing import List, Optional


class DllNode:
    """Doubly linked list node."""

    def __init__(self, data: int, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DLinkedList:
    """Doubly linked list implementation."""

    def __init__(self):
        self._head: Optional[DllNode] = None
        self._tail: Optional[DllNode] = None
        self._num_of_nodes = 0

    def insert_first(self, data: int):
        """Insert an item at the beginning of the list."""
        new_node = DllNode(data)
        if self._head is None:  # list is empty
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._num_of_nodes += 1

    def insert_last(self, data: int):
        """Insert an item at the end of the list."""
        new_node = DllNode(data)
        if self._head is None or self._tail is None:  # list is empty
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        self._num_of_nodes += 1

    def size(self):
        """Return the total number of nodes in this list."""
        return self._num_of_nodes

    def delete(self, value: int):
        """Delete the given node."""
        cur_node = self._head
        while cur_node and cur_node.data != value:
            cur_node = cur_node.next

        if cur_node is None:
            return  # list is empty or item not found

        prev_node = cur_node.prev
        next_node = cur_node.next

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

        self._num_of_nodes -= 1

    def get_nodes(self, reverse=False) -> List[int]:
        """Get all nodes orderly."""
        nodes: List[int] = []
        if self._head is None or self._tail is None:
            return nodes

        if reverse:
            cur_node = self._tail
            while cur_node:
                nodes.append(cur_node.data)
                cur_node = cur_node.prev
        else:
            cur_node = self._head
            while cur_node:
                nodes.append(cur_node.data)
                cur_node = cur_node.next

        return nodes
