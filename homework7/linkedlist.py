class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedListIterator:
    def __init__(self, start_node):
        self.current_node = start_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        data = self.current_node.data
        self.current_node = self.current_node.next
        return data

class LinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._size = 0

    def append(self, item):
        new_node = Node(item)
        if self._tail_node is None:
            self._head_node = new_node
            self._tail_node = new_node
        else:
            self._tail_node.next = new_node
            new_node.prev = self._tail_node
            self._tail_node = new_node
        self._size += 1
        print(f"Элемент {item} добавлен в конец списка.")

    def prepend(self, item):
        new_node = Node(item)
        if self._head_node is None:
            self._head_node = new_node
            self._tail_node = new_node
        else:
            new_node.next = self._head_node
            self._head_node.prev = new_node
            self._head_node = new_node
        self._size += 1
        print(f"Элемент {item} добавлен в начало списка.")

    def insert(self, item, i):
        if i < 0 or i > self._size:
            raise IndexError("Индекс вне диапазона.")
        new_node = Node(item)
        if i == 0:
            self.prepend(item)
        elif i == self._size:
            self.append(item)
        else:
            current = self._head_node
            for _ in range(i):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self._size += 1
            print(f"Элемент {item} вставлен на позицию {i}.")

    def delete(self, item):
        current = self._head_node
        while current:
            if current.data == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head_node = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail_node = current.prev
                self._size -= 1
                print(f"Элемент {item} удален из списка.")
                return
            current = current.next
        print(f"Элемент {item} не найден в списке.")

    def find(self, item):
        current = self._head_node
        while current:
            if current.data == item:
                return current
            current = current.next
        return None

    def display(self, reverse=False):
        elements = []
        if reverse:
            current = self._tail_node
            while current:
                elements.append(current.data)
                current = current.prev
        else:
            current = self._head_node
            while current:
                elements.append(current.data)
                current = current.next
        print(" -> ".join(map(str, elements)))

    def __getitem__(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Индекс вне диапазона.")
        current = self._head_node
        for _ in range(i):
            current = current.next
        return current.data

    def __len__(self):
        return self._size


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.prepend(5)
linked_list.insert(15, 2)
linked_list.display()
print(f"Элемент на позиции 2: {linked_list[2]}")
linked_list.delete(15)
linked_list.display()
print(f"Размер списка: {len(linked_list)}")

# итерация
for item in linked_list:
    print(item)
