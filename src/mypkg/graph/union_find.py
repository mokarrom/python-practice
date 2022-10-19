"""Union-Find algorithm."""
from typing import List
from collections import defaultdict


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


class CountComponents:
    """323. Number of Connected Components in an Undirected Graph.

    https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
    """

    @staticmethod
    def count_components_uf(n: int, edges: List[List[int]]) -> int:
        """Count components using union-find algorithm."""
        root = [i for i in range(n)]
        size = [1] * n

        def find(p: int) -> int:
            node = p
            while node != root[node]:
                root[node] = root[root[node]]
                node = root[node]
            return node

        def union(p: int, q: int) -> int:
            p_root, q_root = find(p), find(q)

            if p_root == q_root:
                return 0

            if size[p_root] < size[q_root]:
                root[p_root] = q_root
                size[q_root] += size[p_root]
            else:
                root[q_root] = p_root
                size[p_root] += size[q_root]

            return 1

        comp_count = n
        for n1, n2 in edges:
            comp_count -= union(n1, n2)

        return comp_count

    @staticmethod
    def count_components_dfs(n: int, edges: List[List[int]]) -> int:
        """Count components using DFS."""
        visited = [False] * n
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(node: int) -> None:
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        comp_count = 0
        for u in range(n):
            if not visited[u]:
                dfs(u)
                comp_count += 1

        return comp_count
