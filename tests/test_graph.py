from mypkg.graph.graph import Graph


class TestGraph:
    """Test class for graph."""

    # A-- -- --B-- -- --C
    # | \      |     /  |   \
    # |   \    |   /    |     G
    # |     \  | /      |   /
    # D-- -- --E-- -- --F

    def setup_method(self):
        connections = [
            ("A", "B"),
            ("A", "D"),
            ("A", "E"),
            ("B", "C"),
            ("B", "E"),
            ("C", "E"),
            ("C", "F"),
            ("C", "G"),
            ("D", "E"),
            ("E", "F"),
            ("F", "G"),
        ]

        self.graph = Graph(connections)
        self.graph.display_graph()

    def test_bfs(self):
        nodes = self.graph.bfs("A")
        assert len(nodes) == 7

        nodes = self.graph.dfs_iterative("A")
        assert len(nodes) == 7

        nodes = self.graph.dfs_recursive("A")
        assert len(nodes) == 7
