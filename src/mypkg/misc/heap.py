"""Heap Implementation in Python."""
from typing import List


class MinHeap:
    """Min Heap Implementation."""

    def __init__(self):
        self._heap: List[int] = list()
        self._size: int = 0

    @staticmethod
    def _get_parent_idx(child_idx: int) -> int:
        """Returns parent using (n - 1) / 2."""
        return (child_idx - 1) // 2

    @staticmethod
    def _get_left_child_idx(parent_idx: int) -> int:
        """Returns left child index using 2n + 1."""
        return 2 * parent_idx + 1

    @staticmethod
    def _get_right_child_idx(parent_idx: int) -> int:
        """Returns right child index using 2n + 2."""
        return 2 * parent_idx + 2

    @staticmethod
    def _has_parent(child_idx: int) -> bool:
        """Check if node has parent or not."""
        return MinHeap._get_parent_idx(child_idx) >= 0

    def _has_left_child(self, parent_idx: int) -> bool:
        """Check if this node has the left child."""
        return MinHeap._get_left_child_idx(parent_idx) < self._size

    def _has_right_child(self, parent_idx: int) -> bool:
        """Check if this node has the right child."""
        return MinHeap._get_right_child_idx(parent_idx) < self._size

    def _parent(self, child_idx: int) -> int:
        """Return the parent node of this child."""
        return self._heap[MinHeap._get_parent_idx(child_idx)]

    def _left_child(self, parent_idx: int) -> int:
        """Return the left child of this node."""
        return self._heap[MinHeap._get_left_child_idx(parent_idx)]

    def _right_child(self, parent_idx: int) -> int:
        """Return the right child of this node."""
        return self._heap[MinHeap._get_right_child_idx(parent_idx)]

    def _swap(self, idx1: int, idx2: int) -> None:
        self._heap[idx1], self._heap[idx2] = self._heap[idx2], self._heap[idx1]

    def _heapify_up(self) -> None:
        """Starting from the last node, compare every node with its parent.

        If the  current node is smaller than its parent then swap.
        """
        child_idx = self._size - 1
        while self._has_parent(child_idx) and self._parent(child_idx) > self._heap[child_idx]:
            parent_idx = self._get_parent_idx(child_idx)
            self._swap(parent_idx, child_idx)
            child_idx = parent_idx

    def _heapify_down(self) -> None:
        """Starting from the root, compare every node with its smallest child.

        If the parent is greater than its smallest child, then swap.
        """
        parent_idx = 0
        while self._has_left_child(parent_idx):
            min_child_idx = self._get_left_child_idx(parent_idx)
            if self._has_right_child(parent_idx) and self._right_child(parent_idx) < self._left_child(parent_idx):
                min_child_idx = self._get_right_child_idx(parent_idx)

            if self._heap[parent_idx] < self._heap[min_child_idx]:
                break

            self._swap(parent_idx, min_child_idx)
            parent_idx = min_child_idx

    def peek(self) -> int:
        """Return the smallest element, i.e., heap's root."""
        if self._size == 0:
            raise ValueError("Heap is empty")

        return self._heap[0]

    def pool(self) -> int:
        """Delete the heap's root and return."""
        if self._size == 0:
            raise ValueError("Heap is empty")

        root = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._size -= 1
        self._heapify_down()

        return root

    def add(self, item: int):
        """Add an item into the heap."""
        self._heap.append(item)
        self._size += 1

        self._heapify_up()

    def display_heap(self) -> List[int]:
        """Return the heap nodes in a list."""
        return self._heap[: self._size]
