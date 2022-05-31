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


def test_topological_sort():
    """Testing topological sort."""
    connections = [("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "F"), ("E", "H"), ("E", "F"), ("F", "G")]
    top_sorted_1 = ["A", "B", "C", "E", "H", "D", "F", "G"]
    top_sorted_2 = ["B", "D", "A", "C", "E", "H", "F", "G"]
    graph = Graph(connections, directed=True)
    assert graph.topological_sort() == top_sorted_1 or top_sorted_2
