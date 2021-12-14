"""Linked List test."""
from mypkg.linkedlist.singly_linkedlist import SLinkedList


def test_singly_linkedlist():
    sg_list = SLinkedList()

    assert not sg_list.contain(5)
    sg_list.insert_last(5)
    assert sg_list.contain(5)
    assert sg_list.get_nodes() == [5]
    sg_list.insert_first(3)
    assert sg_list.get_nodes() == [3, 5]
    sg_list.insert_last(7)
    sg_list.insert_first(1)
    assert sg_list.get_nodes() == [1, 3, 5, 7]
    sg_list.insert_at(2, 4)
    assert sg_list.get_nodes() == [1, 3, 4, 5, 7]
    sg_list.insert_at(0, 6)
    assert sg_list.get_nodes() == [6, 1, 3, 4, 5, 7]
    sg_list.insert_at(6, 8)
    assert sg_list.get_nodes() == [6, 1, 3, 4, 5, 7, 8]
    sg_list.insert_at(9, 9)
    assert sg_list.get_nodes() == [6, 1, 3, 4, 5, 7, 8, 9]
    assert sg_list.size() == len(sg_list.get_nodes())

    assert sg_list.contain(5)
    assert sg_list.contain(6)
    assert sg_list.contain(9)
    assert not sg_list.contain(2)
    assert not sg_list.contain(11)

    sg_list.delete(6)
    assert sg_list.get_nodes() == [1, 3, 4, 5, 7, 8, 9]
    sg_list.delete(9)
    assert sg_list.get_nodes() == [1, 3, 4, 5, 7, 8]
    sg_list.delete(4)
    assert sg_list.get_nodes() == [1, 3, 5, 7, 8]
    assert sg_list.size() == len(sg_list.get_nodes())
    sg_list.delete(6)
    assert sg_list.get_nodes() == [1, 3, 5, 7, 8]
    sg_list.delete(5)
    assert sg_list.get_nodes() == [1, 3, 7, 8]
    sg_list.delete(1)
    assert sg_list.get_nodes() == [3, 7, 8]
    assert sg_list.size() == len(sg_list.get_nodes())
    sg_list.delete(8)
    assert sg_list.get_nodes() == [3, 7]
    sg_list.delete(7)
    assert sg_list.get_nodes() == [3]
    assert sg_list.size() == len(sg_list.get_nodes())
    sg_list.delete(3)
    assert sg_list.get_nodes() == []
    assert sg_list.size() == len(sg_list.get_nodes())

    sg_list.insert_first(5)
    assert sg_list.get_nodes() == [5]
    sg_list.insert_last(7)
    assert sg_list.get_nodes() == [5, 7]
    sg_list.delete(7)
    assert sg_list.get_nodes() == [5]
