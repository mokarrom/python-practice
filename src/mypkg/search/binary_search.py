"""Binary Search."""
import math
from typing import List, Any


class BinarySearch:
    """Binary Search - finding a value in a sorted sequence."""

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
            index of the target item if found, otherwise -1
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
    def find_first_index(items: List[Any], target: Any, low: int = 0, high=None) -> int:
        """Returns the index of first occurrence of target."""
        # if items[i] <= target ?  [True, True, ..., True, False, False, ..., False]
        if high is None:
            high = len(items) - 1
        if target < items[low] or target > items[high]:
            return -1

        while low < high:
            mid: int = low + (high - low) // 2
            if items[mid] >= target:  # [False, False, ..., False, True, True, ..., True]
                high = mid
            else:
                low = mid + 1
        return low if items[low] == target else -1

    @staticmethod
    def find_last_index(items: List[Any], target: Any, low: int = 0, high=None) -> int:
        """Returns the index of last occurrence of target."""
        if high is None:
            high = len(items) - 1
        if target < items[low] or target > items[high]:
            return -1

        while low < high:
            mid: int = low + (high - low + 1) // 2
            if items[mid] <= target:  # [True, True, ..., True, False, False, ..., False]
                low = mid
            else:
                high = mid - 1
        return low if items[low] == target else -1

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


class BinarySearchAnswer:
    """Binary Search - discrete or abstract."""

    @staticmethod
    def find_bs_discrete(items: List[Any], target: Any) -> int:
        """Find the index of the first element in A equal to or greater than the target value."""
        # Is A[x] greater than or equal to the target value? [False, False, ..., False, True, True, ..., True].
        def predicate(idx: int) -> bool:
            """Check if the candidate solution is legal according to the definition of the problem."""
            return bool(items[idx] >= target)

        if target < items[0]:
            return -1  # p(x) is false for all x in S!

        low, high = 0, len(items) - 1
        while low < high:
            mid = low + (high - low) // 2
            if predicate(mid):
                high = mid  # discard all values greater than mid.
            else:
                low = mid + 1  # discard all values less than or equal mid.

        return low if predicate(low) else -1

    @staticmethod
    def sqrt_bs(n: float) -> float:
        """Find the sqrt of n using binary search."""
        low, high = 1.0, n
        while not math.isclose(low, high, abs_tol=0.001):
            mid: float = (low + high) / 2.0
            if mid * mid >= n:
                high = mid
            else:
                low = mid

        return low

    @staticmethod
    def get_most_work(folder: List[int], num_workers: int) -> int:
        """Given a list of folder and number of workers, return the maximum number of files each worker need to look."""
        # Each worker gets a sequential series of files.
        # Ref: https://community.topcoder.com/stat?c=problem_statement&pm=1901&rd=4650
        def can_finish(max_work_load: int) -> bool:
            worker_count = 1
            cur_load = 0
            for files in folder:
                cur_load += files
                if cur_load > max_work_load:
                    cur_load = files
                    worker_count += 1
            return worker_count <= num_workers

        low, high = max(folder), sum(folder)
        while low < high:
            mid = low + (high - low) // 2
            if can_finish(mid):
                high = mid
            else:
                low = mid + 1
        return low
