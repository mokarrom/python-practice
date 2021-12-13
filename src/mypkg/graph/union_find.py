"""Union-Find algorithm."""
from typing import List


class QuickFindUF:
    """Find is faster but Union is too expensive.

    - Integer array/dictionary root[] of length N. Initialize all elements as their own root.
    - Find: a point/edge (p, q) is connected iff they have the same root.
    - Union: to merge components containing p and q,  change all entries whose root equals root[p] to root[q]
    """

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
    """Union is faster but Find is too expensive.

    - Integer array/dictionary root[] of length N. Initialize all elements as their own root.
    - roots[i] is the parent off i. Root of i is roots[roots[...roots[i]...]]
    - Find: a point/edge (p, q) is connected iff they have the same root.
    - Union: to merge components containing p and q, set p's root to the q's root.
    """

    def __init__(self, n: int):
        self.roots: List[int] = [i for i in range(n)]

    def _root(self, node: int):
        while node != self.roots[node]:
            node = self.roots[node]

        return node

    def _root_optimized(self, node: int):
        while node != self.roots[node]:
            self.roots[node] = self.roots[self.roots[node]]  # optimization: path compression
            node = self.roots[node]

        return node

    def connected(self, p: int, q: int) -> bool:
        """Are p and q in the same component?"""
        return bool(self._root_optimized(p) == self._root_optimized(q))

    def union(self, p: int, q: int):
        """Add connection between p and q."""
        p_root = self._root_optimized(p)
        q_root = self._root_optimized(q)
        self.roots[p_root] = q_root

    def count(self) -> int:
        """Return the number of components."""
        return -1
