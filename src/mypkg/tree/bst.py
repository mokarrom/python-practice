"""BST Algorithm."""
from typing import List, Optional
from mypkg.tree.tree_node import TreeNode


class BST:
    """Binary Search Tree."""

    @staticmethod
    def bst_from_sorted_array(nums: List[int]) -> Optional[TreeNode]:
        """Construct a height-balanced binary search tree from a sorted array."""

        def balanced_bst(low, high) -> Optional[TreeNode]:
            if low > high:
                return None
            elif low == high:
                return TreeNode(nums[low])

            mid = (low + high) // 2
            root = TreeNode(nums[mid])
            root.left = balanced_bst(low, mid - 1)
            root.right = balanced_bst(mid + 1, high)

            return root

        if not nums:
            return None
        else:
            return balanced_bst(0, len(nums) - 1)
