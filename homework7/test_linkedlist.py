import pytest
from linkedlist import LinkedList


class TestLinkedList:
    def test_append_prepend_empty_linkedlist(self, capsys):
        linkedlist = LinkedList()
        linkedlist.append(10)
        captured = capsys.readouterr()
        assert "Элемент 10 добавлен в конец списка." in captured.out
        linkedlist.prepend(15)
        captured = capsys.readouterr()
        assert "Элемент 15 добавлен в начало списка." in captured.out
        assert len(linkedlist) == 2

    def test_append_prepend_to_not_empty_linkedlist(self, capsys):
        linkedlist = LinkedList()
        linkedlist.append(15)
        captured = capsys.readouterr()
        linkedlist.append(20)
        captured = capsys.readouterr()
        assert "Элемент 20 добавлен в конец списка." in captured.out
        linkedlist.prepend(10)
        captured = capsys.readouterr()
        linkedlist.prepend(5)
        captured = capsys.readouterr()
        assert "Элемент 5 добавлен в начало списка." in captured.out
        assert len(linkedlist) == 4

    def test_delete_from_empty_linkedlist(self, capsys):
        linkedlist = LinkedList()
        linkedlist.append(20)
        captured = capsys.readouterr()
        assert "Элемент 20 добавлен в конец списка." in captured.out
        linkedlist.prepend(10)
        captured = capsys.readouterr()
        assert "Элемент 10 добавлен в начало списка." in captured.out

        assert len(linkedlist) == 2

        linkedlist.delete(10)
        captured = capsys.readouterr()
        assert "Элемент 10 удалён из списка"

        assert len(linkedlist) == 1

        linkedlist.delete(15)
        captured = capsys.readouterr()
        assert "Элемент 15 не найден в списке"

        linkedlist.delete(20)
        captured = capsys.readouterr()
        assert "Элемент 20 удалён из списка"

        assert len(linkedlist) == 0

    def test_insert(self, capsys):
        linkedlist = LinkedList()
        linkedlist.append(20)
        captured = capsys.readouterr()
        assert "Элемент 20 добавлен в конец списка." in captured.out

        linkedlist.prepend(10)
        captured = capsys.readouterr()
        assert "Элемент 10 добавлен в начало списка." in captured.out

        linkedlist.insert(15, 1)
        captured = capsys.readouterr()
        assert f"Элемент 15 вставлен на позицию 1."

        assert len(linkedlist) == 3

        with pytest.raises(IndexError, match="Индекс вне диапазона."):
            linkedlist.insert(25, 7)

    def test_find(self):
        linkedlist = LinkedList()
        linkedlist.append(20)
        linkedlist.prepend(10)
        node = linkedlist.find(20)
        assert node is not None
        assert node.data == 20

        node = linkedlist.find(40)
        assert node is None

    def test_display(self, capsys):
        linkedlist = LinkedList()
        linkedlist.append(10)
        linkedlist.append(20)
        linkedlist.append(30)
        linkedlist.display()
        captured = capsys.readouterr()
        assert "10 -> 20 -> 30" in captured.out

        linkedlist.display(reverse=True)
        captured = capsys.readouterr()
        assert "30 -> 20 -> 10" in captured.out

    def test_len(self):
        linkedlist = LinkedList()
        linkedlist.append(10)
        assert len(linkedlist) == 1
        linkedlist.prepend(5)
        assert len(linkedlist) == 2

    def test_getitem(self):
        linkedlist = LinkedList()
        linkedlist.append(20)
        linkedlist.append(30)
        linkedlist.append(40)
        assert linkedlist[0] == 20
        assert linkedlist[1] == 30
        assert linkedlist[2] == 40

        with pytest.raises(IndexError, match="Индекс вне диапазона."):
            linkedlist[10]

    def test_linkedlist_iterator_empty(self):
        linkedlist = LinkedList()
        iterator = iter(linkedlist)
        with pytest.raises(StopIteration):
            next(iterator)

    def test_linkedlist_iterator_non_empty(self):
        linkedlist = LinkedList()
        linkedlist.append(40)
        linkedlist.append(50)
        linkedlist.append(60)
        iterator = iter(linkedlist)

        linkedlist.prepend(30)
        linkedlist.prepend(20)
        linkedlist.prepend(10)
        iterator = iter(linkedlist)

        assert next(iterator) == 10
        assert next(iterator) == 20
        assert next(iterator) == 30
        assert next(iterator) == 40
        assert next(iterator) == 50
        assert next(iterator) == 60

        with pytest.raises(StopIteration):
            next(iterator)
