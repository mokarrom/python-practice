from mypkg.misc.stack_queue import MyStack, MyQueue, QueueUsingStack


class TestStackQueue:
    def test_stack(self):
        stack = MyStack()

        stack.push(3)
        stack.push(5)
        stack.push(7)
        assert stack.pop() == 7
        stack.push(9)
        assert stack.pop() == 9
        assert not stack.empty()
        assert stack.pop() == 5
        assert stack.pop() == 3
        assert stack.empty()

    def test_queue(self):
        queue = MyQueue()

        queue.push(3)
        queue.push(5)
        queue.push(7)

        assert queue.pop() == 3
        queue.push(9)
        assert queue.pop() == 5
        assert not queue.empty()
        assert queue.pop() == 7
        assert queue.pop() == 9
        assert queue.empty()

    def test_stack_queue(self):
        queue = QueueUsingStack()

        queue.push(3)
        queue.push(5)
        queue.push(7)

        assert queue.pop() == 3
        queue.push(9)
        assert queue.pop() == 5
        assert not queue.empty()
        assert queue.pop() == 7
        assert queue.pop() == 9
        assert queue.empty()
