from typing import List
from mypkg.sort.insertion_sort import InsertionSort
from mypkg.sort.merge_sort import MergeSort
from mypkg.sort.quick_sort import QuickSort
from mypkg.sort.heap_sort import MaxHeap, HeapSort

NUMS: List[List[int]] = [
    [],
    [1],
    [1, 2],
    [2, 1],
    [3, 6, 0, 1, 5],
    [7, 2, 4, 1, 5, 3],
    [19, 9, 3, 7, 9, 0, 4, 33, 2, 5, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [22, 21, 19, 18, 15, 14, 9, 7, 5],
    [5, 4, 4, 1, 1, 3, 3, 7, 7],
]


def test_insertion_sort():
    for _nums in NUMS:
        InsertionSort.sort(_nums)
        assert _nums == sorted(_nums)


def test_merge_sort():
    for _nums in NUMS:
        MergeSort.sort(_nums)
        assert _nums == sorted(_nums)


def test_quick_sort():
    for _nums in NUMS:
        QuickSort.sort(_nums)
        assert _nums == sorted(_nums)


def test_heap_sort():
    for _nums in NUMS:
        HeapSort.sort(_nums)
        assert _nums == sorted(_nums)


def test_max_heap():
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    MaxHeap.build_heap(arr)
    assert arr == [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
    assert MaxHeap.pop(arr) == 17
    assert arr == [15, 9, 13, 8, 6, 5, 10, 4, 1, 3]
    MaxHeap.push(arr, 20)
    assert arr == [20, 15, 13, 8, 9, 5, 10, 4, 1, 3, 6]
    MaxHeap.push(arr, 16)
    assert arr == [20, 15, 16, 8, 9, 13, 10, 4, 1, 3, 6, 5]
    MaxHeap.push(arr, 3)
    assert arr == [20, 15, 16, 8, 9, 13, 10, 4, 1, 3, 6, 5, 3]
