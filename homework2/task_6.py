# Пользователь вводит 2 слова. Напишите программу, которая проверяет,
# являются ли они анаграммами (первое слово может быть сформировано путем перестановки букв во втором слове).

word1, word2 = (input("Первое слово: ").lower()), (input("Второе слово: ").lower()) 
sortedwords1, sortedwords2 = sorted(word1), sorted(word2)
if sortedwords1 == sortedwords2:
    print(f"Слова {word1} и {word2} являются анаграммами")
else:
    print(f"Слова {word1} и {word2} не являются анаграммами")