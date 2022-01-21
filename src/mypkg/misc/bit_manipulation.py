"""Bit manipulation."""
import math
from typing import List


def count_bits(n: int):
    """Returns the total number of bits in n. Formula: floor(log2(n)) + 1."""
    return int(math.log2(n)) + 1


def count_bits2(n: int):
    """Returns the total number of bits in n. Formula: floor(log2(n)) + 1."""
    count = 0
    while n:
        count += 1
        n >>= 1

    return count


def bitwise_complement(n: int) -> int:
    """Returns the complement of n by flipping all bits of n."""
    if n == 0:
        return 1

    n_comp = n
    mask = 1
    while n:
        n_comp ^= mask
        mask <<= 1
        n >>= 1

    return n_comp


def bitwise_complement2(n: int) -> int:
    """Returns the complement of n by flipping all bits of n."""
    if n == 0:
        return 1

    n_bits = int(math.log2(n)) + 1
    bitmask = (1 << n_bits) - 1
    return bitmask ^ n


def generate_padded_binary(n: int) -> List[str]:
    """Generate all binary numbers up to n with zero left padded."""
    num_of_bits = int(math.log2(n)) + 1
    nth_bits = 1 << num_of_bits
    return [bin(i | nth_bits)[3:] for i in range(n)]


def generate_padded_binary(n: int) -> List[str]:
    """Generate all binary numbers up to n with zero left padded."""
    num_of_bits = int(math.log2(n)) + 1
    nth_bits = 1 << num_of_bits
    return [bin(i | nth_bits)[3:] for i in range(n)]
