from pytest import fixture
from mypkg.tree.bst import BST


@fixture(scope="module")
def bst():
    bst = BST()
    # ==========Binary Search Tree========
    # [8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13, null]
    #                 8
    #             /       \
    #          /             \
    #         3                10
    #      /     \               \
    #    /         \               \
    #   1           6              14
    #             /    \          /
    #            4      7        13
    items = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for item in items:
        bst.insert(item)
    return bst


def test_display(bst):
    assert bst.display() == [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13, None]


def test_contains(bst):
    assert bst.contains(14)
    assert bst.contains(6)
    assert not bst.contains(12)
    assert not bst.contains(2)


def tst_height_and_depth(bst):
    assert bst.get_height() == 3
    assert bst.get_height() == 3
    assert bst.max_depth() == 4
    assert bst.min_depth() == 3


def test_traversal(bst):
    assert bst.level_order_traverse() == [8, 3, 10, 1, 6, 14, 4, 7, 13]
    assert bst.pre_order_traverse() == [8, 3, 1, 6, 4, 7, 10, 14, 13]
    assert bst.in_order_traverse() == [1, 3, 4, 6, 7, 8, 10, 13, 14]
    assert bst.post_order_traverse() == [1, 4, 7, 6, 3, 13, 14, 10, 8]


def test_valid_max(bst):
    assert bst.find_maximum_value() == 14
    assert bst.find_minimum_value() == 1
    assert bst.is_valid_bst1()
    assert bst.is_valid_bst2()
    assert not bst.is_complete()
    assert bst.find(14).data == 14
    assert bst.find(6).data == 6
    assert bst.find(1).data == 1


def test_find_successor(bst):
    assert bst.find_inorder_successor_bt(3).data == 4
    assert bst.find_inorder_successor_bt(1).data == 3
    assert not bst.find_inorder_successor_bt(14)
    assert not bst.find_inorder_successor_bt(12)
    assert not bst.find_inorder_successor_bt(2)

    assert bst.find_inorder_successor_bst(3).data == 4
    assert bst.find_inorder_successor_bst(1).data == 3
    assert not bst.find_inorder_successor_bt(14)
    assert not bst.find_inorder_successor_bt(12)
    assert not bst.find_inorder_successor_bt(2)


def test_find_predecessor(bst):
    assert bst.find_inorder_predecessor_bst(6).data == 4
    assert bst.find_inorder_predecessor_bst(10).data == 8
    assert not bst.find_inorder_predecessor_bst(1)
