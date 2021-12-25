"""A class that represent a node in binary tree."""
from typing import Optional


class TreeNode:
    """Binary Tree Node."""

    def __init__(self, val: int, left=None, right=None):
        self.data: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right
