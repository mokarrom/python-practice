"""Quick sort."""
from typing import List, Any


class QuickSort:
    """Quick sort Implementation."""

    @staticmethod
    def sort(items: List[Any]) -> None:
        if not items or len(items) < 2:
            return
        QuickSort._quick_sort(items, 0, len(items) - 1)

    @staticmethod
    def _quick_sort(items: List[Any], low: int, high: int):
        if low < high:
            p_idx = QuickSort._partition(items, low, high)
            QuickSort._quick_sort(items, low, p_idx - 1)
            QuickSort._quick_sort(items, p_idx, high)

    @staticmethod
    def _partition(items: List[Any], low: int, high: int) -> int:
        piv_item = items[(low + high) // 2]
        while low <= high:
            while items[low] < piv_item:
                low += 1
            while items[high] > piv_item:
                high -= 1
            if low <= high:
                items[low], items[high] = items[high], items[low]
                low += 1
                high -= 1
        return low
