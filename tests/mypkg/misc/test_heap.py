import heapq
from collections import Counter
from mypkg.misc.heap import MinHeap, MaxHeapObj, Person


def test_min_heap():
    my_heap = MinHeap()

    nodes = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

    for node in nodes:
        my_heap.add(node)
    # ================= Min Heap Tree ============
    #                         5
    #                      /     \
    #                    /          \
    #                  9             11
    #                /   \           /  \
    #              /       \        /     \
    #            14         18     19      21
    #           /   \       /
    #         33     17   27
    assert my_heap.peek() == 5
    assert my_heap._size == 10
    assert my_heap._left_child(2) == 19
    assert my_heap._right_child(3) == 17
    assert my_heap._parent(4) == 9
    assert my_heap._parent(6) == 11
    assert my_heap._has_left_child(4)
    assert not my_heap._has_right_child(4)
    assert my_heap._has_parent(6)
    assert not my_heap._has_parent(0)
    assert my_heap.display_heap() == nodes

    my_heap.add(7)
    # ================= Min Heap Tree ============
    #                         5
    #                      /     \
    #                    /          \
    #                  7             11
    #                /   \           /  \
    #              /       \        /     \
    #            14         9     19      21
    #           /   \      /  \
    #         33     17   27   18
    assert my_heap._size == 11
    assert my_heap.display_heap() == [5, 7, 11, 14, 9, 19, 21, 33, 17, 27, 18]
    assert my_heap._parent(4) == 7
    assert my_heap._right_child(4) == 18

    assert my_heap.pool() == 5
    # ================= Min Heap Tree ============
    #                         7
    #                      /     \
    #                    /          \
    #                  9             11
    #                /   \           /  \
    #              /       \        /     \
    #            14         18     19      21
    #           /   \      /
    #         33     17   27
    assert my_heap._size == 10
    assert my_heap.display_heap() == [7, 9, 11, 14, 18, 19, 21, 33, 17, 27]
    assert my_heap._parent(4) == 9
    assert my_heap._left_child(4) == 27
    assert my_heap._right_child(1) == 18
    assert not my_heap._has_right_child(4)


def test_max_heap():
    freq_count = Counter("caabababcd")
    max_heap = [MaxHeapObj(char, freq) for char, freq in freq_count.items()]
    heapq.heapify(max_heap)

    sorted_chars = []
    while max_heap:
        heap_obj = heapq.heappop(max_heap)
        sorted_chars.append((heap_obj.char, heap_obj.freq))

    assert sorted_chars == [("d", 1), ("c", 2), ("b", 3), ("a", 4)]


def test_custom_heap():
    min_heap = [("a-1", Person("aaa", 65)), ("a-1", Person("abc", 35)), ("b-1", Person("bbb", 55))]
    heapq.heapify(min_heap)
    sin, person = heapq.heappop(min_heap)
    assert sin == "a-1"
    assert person.age == 35
