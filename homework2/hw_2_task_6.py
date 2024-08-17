word1, word2 = (input("1 cлово: ").lower()), (input("2 слово: ").lower())
sortedwords1, sortedwords2 = sorted(word1), sorted(word2)
if sortedwords1 == sortedwords2:
    print(f"Слова {word1} и {word2} являются анаграммами")
else:
    print(f"Слова {word1} и {word2} не являются анаграммами")
