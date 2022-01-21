import math
from collections import Counter, defaultdict, deque
from itertools import chain, product
from typing import List, Dict, Optional, Set, FrozenSet
from functools import lru_cache
import heapq
import bisect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n_bits = int(math.log2(n)) + 1
        bitmask = (1 << n_bits) - 1
        return bitmask ^ n


if __name__ == "__main__":
    sln = Solution()

    letters = ["c", "f", "j", "j", "m", "p"]
    target = "p"


print(sln.bitwiseComplement(0))
