import pytest
from stack import Stack


class TestStack:
    def test_push_to_empty_stack(self, capsys):
        stack = Stack()
        stack.push(10)
        captured = capsys.readouterr()
        assert "Новый элемент стал вершиной стека." in captured.out
        assert stack.peek() == 10
        assert stack.size() == 1

    def test_push_to_non_empty_stack(self, capsys):
        stack = Stack()
        stack.push(10)
        captured = capsys.readouterr()
        stack.push(20)
        captured = capsys.readouterr()
        assert "Элемент стал вершиной стека." in captured.out
        assert stack.peek() == 20
        assert stack.size() == 2

    def test_pop_from_empty_stack(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()

    def test_pop_from_one_element_stack(self, capsys):
        stack = Stack()
        stack.push(10)
        stack.size() == 1
        popped = stack.pop()
        captured = capsys.readouterr()
        assert "Элемент 10 удален из стека." in captured.out
        assert popped == 10
        assert stack.is_empty()
        assert stack.size() == 0

    def test_pop_from_multiple_elements_stack(self, capsys):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        popped = stack.pop()
        captured = capsys.readouterr()
        assert "Элемент 30 удален из стека." in captured.out
        assert popped == 30
        assert not stack.is_empty()
        assert stack.peek() == 20
        assert stack.size() == 2

    def test_peek_from_empty_stack(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.peek()

    def test_peek_from_multiple_elements_stack(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        assert stack.peek() == 30
        assert stack.size() == 3

    def test_is_empty_empty_stack(self):
        stack = Stack()
        assert stack.is_empty() is True
        assert stack.size() == 0

    def test_is_empty_non_empty_stack(self):
        stack = Stack()
        stack.push(10)
        assert stack.is_empty() is False
        assert stack.size() >= 1

    def test_size_empty_stack(self):
        stack = Stack()
        assert stack.size() == 0
        assert stack.is_empty() is True

    def test_size_non_empty_stack(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        expected_size = 3
        assert stack.size() == expected_size

    def test_stack_iterator_empty(self):
        stack = Stack()
        iterator = iter(stack)
        with pytest.raises(StopIteration):
            next(iterator)

    def test_stack_iterator_non_empty(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        iterator = iter(stack)

        assert next(iterator) == 30
        assert next(iterator) == 20
        assert next(iterator) == 10

        with pytest.raises(StopIteration):
            next(iterator)
