# Пользователь вводит список слов. Напишите программу, которая считает,
# сколько раз каждое слово встречается в списке, и сохраните результат в
# словарь. Слова Apple и apple считаются одинаковыми.
# Пример:
# >> “apple banana cherry apple banana”.
# {'apple': 2, 'banana': 2, 'cherry': 1}

word_list = input("Введите список слов через пробел: ").lower().split()
unique_words = set(word_list)
word_list_count = []
for word in unique_words:
    count = word_list.count(word)
    word_list_count.append((word, count))
word_list_count = dict(word_list_count)
print(word_list_count)
