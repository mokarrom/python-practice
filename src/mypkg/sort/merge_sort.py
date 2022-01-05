"""Merge sort."""
from typing import List, Any


class MergeSort:
    """Merge sort Implementation."""

    @staticmethod
    def sort(items: List[Any]) -> None:
        """Sorting an unordered array using Merge sort."""
        if not items or len(items) < 2:
            return
        MergeSort._merge_sort(items, 0, len(items) - 1)

    @staticmethod
    def _merge_sort(items: List[Any], low: int, high: int):
        if low < high:
            mid = (low + high) // 2
            MergeSort._merge_sort(items, low, mid)
            MergeSort._merge_sort(items, mid + 1, high)
            MergeSort._merge(items, low, mid, high)

    @staticmethod
    def _merge(items: List[Any], low: int, mid: int, high: int) -> None:
        i = low
        j = mid + 1
        sorted_items = []

        while i <= mid and j <= high:
            if items[i] < items[j]:
                sorted_items.append(items[i])
                i += 1
            else:
                sorted_items.append(items[j])
                j += 1

        if i <= mid:
            sorted_items.extend(items[i : mid + 1])
        if j <= high:
            sorted_items.extend(items[j : high + 1])

        # copy temp array to the original array
        items[low : high + 1] = sorted_items
