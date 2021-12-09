"""Graph algorithms."""
import pprint
from collections import defaultdict
from typing import List, Set, Tuple, Dict


class Graph(object):
    """Graph data structure, undirected by default."""

    def __init__(self, connections: List[Tuple[str, str]], directed=False):
        self._graph: Dict[str, Set[str]] = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)
        self._pretty_print = pprint.PrettyPrinter()

    def add_connections(self, connections: List[Tuple[str, str]]):
        """Add connections (list of tuple pairs) to graph."""
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1: str, node2: str):
        """Add a connection between node1 and node2."""
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node: str):
        """Remove all references to the given node."""
        for _, neighbors in self._graph.items():
            if node in neighbors:
                neighbors.remove(node)
        if node in self._graph:
            del self._graph[node]

    def __str__(self):
        """Overriding Object's str()."""
        return "{}({})".format(self.__class__.__name__, dict(self._graph))

    def display_graph(self):
        """Display graph's nodes and edges."""
        self._pretty_print.pprint(self._graph)

    def is_connected(self, node1: str, node2: str) -> bool:
        """Is node1 is connected to node2."""
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1: str, node2: str) -> List[str]:
        """Find any path between node1 and node2 (may not be shortest)."""
        path: List[str] = list()
        if node1 not in self._graph or node2 not in self._graph:
            return path

        path = path + [node1]

        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2)
                if new_path:
                    path.extend(new_path)
        return path

    def bfs(self, start_node: str) -> List[str]:
        """Return the Breadth-first traversal."""
        visited: List[str] = list()
        seen: Set[str] = set()
        queue: List[str] = list()

        if start_node not in self._graph:
            return visited

        seen.add(start_node)
        queue.append(start_node)

        while queue:
            cur_node = queue.pop(0)
            visited.append(cur_node)
            for neighbor in self._graph[cur_node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return visited

    def dfs_iterative(self, start_node: str) -> List[str]:
        """Return the Depth-first traversal."""
        visited: List[str] = list()
        seen: Set[str] = set()
        stack: List[str] = list()

        if start_node not in self._graph:
            return visited

        seen.add(start_node)
        stack.append(start_node)
        while stack:
            cur_node = stack.pop()
            visited.append(cur_node)
            for neighbor in self._graph[cur_node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        return visited

    def dfs_recursive(self, start_node: str, visited: List[str] = None) -> List[str]:
        """Return the Depth-first traversal."""
        if visited is None:
            visited = list()
        visited.append(start_node)
        for neighbor in self._graph[start_node]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

        return visited


if __name__ == "__main__":
    # A-- -- --B-- -- --C
    # | \      |     /  |   \
    # |   \    |   /    |     G
    # |     \  | /      |   /
    # D-- -- --E-- -- --F

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
    g = Graph(connections)

    g.display_graph()

    print(g.bfs("A"))
    print(g.dfs_iterative("A"))
    print(g.dfs_recursive("A"))

    # g.display_graph()
    # g.add('E', 'D')
    # g.display_graph()
    # g.remove('A')
    # g.display_graph()
    # g.add('G', 'B')
    # g.display_graph()
    # p = g.find_path('G', 'E')
    # print(p)
