"""LRU cache test."""
from mypkg.linkedlist.lru_cache import LRUCache, LRUCache2


def test_lru_cache():
    cache = LRUCache(capacity=3)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    cache.put(5, 5)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    assert cache.get(5) == 5
    cache.put(3, 13)
    cache.put(2, 12)
    assert cache.get(3) == 13
    cache.put(6, 6)
    cache.put(7, 7)
    cache.put(8, 8)

    cache = LRUCache(1)
    assert cache.get(1) == -1
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.get(2) == 2
    assert cache.get(2) == 2
    cache.put(4, 4)
    assert cache.get(4) == 4


def test_lru_cache_2():
    cache = LRUCache2(10)
    cache.put(10, 13)
    cache.put(3, 17)
    cache.put(6, 11)
    cache.put(10, 5)
    cache.put(9, 10)
    assert cache.get(13) == -1
    cache.put(2, 19)
    assert cache.get(2) == 19
    assert cache.get(3) == 17
    cache.put(5, 25)
    assert cache.get(8) == -1
    cache.put(9, 22)
    cache.put(5, 5)
    cache.put(1, 30)
    assert cache.get(11) == -1
    cache.put(9, 12)
    assert cache.get(7) == -1
    assert cache.get(5) == 5
    assert cache.get(8) == -1
    assert cache.get(9) == 12
    cache.put(4, 30)
    cache.put(9, 3)
    assert cache.get(9) == 3
    assert cache.get(10) == 5
    assert cache.get(10) == 5
    cache.put(6, 14)
    cache.put(3, 1)
    assert cache.get(3) == 1
    cache.put(10, 11)
    assert cache.get(8) == -1
    cache.put(2, 14)
    assert cache.get(1) == 30
    assert cache.get(5) == 5
    assert cache.get(4) == 30
    cache.put(11, 4)
    cache.put(12, 24)
    cache.put(5, 18)
    assert cache.get(13) == -1
    cache.put(7, 23)
    assert cache.get(8) == -1
    assert cache.get(12) == 24
    cache.put(3, 27)
    cache.put(2, 12)
    assert cache.get(5) == 18
    cache.put(2, 9)
    cache.put(13, 4)
    cache.put(8, 18)
    cache.put(1, 7)
    assert cache.get(6) == -1
    cache.put(9, 29)
    cache.put(8, 21)
    assert cache.get(5) == 18
