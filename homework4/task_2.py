def merge_dicts(dict_a, dict_b):
    for key, value in dict_b.items():
        if key in dict_a:
            if isinstance(dict_a[key], dict) and isinstance(value, dict):
                merge_dicts(dict_a[key], value)
            elif isinstance(dict_a[key], (list, set, tuple)) and isinstance(value, (list, set, tuple)):
                if len(dict_a[key]) == len(value):
                    if all(isinstance(a, (int, float, str)) and isinstance(b, (int, float, str)) for a, b in zip(dict_a[key], value)):
                        dict_a[key] = type(dict_a[key])([a + b for a, b in zip(dict_a[key], value)])
                else:
                    dict_a[key] = value
            else:
                dict_a[key] = value
        else:
            dict_a[key] = value

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

merge_dicts(dict_a, dict_b)
print(dict_a)