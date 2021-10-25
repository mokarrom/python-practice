"""Binary Search."""
from typing import List, Any


class BinarySearch:
    """Binary Search Implementation."""

    @staticmethod
    def recur_search(items: List[Any], target: Any, low: int, high: int):
        """Search for an item in a sorted array.

        Args:
            items: list of items
            target: target item
            low: starting index
            high: ending index

        Returns
            index of the target item
        """
        if low > high:
            return -1

        mid = low + (high - low) // 2
        if items[mid] == target:
            return mid
        elif target < items[mid]:
            return BinarySearch.recur_search(items, target, low, mid - 1)
        else:
            return BinarySearch.recur_search(items, target, mid + 1, high)

    @staticmethod
    def iterative_search(items: List[Any], x: Any):
        """Search for an item in a sorted array.

        Args:
            items: list of items
            x: target item

        Returns:
            index of the target item
        """
        low = 0
        high = len(items) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if x < items[mid]:
                high = mid - 1
            elif x > items[mid]:
                low = mid + 1
            else:
                return mid

        return -1
