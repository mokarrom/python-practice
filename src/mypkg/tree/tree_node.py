"""A class that represent a node in binary tree."""


class TreeNode:
    """Binary Tree Node."""

    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
