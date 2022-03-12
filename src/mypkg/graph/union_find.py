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
        self.parent: List[int] = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node: int):
        """Returns the root of the given node."""
        while node != self.parent[node]:
            node = self.parent[node]

        return node

    def find_optimized(self, node: int):
        """Returns the root of the given node."""
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]  # optimization: path compression
            node = self.parent[node]

        return node

    def connected(self, p: int, q: int) -> bool:
        """Are p and q in the same component?"""
        return bool(self.find_optimized(p) == self.find_optimized(q))

    def union(self, p: int, q: int):
        """Add connection between p and q."""
        p_root = self.find_optimized(p)
        q_root = self.find_optimized(q)

        # We want to ensure the larger set remains the root.
        if self.size[p_root] < self.size[q_root]:
            # Make q_root the overall root.
            self.parent[p_root] = q_root
            # The size of the set rooted at q is the sum of the two.
            self.size[q_root] += self.size[p_root]
        else:
            # Make p_root the overall root.
            self.parent[q_root] = p_root
            # The size of the set rooted at p is the sum of the two.
            self.size[p_root] += self.size[q_root]

    def count(self) -> int:
        """Return the number of components."""
        return -1
