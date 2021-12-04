"""Union-Find algorithm."""
from typing import List


class QuickFindUF:
    """Find is faster but Union is too expensive."""

    def __init__(self, n: int):
        self.roots: List[int] = [i for i in range(n)]

    def connected(self, p: int, q: int) -> bool:
        """Are p and q in the same component?"""
        return self.roots[p] == self.roots[q]

    def union(self, p: int, q: int):
        """Add connection between p and q."""
        p_root = self.roots[p]
        q_root = self.roots[q]

        for idx, root in enumerate(self.roots):
            if root == p_root:
                self.roots[idx] = q_root

    def count(self) -> int:
        """Return the number of components."""
        return -1


class QuickUnionUF:
    """Union is faster but Find is too expensive."""

    def __init__(self, n: int):
        self.roots: List[int] = [i for i in range(n)]

    def _root(self, node: int):
        while node != self.roots[node]:
            self.roots[node] = self.roots[self.roots[node]]  # optimization: path compression
            node = self.roots[node]

        return node

    def connected(self, p: int, q: int) -> bool:
        """Are p and q in the same component?"""
        return bool(self._root(p) == self._root(q))

    def union(self, p: int, q: int):
        """Add connection between p and q."""
        p_root = self._root(p)
        q_root = self._root(q)
        self.roots[p_root] = q_root

    def count(self) -> int:
        """Return the number of components."""
        return -1
