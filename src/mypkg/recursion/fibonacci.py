"""Different implementations of Fibonacci numbers."""


def fib_recur_bf(n: int) -> int:
    """Return n'th fibonacci number; where n > 0."""
    if n < 3:
        return 1

    return fib_recur_bf(n - 1) + fib_recur_bf(n - 2)


def fib_iterative(n: int) -> int:
    """Bottom dp table. Linear time and space complexity."""
    if n < 3:
        return 1

    dp = [0] * n
    dp[0] = dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1]


def fib_space_optimized(n: int) -> int:
    """Constant space and linear time."""
    fib = fib1 = fib2 = 1
    for _ in range(2, n):
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib

    return fib
