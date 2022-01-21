"""BST Algorithm."""
from sys import maxsize
from typing import List, Optional
from collections import deque
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

    def delete(self, value: int):
        """Delete the node from BST corresponding to the given value."""
        return self._find_and_delete(self._root, value)

    def _find_and_delete(self, root: Optional[TreeNode], value: int):
        if root is None:
            return root

        if value < root.data:
            root.left = self._find_and_delete(root.left, value)
        elif value > root.data:
            root.right = self._find_and_delete(root.right, value)
        else:  # Node to be deleted has found!
            # Case-1: Node to be removed has no children.
            if root.left is None and root.right is None:
                root = None
            # Case-2: Node to be removed has exactly one child
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            # Case-3: Node to be removed has both left and right child
            else:
                right_min_node = self._find_minimum_node(root.right)
                root.data = right_min_node.data
                root.right = self._find_and_delete(root.right, right_min_node.data)

        return root

    def contains(self, value: int) -> bool:
        """Check whether the tree contains a specific node or not."""
        return self._contains(self._root, value)

    def _contains(self, root: TreeNode, value: int) -> bool:
        if root is None:
            return False
        if value == root.data:
            return True

        return self._contains(root.left, value) if value < root.data else self._contains(root.right, value)

    def find(self, value: int) -> TreeNode:
        """Return the node from the BST that correspond to the given value."""
        return self._find(self._root, value)

    def _find(self, cur_node: TreeNode, value: int) -> Optional[TreeNode]:
        """Time Complexity O(h)."""
        if cur_node is None or value == cur_node.data:
            return cur_node
        elif value < cur_node.data:
            return self._find(cur_node.left, value)
        else:
            return self._find(cur_node.right, value)

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

    def _find_minimum_node(self, root: TreeNode) -> TreeNode:
        """Return the minimum node, i.e., left most node of BST."""
        if root.left is None:
            return root
        else:
            return self._find_minimum_node(root.left)

    def find_minimum_value(self) -> int:
        """Return the left most node's value. The node whose left is None is the node with minimum value."""
        if self._root is None:
            raise ValueError("Tree is empty!")

        cur_node = self._root
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node.data  # type: ignore

    def find_maximum_value(self) -> int:
        """Return the right most node's value. The node whose right is None is the node with maximum value."""
        if self._root is None:
            raise ValueError("Tree is empty!")

        cur_node = self._root
        while cur_node.right:
            cur_node = cur_node.right
        return cur_node.data  # type: ignore

    def level_order_traverse(self) -> List[int]:
        """Traverse the nodes in BST, as Breadth first order, aka, level-order traversal."""
        values = []
        queue = deque([self._root] if self._root else [])

        while queue:
            cur_node = queue.popleft()
            values.append(cur_node.data)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        return values

    def pre_order_traverse(self) -> List[int]:
        """Traverse the nodes in BST, as Depth first pre-order, i.e., root -> left -> right."""

        def _pre_order(root: TreeNode):
            if root:
                values.append(root.data)
                _pre_order(root.left)
                _pre_order(root.right)

        values: List[int] = []
        _pre_order(self._root)
        return values

    def in_order_traverse(self) -> List[int]:
        """Traverse the nodes in BST, as Depth first in-order, i.e., left -> root -> right."""
        return self._in_order(self._root)

    def _in_order(self, root: TreeNode, values: List[int] = None) -> List[int]:
        if values is None:
            values = list()
        if root is None:
            return values

        self._in_order(root.left, values)
        values.append(root.data)
        self._in_order(root.right, values)

        return values

    def post_order_traverse(self) -> List[int]:
        """Traverse the nodes in BST, as Depth first post-order, i.e., left -> right -> root."""
        return self._post_order(self._root)

    def _post_order(self, root: TreeNode) -> List[int]:
        return self._post_order(root.left) + self._post_order(root.right) + [root.data] if root else []

    def is_valid_bst1(self) -> bool:
        """Return True if the given binary tree is a BST, otherwise False."""
        return self._is_valid1(self._root, -maxsize, maxsize)

    def _is_valid1(self, root: TreeNode, low: int, high: int) -> bool:
        if root is None:
            return True
        if root.data < low or root.data > high:
            return False

        return self._is_valid1(root.left, low, root.data) and self._is_valid1(root.right, root.data, high)

    def is_valid_bst2(self) -> bool:
        """Check whether a binary tree is binary search tree or not.

        Traverse the tree in-order fashion and check every node is greater than or equal to the previous node.
        """

        def _is_valid2(curr_node: Optional[TreeNode], prev_node: Optional[TreeNode]) -> bool:
            if curr_node is None:
                return True
            if not _is_valid2(curr_node.left, prev_node):
                return False
            if prev_node and curr_node.data < prev_node.data:
                return False
            prev_node = curr_node
            if not _is_valid2(curr_node.right, prev_node):
                return False

            return True

        return _is_valid2(self._root, None)

    def is_complete(self):
        """Check whether the binary tree is complete or not.

        A binary tree is complete if its every node has zero or exactly two children.
        """
        if self._root is None:
            return True
        return self._complete(self._root)

    def _complete(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True
        elif root.left and root.right:
            return self._complete(root.left) and self._complete(root.right)
        else:
            return False

    def find_inorder_successor(self, value: int) -> Optional[TreeNode]:
        """Return the in-order successor of a node associated with the given value in a BST."""
        curr_node = self._find(self._root, value)
        if curr_node is None:
            return None

        if curr_node.right:
            # Case 1: Node has right subtree.
            # Left most node, i.e., minimum node, in right subtree is the inorder successor of current node.
            return self._find_minimum_node(curr_node.right)
        else:
            # Case 2: No right subtree.
            # Go to the nearest ancestor for which given node would be in left subtree.
            successor = None
            ancestor = self._root
            assert isinstance(ancestor, TreeNode)
            while ancestor != curr_node:
                if curr_node.data < ancestor.data:
                    successor = ancestor  # so far this is the deepest node for which current node is in the left.
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor

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
