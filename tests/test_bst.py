from mypkg.tree.bst import BST


def test_insert():
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

    assert bst.display() == [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13, None]
    assert bst.contains(14)
    assert bst.contains(6)
    assert not bst.contains(12)
    assert not bst.contains(2)

    assert bst.get_height() == 3
    assert bst.max_depth() == 4
    assert bst.min_depth() == 3
    assert bst.find_maximum_value() == 14
    assert bst.find_minimum_value() == 1

    assert bst.level_order_traverse() == [8, 3, 10, 1, 6, 14, 4, 7, 13]
    assert bst.pre_order_traverse() == [8, 3, 1, 6, 4, 7, 10, 14, 13]
    assert bst.in_order_traverse() == [1, 3, 4, 6, 7, 8, 10, 13, 14]
    assert bst.post_order_traverse() == [1, 4, 7, 6, 3, 13, 14, 10, 8]

    assert bst.is_valid_bst1()
    assert bst.is_valid_bst2()
    assert bst.find(14).data == 14
    assert bst.find(6).data == 6
    assert bst.find(1).data == 1

    assert bst.find_inorder_successor(3).data == 4
    assert bst.find_inorder_successor(1).data == 3
    assert not bst.find_inorder_successor(14)
    assert not bst.find_inorder_successor(12)
    assert not bst.find_inorder_successor(2)

    bst.delete(3)
    assert bst.display() == [8, 4, 10, 1, 6, None, 14, None, None, None, 7, 13, None]
    bst.delete(14)
    assert bst.display() == [8, 4, 10, 1, 6, None, 13, None, None, None, 7, None, None]
    bst.delete(1)
    assert bst.display() == [8, 4, 10, None, 6, None, 13, None, 7, None, None]
