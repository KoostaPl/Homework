def merge_sorted_list(list1, list2):
    merged_list = []
    i, j = 0, 0

    # Пока есть элементы в обоих списках
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Если остались элементы в list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Если остались элементы в list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_list(list1, list2))
