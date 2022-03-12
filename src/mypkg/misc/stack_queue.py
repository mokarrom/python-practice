from typing import List, Any, Deque
from collections import deque


class MyStack:
    """Stack implementation using python list."""

    def __init__(self):
        self._items: List[Any] = list()

    def push(self, x: Any) -> None:
        self._items.append(x)

    def pop(self) -> Any:
        if self.empty():
            raise ValueError("Stack is empty!")

        return self._items.pop()

    def peek(self) -> Any:
        return self._items[-1]

    def empty(self) -> bool:
        return not self._items


class MyQueue:
    """Queue implementation using Deque - Doubly Ended Queue."""
    # Good for quicker append and pop operations from both the ends
    def __init__(self):
        self._items: Deque[Any] = deque()

    def push(self, x: Any) -> None:
        self._items.appendleft(x)

    def pop(self) -> Any:
        if self.empty():
            raise ValueError("Queue is empty!")

        return self._items.pop()

    def peek(self) -> Any:
        return self._items[-1]

    def empty(self) -> bool:
        return not self._items


class QueueUsingStack:
    """Queue implementation using two stacks. push() -> O(1), pop() -> amortized O(1)."""

    def __init__(self):
        self._rear_stack = MyStack()
        self._front_stack = MyStack()

    def _move_rear_to_front(self) -> None:
        while not self._rear_stack.empty():
            self._front_stack.push(self._rear_stack.pop())

    def push(self, x: int) -> None:
        self._rear_stack.push(x)

    def pop(self) -> int:
        if self._front_stack.empty() and self._rear_stack.empty():
            raise ValueError("Queue is empty!")

        if self._front_stack.empty():
            self._move_rear_to_front()

        return self._front_stack.pop()

    def peek(self) -> int:
        if self._front_stack.empty():
            self._move_rear_to_front()

        return self._front_stack.peek()

    def empty(self) -> bool:
        return self._front_stack.empty() and self._rear_stack.empty()
