def unique_elements(list1):
    unique_set = set()

    def fltn(lst):
        for item in lst:
            if isinstance(item, list):
                fltn(item)
            else:
                unique_set.add(item)

    fltn(list1)
    return sorted(unique_set)


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))
