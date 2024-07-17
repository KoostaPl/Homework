import pytest
from queues import Queue


class TestQueue:
    def test_enqueue_empty_queue(self, capsys):
        queue = Queue()
        queue.enqueue(10)
        captured = capsys.readouterr()
        assert "Новый элемент стал началом очереди" in captured.out
        assert queue.size() == 1

    def test_enqueue_to_non_empty_queue(self, capsys):
        queue = Queue()
        queue.enqueue(10)
        captured = capsys.readouterr()
        queue.enqueue(20)
        captured = capsys.readouterr()
        assert "Элемент стал концом очереди." in captured.out
        assert queue.front() == 10
        assert queue.size() == 2

    def test_dequeue_from_empty_queue(self):
        queue = Queue()
        with pytest.raises(IndexError):
            queue.dequeue()

    def test_dequeue_from_one_element__queue(self, capsys):
        queue = Queue()
        queue.enqueue(10)
        queue.size() == 1
        dequeued = queue.dequeue()
        captured = capsys.readouterr()
        assert "Элемент 10 удалён из очереди." in captured.out
        assert dequeued == 10
        assert queue.is_empty()
        assert queue.size() == 0

    def test_dequeue_from_multiple_element__queue(self, capsys):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        dequeued = queue.dequeue()
        captured = capsys.readouterr()
        assert "Элемент 10 удалён из очереди." in captured.out
        assert dequeued == 10
        assert not queue.is_empty()
        assert queue.front() == 20
        assert queue.size() == 2

    def test_front_from_empty_queue(self):
        queue = Queue()
        with pytest.raises(IndexError):
            queue.front()

    def test_front_from_multiple_elements_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.front() == 1
        assert queue.size() == 3

    def test_is_empty_empty_queue(self):
        queue = Queue()
        assert queue.is_empty() is True
        assert queue.size() == 0

    def test_is_empty_non_empty_queue(self):
        queue = Queue()
        queue.enqueue(5)
        assert queue.is_empty() is False
        assert queue.size() >= 1

    def test_size_empty_queue(self):
        queue = Queue()
        assert queue.is_empty() is True
        assert queue.size() == 0

    def test_size_non_empty_queue(self):
        queue = Queue()
        queue.enqueue(9)
        queue.enqueue(24)
        queue.enqueue(900)
        expected_size = 3
        assert queue.size() == expected_size

    def test_queue_iterator_empty(self):
        queue = Queue()
        iterator = iter(queue)
        with pytest.raises(StopIteration):
            next(iterator)

    def test_queue_iterator_non_empty(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        iterator = iter(queue)

        assert next(iterator) == 10
        assert next(iterator) == 20
        assert next(iterator) == 30

        with pytest.raises(StopIteration):
            next(iterator)
