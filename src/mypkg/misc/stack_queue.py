"""Stack/Queue implementation."""
from typing import List, Any, Deque
from collections import deque


class MyStack:
    """Stack implementation using python list."""

    def __init__(self):
        self._items: List[Any] = list()

    def push(self, x: Any) -> None:
        """Push an element at the top of stack."""
        self._items.append(x)

    def pop(self) -> Any:
        """Remove an element from top of the stack."""
        if self.empty():
            raise ValueError("Stack is empty!")

        return self._items.pop()

    def peek(self) -> Any:
        """Return stack top."""
        return self._items[-1]

    def empty(self) -> bool:
        """Return True when the stack is empty, otherwise False."""
        return not self._items


class MyQueue:
    """Queue implementation using Deque - Doubly Ended Queue."""

    # Good for quicker append and pop operations from both the ends
    def __init__(self):
        self._items: Deque[Any] = deque()

    def push(self, x: Any) -> None:
        """Add an element at the back of queue."""
        self._items.appendleft(x)

    def pop(self) -> Any:
        """Remove and return the front element from the queue."""
        if self.empty():
            raise ValueError("Queue is empty!")

        return self._items.pop()

    def peek(self) -> Any:
        """Return the front element from the queue."""
        return self._items[-1]

    def empty(self) -> bool:
        """Return True when the queue is empty, otherwise False."""
        return not self._items


class QueueUsingStack:
    """Queue implementation using two stacks. push() -> O(1), pop() -> amortized O(1)."""

    def __init__(self):
        self._rear_stack = MyStack()
        self._front_stack = MyStack()

    def _move_rear_to_front(self) -> None:
        while not self._rear_stack.empty():
            self._front_stack.push(self._rear_stack.pop())

    def push(self, x: Any) -> None:
        """Add an element at the back of queue."""
        self._rear_stack.push(x)

    def pop(self) -> Any:
        """Remove and return the front element from the queue."""
        if self._front_stack.empty() and self._rear_stack.empty():
            raise ValueError("Queue is empty!")

        if self._front_stack.empty():
            self._move_rear_to_front()

        return self._front_stack.pop()

    def peek(self) -> Any:
        """Return the front element from the queue."""
        if self._front_stack.empty():
            self._move_rear_to_front()

        return self._front_stack.peek()

    def empty(self) -> bool:
        """Return True when the queue is empty, otherwise False."""
        return self._front_stack.empty() and self._rear_stack.empty()
