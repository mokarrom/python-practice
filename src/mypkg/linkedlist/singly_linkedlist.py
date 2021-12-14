"""Singly LinkedList."""
from typing import Optional


class Node:
    """Node class."""

    def __init__(self, data: int, next_node=None):
        self.data: int = data
        self.next: Optional[Node] = next_node


class SLinkedList:
    """Singly Linked List."""

    def __init__(self):
        self._head: Optional[Node] = None
        self._num_of_nodes: int = 0

    def insert_first(self, data: int):
        """Insert an item at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node

        self._num_of_nodes += 1

    def insert_last(self, data: int):
        """Insert an item at the end of the list."""
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            cur_node = self._head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node

        self._num_of_nodes += 1

    def insert_at(self, index: int, data: int):
        """Insert an item in a particular position of the list. Index starts from zero.

        If index is greater than the size, then the item will added at the end of list.
        """
        if index < 0:
            raise ValueError("Index must be greater than 0")
        elif index == 0:
            self.insert_first(data)
            return

        cur_idx = 0
        cur_node = self._head
        assert isinstance(cur_node, Node)
        while cur_node.next and cur_idx < index - 1:
            cur_node = cur_node.next
            cur_idx += 1

        new_node = Node(data)
        if cur_node.next is None:
            cur_node.next = new_node
        else:
            cur_node.next, new_node.next = new_node, cur_node.next

        self._num_of_nodes += 1

    def delete(self, value: int):
        """Delete the given node."""
        if self._head is None:
            return

        if self._head.data == value:  # delete the very fist node.
            self._head = self._head.next
            self._num_of_nodes -= 1
            return

        cur_node = self._head
        while cur_node.next and cur_node.next.data != value:
            cur_node = cur_node.next

        if cur_node.next:
            cur_node.next = cur_node.next.next
            self._num_of_nodes -= 1

    def contain(self, value: int) -> bool:
        """Check whether the given value exist or not in the list."""
        if self._head is None:
            return False

        cur_node = self._head
        while cur_node:
            if cur_node.data == value:
                return True
            cur_node = cur_node.next  # type: ignore

        return False

    def size(self):
        """Return the total number of nodes in this list."""
        return self._num_of_nodes

    def get_nodes(self):
        """Return all the nodes orderly."""
        nodes = []
        if self._head:
            cur_node = self._head
            nodes.append(cur_node.data)
            while cur_node.next:
                cur_node = cur_node.next
                nodes.append(cur_node.data)

        return nodes
