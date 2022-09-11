"""Implement a stak with max() function."""
from typing import List


class MaxStack:
    """A stack that supports push, pop, top, and retrieving the maximum element in constant time."""

    def __init__(self):
        self.stack: List[int] = list()
        self.max_cache: List[List[int]] = list()

    def push(self, val: int) -> None:
        """Pushes the element val onto the stack."""
        self.stack.append(val)

        # if max_cache is empty or val is greater than the top of the max_cache,
        # put it with count 1.
        if not self.max_cache or val > self.max_cache[-1][0]:
            self.max_cache.append([val, 1])
        # Else if val is equal to max_cache top, increment the top's counter by 1.
        elif val == self.max_cache[-1][0]:
            self.max_cache[-1][1] += 1

    def pop(self) -> None:
        """Removes the element on the top of the stack."""
        if not self.stack:
            raise ValueError("Stack is empty!")

        if self.stack[-1] == self.max_cache[-1][0]:
            if self.max_cache[-1][1] == 1:
                self.max_cache.pop()
            else:
                self.max_cache[-1][1] -= 1

        self.stack.pop()

    def top(self) -> int:
        """Gets the top element of the stack."""
        return self.stack[-1]

    def get_max(self) -> int:
        """Gets the maximum element of the stack."""
        return self.max_cache[-1][0]


if __name__ == "__main__":
    max_stack = MaxStack()

    max_stack.push(5)
    max_stack.push(3)
    max_stack.push(9)

    assert max_stack.get_max() == 9
    assert max_stack.top() == 9

    max_stack.pop()
    assert max_stack.get_max() == 5
    assert max_stack.top() == 3
