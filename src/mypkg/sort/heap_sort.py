"""Heap sort."""
from typing import List, Any


class HeapSort:
    """Heap sort Implementation."""

    @staticmethod
    def sort(items: List[Any]) -> None:
        """Sorting an unordered array using Heap sort algorithm."""
        if not items or len(items) < 2:
            return
        MaxHeap.build_heap(items)
        for i in range(len(items) - 1, 0, -1):
            swap(items, 0, i)
            MaxHeap.heapify_down(items, 0, i)


class MaxHeap:
    """Max Heap implementation."""

    @staticmethod
    def heapify_up(heap: List[Any], child_idx: int) -> None:
        """Heapify up from the given child to the root.

        Compare the given child with its parent. If they are out of order swap, and repeat, else stop.
        """
        while has_parent(child_idx) and get_parent(heap, child_idx) < heap[child_idx]:
            parent_idx = get_parent_idx(child_idx)
            swap(heap, parent_idx, child_idx)
            child_idx = parent_idx

    @staticmethod
    def heapify_down(heap: List[Any], parent_idx: int, size: int) -> None:
        """Heapify the subtree rooted at given parent index.

        Compare the given node with its largest child.
        If the parent is smaller than its largest child, then swap, and repeat, else break.
        """
        while has_left_child(size, parent_idx):
            max_child_idx = get_left_child_idx(parent_idx)
            if has_right_child(size, parent_idx) and get_right_child(heap, parent_idx) > get_left_child(
                heap, parent_idx
            ):
                max_child_idx = get_right_child_idx(parent_idx)
            if heap[parent_idx] >= heap[max_child_idx]:
                break
            swap(heap, parent_idx, max_child_idx)
            parent_idx = max_child_idx

    @staticmethod
    def build_heap(items: List[Any]):
        """Builds a max heap (in-place) from an unordered array/list.

        Perform reverse level order traversal from last non-leaf node and heapify each node.
        """
        size = len(items)
        start_idx = len(items) // 2 - 1  # Index of last non-leaf node

        for i in range(start_idx, -1, -1):
            MaxHeap.heapify_down(items, i, size)

    @staticmethod
    def pop(heap: List[Any]) -> Any:
        """Delete the heap's root and return."""
        if len(heap) == 0:
            raise ValueError("Heap is empty")

        last_item = heap.pop()
        if heap:
            root = heap[0]
            heap[0] = last_item
            MaxHeap.heapify_down(heap, 0, len(heap))
            return root

        return last_item

    @staticmethod
    def push(heap: List[Any], item: int):
        """Add an item into the heap."""
        heap.append(item)
        MaxHeap.heapify_up(heap, len(heap) - 1)


def get_parent_idx(child_idx: int) -> int:
    """Returns parent using (n - 1) / 2."""
    return (child_idx - 1) // 2


def get_left_child_idx(parent_idx: int) -> int:
    """Returns left child index using 2n + 1."""
    return 2 * parent_idx + 1


def get_right_child_idx(parent_idx: int) -> int:
    """Returns right child index using 2n + 2."""
    return 2 * parent_idx + 2


def has_parent(child_idx: int) -> bool:
    """Returns True if the node has parent otherwise False."""
    return get_parent_idx(child_idx) >= 0


def has_left_child(num_of_nodes: int, parent_idx: int) -> bool:
    """Returns True if the node has a left child otherwise False."""
    return get_left_child_idx(parent_idx) < num_of_nodes


def has_right_child(num_of_nodes: int, parent_idx: int) -> bool:
    """Returns True if the node has a right child otherwise False."""
    return get_right_child_idx(parent_idx) < num_of_nodes


def get_parent(items: List[Any], child_idx: int) -> Any:
    """Return the parent node of this child."""
    return items[get_parent_idx(child_idx)]


def get_left_child(items: List[Any], parent_idx: int) -> Any:
    """Return the left child of this node."""
    return items[get_left_child_idx(parent_idx)]


def get_right_child(items: List[Any], parent_idx: int) -> Any:
    """Return the right child of this node."""
    return items[get_right_child_idx(parent_idx)]


def swap(items: List[Any], idx1: int, idx2: int) -> None:
    """Swap elements in the given list."""
    items[idx1], items[idx2] = items[idx2], items[idx1]
