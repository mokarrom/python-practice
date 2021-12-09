"""BST Algorithm."""
from typing import List, Optional
from mypkg.tree.tree_node import TreeNode


class BinarySearchTree:
    """Binary Search Tree."""

    def bst_from_sorted_array(self, nums: List[int]) -> Optional[TreeNode]:
        """Construct a height-balanced binary search tree from a sorted array."""
        if not nums:
            return None

        return self._balanced_bst(nums, 0, len(nums) - 1)

    def _balanced_bst(self, nums: List[int], beg: int, end: int) -> Optional[TreeNode]:
        if end < beg:
            return None

        mid = beg + (end - beg) // 2
        root = TreeNode(nums[mid])
        root.left = self._balanced_bst(nums, beg, mid - 1)
        root.right = self._balanced_bst(nums, mid + 1, end)

        return root
