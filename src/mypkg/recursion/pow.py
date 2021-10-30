
class MyPow:
    @staticmethod
    def recursive_pow(x: float, n: int) -> float:
        """Implement pow(x, n), i.e., raise x to the power n, i.e., calculate x^n."""
        if n == 0:
            return 1
        if n < 0:
            return 1 / MyPow.recursive_pow(x, abs(n))
        if n % 2 == 0:
            return MyPow.recursive_pow(x*x, n//2)
        else:
            return x * MyPow.recursive_pow(x*x, n//2)

    @staticmethod
    def iterative_pow(x: float, n: int) -> float:
        """Implement pow(x, n), i.e., raise x to the power n, i.e., calculate x^n."""
        result: float = 1.0
        if n < 0:
            n = -n
            x = 1/x
        while n > 0:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result

    @staticmethod
    def naive_pow(x: float, n: int) -> float:
        """Implement pow(x, n), i.e., raise x to the power n, i.e., calculate x^n."""
        result: float = 1.0
        if n < 0:
            n = -n
            x = 1/x
        while n > 0:
            result *= x
            n -= 1
        return result
