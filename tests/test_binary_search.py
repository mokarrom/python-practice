from typing import List, Union
from pytest import fixture
from search.binary_search import BinarySearch


class TestBinarySearch:
    """Binary Search test class."""

    @fixture(scope="class", params=["numbers", "names"])
    def get_items(self, request):
        items: List[Union[int, str]]
        if request.param == "numbers":
            items = [-1, 5, 6, 18, 19, 25, 46, 78, 102, 114]
        elif request.param == "names":
            items = ["Chandler", "Joye", "Monica", "Phebe", "Rachel", "Ross"]
        else:
            raise ValueError("Invalid Param")

        return items

    def test_iterative_search(self, get_items):
        if type(get_items[0]) == int:
            assert BinarySearch.iterative_search(get_items, 102) == 8
            assert BinarySearch.iterative_search(get_items, -1) == 0
            assert BinarySearch.iterative_search(get_items, 114) == 9
            assert BinarySearch.iterative_search(get_items, 120) == -1
            assert BinarySearch.iterative_search(get_items, 7) == -1
        else:
            assert BinarySearch.iterative_search(get_items, "Tom") == -1
            assert BinarySearch.iterative_search(get_items, "Joye") == 1
            assert BinarySearch.iterative_search(get_items, "Ross") == 5
            assert BinarySearch.iterative_search(get_items, "Chandler") == 0
            assert BinarySearch.iterative_search(get_items, "Monica") == 2

    def test_recur_search(self, get_items):
        if type(get_items[0]) == int:
            assert BinarySearch.recur_search(get_items, 0, (len(get_items) - 1), 102) == 8
            assert BinarySearch.recur_search(get_items, 0, (len(get_items) - 1), -1) == 0
            assert BinarySearch.recur_search(get_items, 0, (len(get_items) - 1), 114) == 9
            assert BinarySearch.recur_search(get_items, 0, (len(get_items) - 1), 120) == -1
            assert BinarySearch.recur_search(get_items, 0, (len(get_items) - 1), 7) == -1
        else:
            assert BinarySearch.recur_search(get_items, 0, len(get_items) - 1, "Tom") == -1
            assert BinarySearch.recur_search(get_items, 0, len(get_items) - 1, "Joye") == 1
            assert BinarySearch.recur_search(get_items, 0, len(get_items) - 1, "Ross") == 5
            assert BinarySearch.recur_search(get_items, 0, len(get_items) - 1, "Chandler") == 0
            assert BinarySearch.recur_search(get_items, 0, len(get_items) - 1, "Monica") == 2
