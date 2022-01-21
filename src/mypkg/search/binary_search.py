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
    def iterative_search(items: List[Any], target: Any) -> int:
        """Search for an item in a sorted array.

        Args:
            items: list of items
            target: target item

        Returns:
            index of the target item
        """
        low = 0
        high = len(items) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if target < items[mid]:
                high = mid - 1
            elif target > items[mid]:
                low = mid + 1
            else:
                return mid

        return -1

    @staticmethod
    def find_index(items: List[Any], target: Any, first_occurrence: bool = True, low: int = 0, high=None) -> int:
        """Returns the first or the last occurrence of a target in a sorted array."""
        if high is None:
            high = len(items) - 1

        while low <= high:
            mid: int = low + (high - low) // 2
            if target < items[mid]:
                high = mid - 1
            elif target > items[mid]:
                low = mid + 1
            else:  # target == items[mid]
                if first_occurrence:  # index of the first occurrence of target item
                    if mid == low or items[mid - 1] < target:
                        return mid
                    else:
                        high = mid - 1
                else:  # index of the last occurrence of target item
                    if mid == high or items[mid + 1] > target:
                        return mid
                    else:
                        low = mid + 1
        return -1

    @staticmethod
    def rotated_sorted_array_search(nums: List[int], target: int) -> int:
        """Search in Rotated Sorted Array. Ref: https://leetcode.com/problems/search-in-rotated-sorted-array/.

        Args:
            nums: possibly rotated sorted array of distinct integers
            target: target item

        Returns:
            index of the target if it is in nums, or -1 if it is not in nums.
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return low if target == nums[low] else -1

    @staticmethod
    def find_min_rotated_sorted_array(nums: List[int]) -> int:
        """Find Minimum in Rotated Sorted Array. Ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/.

        Args:
            nums: sorted rotated array of unique elements

        Returns:
            the minimum element of this array.
        """
        return BinarySearch._find_min(nums, 0, len(nums) - 1)

    @staticmethod
    def _find_min(nums: List[int], low: int, high: int) -> int:
        if low >= high:
            return nums[low]

        mid = (low + high) // 2

        if nums[mid] > nums[high]:
            return BinarySearch._find_min(nums, mid + 1, high)
        else:
            return BinarySearch._find_min(nums, low, mid)
