class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackIterator:
    def __init__(self, top_node):
        self.current_node = top_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        data = self.current_node.data
        self.current_node = self.current_node.next
        return data


class Stack:
    def __init__(self):
        self._top_node = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self._top_node
        self._top_node = new_node
        self._size += 1
        if self._size == 1:
            print("Новый элемент стал вершиной стека.")
        else:
            print("Элемент стал вершиной стека.")

    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека.")
        popped_node = self._top_node
        self._top_node = self._top_node.next
        self._size -= 1
        print(f"Элемент {popped_node.data} удален из стека.")
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека.")
        return self._top_node.data

    def is_empty(self):
        return self._top_node is None

    def size(self):
        return self._size

    def display(self):
        current = self._top_node
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Стек: " + " -> ".join(map(str, elements)))

    def __iter__(self):
        return StackIterator(self._top_node)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print(f"Верхний элемент: {stack.peek()}")
print(f"Стек пуст: {stack.is_empty()}")
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
print(f"Стек пуст: {stack.is_empty()}")

# итерация
stack.push(10)
stack.push(20)
stack.push(30)

for item in stack:
    print(item)
