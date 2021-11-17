from typing import List


class QuickFindUF:
    def __init__(self, n: int):
        self.roots: List[int] = [i for i in range(n)]

    def connected(self, p: int, q: int) -> bool:
        return self.roots[p] == self.roots[q]

    def union(self, p: int, q: int):
        p_root = self.roots[p]
        q_root = self.roots[q]

        for idx, root in enumerate(self.roots):
            if root == p_root:
                self.roots[idx] = q_root


class QuickUnionUF:
    def __init__(self, n: int):
        self.roots: List[int] = [i for i in range(n)]

    def _root(self, node: int):
        while node != self.roots[node]:
            self.roots[node] = self.roots[self.roots[node]]  # optimization: path compression
            node = self.roots[node]

        return node

    def connected(self, p: int, q: int) -> bool:
        return self._root(p) == self._root(q)

    def union(self, p: int, q: int):
        p_root = self._root(p)
        q_root = self._root(q)
        self.roots[p_root] = q_root
