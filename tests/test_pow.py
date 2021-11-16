from pytest import fixture, mark
from mypkg.recursion.pow import MyPow


class TestMyPow:
    @fixture(scope="class")
    def test_cases(self):
        tests = [
            (2, 4, pow(2, 4)),
            (2, -4, pow(2, -4)),
            (2, 10, pow(2, 10)),
            (2.1, 3, pow(2.1, 3))
        ]
        return tests

    def test_recursive_pow(self, test_cases):
        for cur_test in test_cases:
            assert MyPow.recursive_pow(cur_test[0], cur_test[1]) == cur_test[2]

        assert MyPow.recursive_pow(0.00001, 2147483647) == pow(0.00001, 2147483647)
        assert MyPow.recursive_pow(2, 5000) == pow(2, 5000)

    def test_iterative_pow(self, test_cases):
        for cur_test in test_cases:
            assert MyPow.iterative_pow(cur_test[0], cur_test[1]) == cur_test[2]

        assert MyPow.iterative_pow(0.00001, 2147483647) == pow(0.00001, 2147483647)
        # assert MyPow.iterative_pow(2, 5000) == pow(2, 5000)

    def test_naive_pow(self, test_cases):
        for cur_test in test_cases:
            assert MyPow.naive_pow(cur_test[0], cur_test[1]) == cur_test[2]

        # assert MyPow.naive_pow(0.00001, 2147483647) == pow(0.00001, 2147483647)
        # assert MyPow.naive_pow(2, 5000) == pow(2, 5000)
