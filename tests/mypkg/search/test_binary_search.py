import math
from typing import List, Union
from pytest import fixture
from mypkg.search.binary_search import BinarySearch, BinarySearchAnswer


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
            assert BinarySearch.recur_search(get_items, 102, 0, (len(get_items) - 1)) == 8
            assert BinarySearch.recur_search(get_items, -1, 0, (len(get_items) - 1)) == 0
            assert BinarySearch.recur_search(get_items, 114, 0, (len(get_items) - 1)) == 9
            assert BinarySearch.recur_search(get_items, 120, 0, (len(get_items) - 1)) == -1
            assert BinarySearch.recur_search(get_items, 7, 0, (len(get_items) - 1)) == -1
        else:
            assert BinarySearch.recur_search(get_items, "Tom", 0, len(get_items) - 1) == -1
            assert BinarySearch.recur_search(get_items, "Joye", 0, len(get_items) - 1) == 1
            assert BinarySearch.recur_search(get_items, "Ross", 0, len(get_items) - 1) == 5
            assert BinarySearch.recur_search(get_items, "Chandler", 0, len(get_items) - 1) == 0
            assert BinarySearch.recur_search(get_items, "Monica", 0, len(get_items) - 1) == 2
            assert BinarySearch.recur_search(get_items, "John", 0, len(get_items) - 1) == -1

    def test_rotated_sorted_array_search(self):
        assert BinarySearch.rotated_sorted_array_search([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert BinarySearch.rotated_sorted_array_search([4, 5, 6, 7, 0, 1, 2], 3) == -1
        assert BinarySearch.rotated_sorted_array_search([1], 0) == -1

        assert BinarySearch.rotated_sorted_array_search([1, 2, 3, 4, 5], 2) == 1
        assert BinarySearch.rotated_sorted_array_search([5, 1, 2, 3, 4], 2) == 2
        assert BinarySearch.rotated_sorted_array_search([4, 5, 1, 2, 3], 2) == 3
        assert BinarySearch.rotated_sorted_array_search([3, 4, 5, 1, 2], 2) == 4
        assert BinarySearch.rotated_sorted_array_search([2, 3, 4, 5, 1], 2) == 0

        assert BinarySearch.rotated_sorted_array_search([2, 1], 2) == 0
        assert BinarySearch.rotated_sorted_array_search([2, 1], 1) == 1
        assert BinarySearch.rotated_sorted_array_search([2, 1], 3) == -1

    def test_find_min_rotated_sorted_array(self):
        assert BinarySearch.find_min_rotated_sorted_array([3, 4, 5, 1, 2]) == 1
        assert BinarySearch.find_min_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2]) == 0

        assert BinarySearch.find_min_rotated_sorted_array([1, 2, 3, 4, 5]) == 1
        assert BinarySearch.find_min_rotated_sorted_array([5, 1, 2, 3, 4]) == 1
        assert BinarySearch.find_min_rotated_sorted_array([4, 5, 1, 2, 3]) == 1
        assert BinarySearch.find_min_rotated_sorted_array([3, 4, 5, 1, 2]) == 1
        assert BinarySearch.find_min_rotated_sorted_array([2, 3, 4, 5, 1]) == 1

    def test_find_index(self, get_items):
        if type(get_items[0]) == int:
            assert BinarySearch.find_index(get_items, 102) == 8
            assert BinarySearch.find_index(get_items, -1) == 0
            assert BinarySearch.find_index(get_items, 114, True) == 9
            assert BinarySearch.find_index(get_items, 120, False) == -1
            assert BinarySearch.find_index(get_items, 7) == -1
        else:
            assert BinarySearch.find_index(get_items, "Tom") == -1
            assert BinarySearch.find_index(get_items, "Joye", True) == 1
            assert BinarySearch.find_index(get_items, "Ross") == 5
            assert BinarySearch.find_index(get_items, "Chandler", False) == 0
            assert BinarySearch.find_index(get_items, "Monica", False) == 2

        items = [2, 7, 7, 7, 8, 10]
        assert BinarySearch.find_index(items, 6) == -1
        assert BinarySearch.find_index(items, 8) == 4
        assert BinarySearch.find_index(items, 7) == 1
        assert BinarySearch.find_index(items, 7, first_occurrence=True) == 1
        assert BinarySearch.find_index(items, 7, first_occurrence=False) == 3
        assert BinarySearch.find_index(items, 10, first_occurrence=False) == 5
        assert BinarySearch.find_index(items, 17, first_occurrence=False) == -1

    def test_find_first_index(self):
        items = [2, 7, 7, 7, 8, 10]
        assert BinarySearch.find_first_index(items, 6) == -1
        assert BinarySearch.find_first_index(items, 8) == 4
        assert BinarySearch.find_first_index(items, 7) == 1
        assert BinarySearch.find_first_index(items, 10) == 5
        assert BinarySearch.find_first_index(items, 17) == -1

        items = [2, 3]
        assert BinarySearch.find_first_index(items, 2) == 0
        assert BinarySearch.find_first_index(items, 3) == 1

        items = [2, 2]
        assert BinarySearch.find_first_index(items, 2) == 0
        assert BinarySearch.find_first_index(items, 3) == -1

    def test_find_last_index(self):
        items = [2, 7, 7, 7, 8, 10]
        assert BinarySearch.find_last_index(items, 6) == -1
        assert BinarySearch.find_last_index(items, 8) == 4
        assert BinarySearch.find_last_index(items, 7) == 3
        assert BinarySearch.find_last_index(items, 10) == 5
        assert BinarySearch.find_last_index(items, 17) == -1

        items = [2, 3]
        assert BinarySearch.find_last_index(items, 2) == 0
        assert BinarySearch.find_last_index(items, 3) == 1

        items = [2, 2]
        assert BinarySearch.find_last_index(items, 2) == 1
        assert BinarySearch.find_last_index(items, 3) == -1

    def test_find_bs_discrete(self, get_items):
        if type(get_items[0]) == int:
            assert BinarySearchAnswer.find_bs_discrete(get_items, 102) == 8
            assert BinarySearchAnswer.find_bs_discrete(get_items, -1) == 0
            assert BinarySearchAnswer.find_bs_discrete(get_items, 114) == 9
            assert BinarySearchAnswer.find_bs_discrete(get_items, 120) == -1
            assert BinarySearchAnswer.find_bs_discrete(get_items, 7) == 3
            assert BinarySearchAnswer.find_bs_discrete(get_items, -3) == -1
        else:
            assert BinarySearchAnswer.find_bs_discrete(get_items, "Tom") == -1
            assert BinarySearchAnswer.find_bs_discrete(get_items, "Joye") == 1
            assert BinarySearchAnswer.find_bs_discrete(get_items, "Ross") == 5
            assert BinarySearchAnswer.find_bs_discrete(get_items, "Chandler") == 0
            assert BinarySearchAnswer.find_bs_discrete(get_items, "Monica") == 2

        assert BinarySearchAnswer.find_bs_discrete([1], 1) == 0
        assert BinarySearchAnswer.find_bs_discrete([1], -1) == -1
        assert BinarySearchAnswer.find_bs_discrete([1], 2) == -1

        assert BinarySearchAnswer.find_bs_discrete([1, 2], 1) == 0
        assert BinarySearchAnswer.find_bs_discrete([1, 2], 2) == 1
        assert BinarySearchAnswer.find_bs_discrete([1, 2], 0) == -1
        assert BinarySearchAnswer.find_bs_discrete([1, 2], 3) == -1

    def test_sqrt_bs(self):
        nums = [4, 16, 81, 3.5]
        for num in nums:
            sqrt_num = round(BinarySearchAnswer.sqrt_bs(num), 3)
            assert math.isclose(sqrt_num, math.sqrt(num), abs_tol=0.001)

    def test_get_most_work(self):
        assert BinarySearchAnswer.get_most_work([10, 20, 30, 40, 50, 60, 70, 80, 90], 3) == 170
        assert BinarySearchAnswer.get_most_work([10, 20, 30, 40, 50, 60, 70, 80, 90], 5) == 110
        assert (
            BinarySearchAnswer.get_most_work(
                [568, 712, 412, 231, 241, 393, 865, 287, 128, 457, 238, 98, 980, 23, 782], 4
            )
            == 1785
        )
        assert BinarySearchAnswer.get_most_work([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000], 2) == 1000
        assert BinarySearchAnswer.get_most_work([50, 50, 50, 50, 50, 50, 50], 2) == 200
        assert BinarySearchAnswer.get_most_work([1, 1, 1, 1, 100], 5) == 100
        assert BinarySearchAnswer.get_most_work([950, 650, 250, 250, 350, 100, 650, 150, 150, 700], 6) == 950
