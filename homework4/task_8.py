def merge_sort(arr):
    # Шаг 1: Проверяем базовый случай - если массив содержит один элемент или пустой,
    # то он уже отсортирован, поэтому возвращаем его
    if len(arr) <= 1:
        return arr

    # Шаг 2: Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Шаг 3: Объединяем две отсортированные половины
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # Шаг 4: Слияние двух отсортированных списков
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Шаг 5: Добавляем оставшиеся элементы из левого списка, если они есть
    while i < len(left):
        result.append(left[i])
        i += 1

    # Шаг 6: Добавляем оставшиеся элементы из правого списка, если они есть
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Пример использования
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)
