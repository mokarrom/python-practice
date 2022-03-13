from mypkg.graph.union_find import QuickFindUF, QuickUnionUF


class Test:
    """Test class."""

    def test_uf(self):
        qf = QuickFindUF(10)
        self._quick_find(qf)

        qu = QuickUnionUF(10)
        self._quick_find(qu)

    @staticmethod
    def _quick_find(uf):
        uf.union(0, 5)
        uf.union(5, 6)
        uf.union(1, 2)
        uf.union(2, 7)
        uf.union(3, 4)
        uf.union(3, 8)
        uf.union(4, 9)

        assert uf.connected(8, 9)
        assert not uf.connected(1, 6)
        assert not uf.connected(2, 8)

        uf.union(1, 6)
        assert uf.connected(1, 6)
