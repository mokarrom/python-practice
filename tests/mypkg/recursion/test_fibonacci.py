import mypkg.recursion.fibonacci as fib

FIB_NUMS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
"""We omit 0'th Fibonacci, so the first Fibonacci is 1, second is 1, third is 2, and so on."""


def test_fib_recur_bf():
    for n in range(1, len(FIB_NUMS)):
        assert fib.fib_recur_bf(n) == FIB_NUMS[n]


def test_fib_iterative():
    for n in range(1, len(FIB_NUMS)):
        assert fib.fib_iterative(n) == FIB_NUMS[n]


def test_fib_space_optimized():
    for n in range(1, len(FIB_NUMS)):
        assert fib.fib_space_optimized(n) == FIB_NUMS[n]
