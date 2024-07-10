class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self._first_node = None
        self._last_node = None
        self._size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._first_node = new_node
        else:
            self._last_node.next = new_node
        self._last_node = new_node
        self._size += 1
        print(f"Элемент {item} добавлен в очередь.")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустой очереди.")
        dequeued_node = self._first_node
        self._first_node = self._first_node.next
        if self._first_node is None:
            self._first_node = None
        self._size -=1
        print(f"Элемент {dequeued_node.data} удалён из очереди.")
        return dequeued_node.data

    def front(self):
        if self.is_empty():
            raise IndexError("Попытка посмотреть элемент в пустой очереди.")
        return self._first_node.data

    def is_empty(self):
        return self._first_node is None
    
    def size(self):
        return self._size
    
    def display(self):
        current = self._first_node
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Очередь: " + " -> ".join(map(str, elements)))
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print(f"Первый элемент: {queue.front()}")
print(f"Очередь пуста: {queue.is_empty()}")
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
print(f"Очередь пуста: {queue.is_empty()}")