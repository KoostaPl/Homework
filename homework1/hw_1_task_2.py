string = input("Введите предложение: ")
punctuation = ".,!?;:"
result = (
    string.replace(".", " ")
    .replace(",", " ")
    .replace("!", " ")
    .replace("?", " ")
    .split()
)
print("Всего слов в предложении: ", len(result))
longest_word = max(result, key=len)
print("Самое длинное слово состоит из", len(longest_word), "символов")
