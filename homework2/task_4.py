# Пользователь вводит список слов. Напишите программу, которая считает,
# сколько раз каждое слово встречается в списке, и сохраните результат в
# словарь. Слова Apple и apple считаются одинаковыми.
# Пример:
# >> “apple banana cherry apple banana”.
# {'apple': 2, 'banana': 2, 'cherry': 1}

word_list = input("Введите список слов через пробел: ").lower().split()

word_counts = {}
for word in word_list:
    word_counts.setdefault(word, 0)
    word_counts[word] += 1

print(f"Результатом является: {word_counts}")