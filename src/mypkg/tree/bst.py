"""BST Algorithm."""
from typing import List, Optional
from mypkg.tree.tree_node import TreeNode


class BST:
    """Binary Search Tree."""

    def __init__(self):
        self._root: Optional[TreeNode] = None

    def insert(self, value: int):
        """Insert a value into the BST."""
        if self._root is None:
            self._root = TreeNode(value)
        else:
            self._insert_recur(self._root, value)

    def _insert_recur(self, cur_node: TreeNode, value: int):
        if value < cur_node.data:
            if cur_node.left is None:
                cur_node.left = TreeNode(value)
            else:
                self._insert_recur(cur_node.left, value)
        else:
            if cur_node.right is None:
                cur_node.right = TreeNode(value)
            else:
                self._insert_recur(cur_node.right, value)

    def contains(self, value: int) -> bool:
        """Check whether the tree contains a specific node or not."""
        return self._contains(self._root, value)

    def _contains(self, root: TreeNode, value: int) -> bool:
        if root is None:
            return False
        if value == root.data:
            return True

        return self._contains(root.left, value) if value < root.data else self._contains(root.right, value)

    def get_height(self) -> int:
        """Return the height of a binary tree.

        Height is the number of edges between the tree's root and its furthest leaf.
        """
        return self._get_height(self._root)

    def _get_height(self, root: TreeNode) -> int:
        if root is None:
            return -1  # we have already counted one null child. therefore deduct 1;
        return 1 + max(self._get_height(root.left), self._get_height(root.right))

    def max_depth(self) -> int:
        """Number of nodes along the longest path from the root node down to the farthest leaf node."""
        return self._max_depth(self._root)

    def _max_depth(self, root) -> int:
        if root is None:
            return 0

        return 1 + max(self._max_depth(root.left), self._max_depth(root.right))

    def min_depth(self) -> int:
        """Number of nodes along the shortest path from the root node down to the farthest leaf node."""
        return self._min_depth(self._root)

    def _min_depth(self, root) -> int:
        if root is None:
            return 0

        min_left = self._min_depth(root.left)
        min_right = self._min_depth(root.right)

        if min_left == 0 or min_right == 0:  # skewed tree; min(0, *) = 0
            return 1 + max(min_left, min_right)

        return 1 + min(min_left, min_right)

    def display(self) -> List[int]:
        """Return a serialized format of a binary tree using level order traversal.

        Here, None signifies a path terminator where no node exists below.
        """
        values = []
        cur_level = [self._root]

        while any(cur_level):
            next_level = []
            for node in cur_level:
                if node:
                    values.append(node.data)
                    next_level.append(node.left if node.left else None)
                    next_level.append(node.right if node.right else None)
                else:
                    values.append(None)
            cur_level = next_level

        return values

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
