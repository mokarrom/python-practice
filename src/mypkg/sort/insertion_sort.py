"""Insertion sort."""

from typing import List, Any


class InsertionSort:
    """Insertion sort Implementation."""

    @staticmethod
    def sort(items: List[Any]) -> None:
        """Sort the list in-place."""
        for i in range(1, len(items)):
            j = i - 1
            key = items[i]
            while j >= 0 and items[j] > key:
                items[j + 1] = items[j]
                j -= 1
            items[j + 1] = key
